# Movie Dataset Analysis

This project explores a historical movie dataset (1900–2019) obtained from Wikipedia, analyzing trends in genres and actor activity. The goal is to identify top genres, top actors, and how their filmography distributes across popular genres over time.

## Features
- Download and clean JSON movie datasets
- Aggregate top-10 genres and top-10 actors
- Visualize trends in film genres and actor activity over decades
- Compare actor filmography in top-3 genres versus other genres
- Export results as CSV and PNG files

## Dashboards

- Looker Studio link - https://lookerstudio.google.com/reporting/67c4e20d-1998-4740-b605-b7b47fc19d18

## Project Structure
movie-analysis/
├── data/        # raw JSON files

├── output/      # results and plots

├── notebooks/   # analysis notebooks

├── src/         # Python scripts

├── requirements.txt

└── README.md


## Requirements
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- requests

Install dependencies:
```bash
pip install -r requirements.txt
