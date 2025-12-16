import pandas as pd
import warnings

warnings.filterwarnings('ignore')

def top_genres(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    df_genres = df.explode('genres')
    df_genres = df_genres[df_genres['genres'].notna()]
    return (
        df_genres.groupby('genres', as_index=False)['title']
        .nunique()
        .rename(columns={'title':'number of films'})
        .sort_values('number of films', ascending=False)
        .head(top_n)
        )

def top_actors(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    df_cast = df.explode('cast')
    df_cast = df_cast[df_cast['cast'].notna()]
    return (
        df_cast.groupby('cast', as_index=False)['title']
        .nunique()
        .rename(columns={'cast':'actor','title':'number of films'})
        .sort_values('number of films', ascending=False)
        .head(top_n)
    )

def genre_trends(df: pd.DataFrame, genres: list) -> pd.DataFrame:
    return (
        df.explode("genres")
        .dropna(subset=["genres"])
        .groupby(["genres", "year"], as_index=False)["title"]
        .count()
        .rename(columns={'title': 'count'})
        .query("genres in @genres")
    )


def actor_trends(df: pd.DataFrame, actors: list) -> pd.DataFrame:
    return (
        df.explode("cast")
        .dropna(subset=["cast"])
        .groupby(["cast", "year"], as_index=False)["title"]
        .nunique()
        .rename(columns={'title':'count','cast': 'actor'})
        .query("actor in @actors")
    )

def actor_genre_summary(df: pd.DataFrame, top_actors: pd.DataFrame, top_genres: pd.DataFrame) -> pd.DataFrame:
    top3_genres = top_genres['genres'].head(3).tolist()
    top10_actors = top_actors['actor'].tolist()

    df_local = df.copy()

    df_local['has_top3'] = df_local['genres'].apply(lambda g: any(genre in top3_genres for genre in g))

    df_top3 = df_local[df_local['has_top3']].explode('cast')
    df_other = df_local[~df_local['has_top3']].explode('cast')

    group_top3 = (
        df_top3
        .groupby('cast')['title']
        .nunique()
        .reset_index()
        .rename(columns={'cast': 'actor','title':'number in top3'})
    )

    group_other = (
        df_other
        .groupby('cast')['title']
        .nunique()
        .reset_index()
        .rename(columns={'cast': 'actor','title':'number in other'})
    )

    result = group_top3.merge(group_other, on ='actor', how = 'outer').fillna(0)
    result = result[result['actor'].isin(top10_actors)]

    actors_movies = top_actors.rename(columns={'number of films': 'total_movies'})
    result = result.merge(actors_movies[['actor', 'total_movies']], on = 'actor', how = 'left')
    result[['number in top3', 'number in other']] = result[['number in top3', 'number in other']].astype(int)
    result['% of top3'] = (result['number in top3'] / result['total_movies'] * 100).round(2)
    return result