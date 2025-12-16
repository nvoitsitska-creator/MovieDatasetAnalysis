import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from pathlib import Path

sns.set_style('whitegrid')
plt.rcParams.update({'figure.dpi': 120})

def save_and_show(path: Path):
    plt.tight_layout()
    plt.savefig(path)
    plt.show()

def plot_top_genres_bar(df: pd.DataFrame, OUT_DIR: Path)-> None:
    #Bar chart
    fig,ax=plt.subplots(figsize=(10,6))
    sns.barplot( x='genres', y='number of films', data=df, palette = 'Blues_d')
    plt.title('Top 10 genres by number of films')
    plt.xlabel("Genre")
    plt.ylabel("Number of films")
    plt.yticks(range(0,15000,1000))
    plt.xticks(rotation = 45, ha = 'right')
    save_and_show(OUT_DIR / 'top10_genres_bar.png')

def plot_top_genres_pie(df: pd.DataFrame, OUT_DIR: Path)-> None:
    #Pie chart
    plt.figure(figsize=(7,7))
    plt.pie(df['number of films'],
            labels=df['genres'],
            startangle=90,
            autopct='%1.1f%%',
            pctdistance=0.8,
            colors=sns.color_palette("pastel"),
            counterclock=False)
    plt.title("Distribution of films by top 10 genres")
    plt.tight_layout()
    save_and_show(OUT_DIR / 'top10_genres_pie.png')


def plot_top10_actors_bar(df: pd.DataFrame, OUT_DIR: Path)-> None:
    plt.figure(figsize=(12, 6))
    sns.barplot(x='actor', y='number of films', data=df, palette="BuGn_r")
    plt.title('Top 10 actors by number of films', pad=12)
    plt.xlabel('Actor')
    plt.ylabel('Number of films')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    save_and_show(OUT_DIR / 'top10_actors_bar.png')

def plot_genre_trends_by_year(df: pd.DataFrame, OUT_DIR: Path)-> None:
    plt.figure(figsize=(12,7))
    sns.lineplot(data=df,x='year',y='count',hue='genres',marker = 'o')
    plt.title('Number of Films by Year (Selected Genres)')
    plt.xlabel('Year')
    plt.ylabel('Number of films')
    plt.xticks(range(1900,2030,10), rotation = 45)
    plt.grid(True,linestyle='--',alpha = 0.5)
    plt.tight_layout()
    save_and_show(OUT_DIR / 'genre_trends_selected.png')

def plot_actor_trends_top3(df: pd.DataFrame, OUT_DIR: Path) -> None:
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df,x="year",y="count",hue="actor",marker="o")
    plt.title("Number of Films by Year for Top-3 Actors")
    plt.xlabel("Year")
    plt.ylabel("Number of Films")
    plt.xticks(rotation=30)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    save_and_show(OUT_DIR / "actors_trends_top3.png")


def plot_actor_genre_stacked(result, OUT_DIR: Path)-> None:
    plt.figure(figsize=(12, 6))
    x = np.arange(len(result))
    plt.bar(x, result['number in top3'], label='Top3 genres', color='#679577')
    plt.bar(x, result['number in other'], bottom=result['number in top3'], label='Other genres', color='#d98181')
    plt.legend()
    plt.title("Top-3 genres vs Other for Top-10 actors")
    plt.xlabel("Actors")
    plt.ylabel("Number of films")
    plt.tight_layout()
    plt.xticks(x, result['actor'], rotation=45)
    plt.xticks(rotation=45)
    plt.ylim(0, (result['number in top3'] + result['number in other']).max() * 1.1)
    save_and_show(OUT_DIR / 'actors_top3_vs_other_stacked.png')

def plot_actor_genre_heatmap(df: pd.DataFrame, OUT_DIR: Path) -> None:
    plt.figure(figsize=(12, 6))
    sns.heatmap(df, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5, cbar=True)
    plt.title("Top-10 Actors: Number of Films in Top-3 Genres")
    plt.xlabel("Genre")
    plt.ylabel("Actor")
    plt.tight_layout()
    save_and_show(OUT_DIR / "pivottable_actors_vs_genres.png")
