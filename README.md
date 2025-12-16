# Movie Dataset Analysis
## Project Overview
This project presents an end-to-end analysis of a historical movie dataset (1900–2019) obtained from Wikipedia. The analysis focuses on understanding trends in film genres, actor activity, and how actors’ filmographies distribute across popular genres over time.

The project demonstrates practical skills in data cleaning, exploratory data analysis, statistical aggregation, and data visualization using Python.

### Objectives

- Download and clean raw JSON movie datasets
- Aggregate top-10 genres and top-10 actors
- Analyze trends in genres and actor activity across decades
- Compare actor filmography in top-3 genres versus other genres
- Communicate insights through clear visualizations
- Export analysis results as CSV tables and PNG charts

### Analytical Questions

- Which genres are the most popular historically?
- Who are the top actors by number of films?
- How do genre trends evolve over time?
- How does an actor’s filmography distribute between top-3 genres and other genres?
- Which genres dominate the careers of the top-10 actors?

## Project Structure
movie-analysis/
│

├── data/             # Raw JSON files downloaded from Wikipedia

│

├── output/           # Generated CSV tables and plots

│

├── notebooks/        # Jupyter notebooks for analysis

│

├── src/              # Python scripts

│   ├── data_loading.py     # Downloading and cleaning JSON datasets

│   ├── data_analysis.py    # Aggregation and analytical functions

│   └── data_visualization.py # Plots and charts

│

├── requirements.txt

└── README.md


## Tools & Technologies

- Python 3.8+
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook
- Requests
- Data Preparation

## Key preprocessing steps:

- Downloading and saving decade-wise JSON movie files
- Cleaning unnecessary columns (href, extract, thumbnail, etc.)
- Converting year to numeric and handling missing values
- Normalizing genres and cast as lists

## Installation

Clone the repository:

```git clone <https://github.com/nvoitsitska-creator/MovieDatasetAnalysis.git>
cd movie-analysis
```

Create and activate a virtual environment:

```python -m venv .venv```
# Windows
```.venv\Scripts\activate```
# macOS/Linux
```source .venv/bin/activate```

Install dependencies:

```pip install -r requirements.txt```


## Load and preprocess data:

```from src.data_loading import download_json_files, load_and_clean_json_files, save_dataframe
import numpy as np
from pathlib import Path

DATA_DIR = Path('data')
OUT_DIR = Path('output')

decades = np.arange(1900, 2020, 10)
base_url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/refs/heads/master/"
```

# Download JSON files
```download_json_files(base_url, decades, DATA_DIR)```
# Load and clean
```df = load_and_clean_json_files(decades, DATA_DIR)
save_dataframe(df, OUT_DIR / 'movies_clean.csv')
```

## 📈 Analysis & Visualizations
### Genres Analysis
- Top-10 genres by number of films
- Distribution of films by top-10 genres (pie chart)
- Genre trends across decades (line plots)

### Actor Analysis
- Top-10 actors by number of films
- Trends of top-3 actors over time
- Comparison of films in top-3 genres versus other genres for top-10 actors
- Pivot table: actors vs genres (heatmap)

### Dashboards
Explore interactive visualizations on Looker Studio:
[Looker Studio Dashboard](https://lookerstudio.google.com/reporting/12cf5bbe-9486-44d5-bf83-08c40de09a6f)

## Output Artifacts

### CSV tables:
- movies_clean.csv – cleaned dataset
- top10_genres.csv
- top10_actors.csv
- top10_actors_top3_vs_other.csv

### Visualizations (PNG):
- Top-10 genres (bar + pie)
[Bar chart](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/top10_genres_bar.png)
[Pie chart](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/top10_genres_pie.png)
- Top-10 actors (bar)
[Bar chart](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/top10_actors_bar.png)
- Actors trends by year (linechart)
[Line chart](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/actors_trends_top3.png)
- Genre trends by year (linechart)
[Line chart](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/genre_trends_selected.png)
- Actor genre comparison (stacked bar)
[Stacked bar](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/actors_top3_vs_other_stacked.png)
- Actor vs genre pivot table (heatmap)
[Heatmap](https://github.com/nvoitsitska-creator/MovieDatasetAnalysis/blob/master/output/pivottable_actors_vs_genres.png)

## Key Insights
- Drama, Comedy, and Silent films dominate historical production
- Certain actors focus heavily on top-3 genres
- Genre trends show evolution across decades
- Actor activity can be clearly segmented by genre preferences

## 👩‍💻 Author
### Anastasiia Voitsitska
#### Data Analyst

📌 This project is part of my data analytics portfolio and demonstrates skills in data cleaning, exploratory analysis, visualization, and communicating insights effectively.