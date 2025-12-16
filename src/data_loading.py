#Import
import json
from pathlib import Path
import pandas as pd
import numpy as np
import requests


DATA_DIR = Path('../data')
DATA_DIR.mkdir(exist_ok=True,parents=True)

OUT_DIR = Path("../output")
OUT_DIR.mkdir(parents=True, exist_ok=True)

#Functions

def download_json_files(dase_url:str, decades: np.array, out_folder: Path) -> int:
  total = 0

  for i in decades:
    file_path = f"{dase_url}movies-{i}s.json"
    file_name = DATA_DIR / f"movies-{i}s.json"
    try:
      response = requests.get(file_path,timeout=20)
      response.raise_for_status()
      data = response.json()
      total += len(data)

      with open(file_name,'w',encoding='UTF-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)
      print(f"Saved {file_name} ({len(data)} records)")

    except Exception as e:
      print(f"Failed to fetch {file_path}: {e}")
  return total

def load_and_clean_json_files(decades:np.array, folder: Path) -> pd.DataFrame:
    full_data=[]

    for i in decades:
      path = folder / f'movies-{i}s.json'
      if not path.exists():
        continue
      with open(path,'r',encoding='UTF-8') as file:
        data = json.load(file)
        for d in data:
          for key in ['href', 'extract', 'thumbnail', 'thumbnail_width', 'thumbnail_height']:
            d.pop(key,None)
            if not d.get('title') or not d.get('year'):
              continue
            full_data.append(d)

    df = pd.DataFrame(full_data)

    # Clean columns
    df['genres'] = df['genres'].apply(lambda x: x if isinstance(x, list) else ([] if pd.isna(x) else [x]))
    df['cast'] = df['cast'].apply(lambda x: x if isinstance(x, list) else ([] if pd.isna(x) else [x]))

    df['year'] = pd.to_numeric(df['year'],errors = 'coerce').astype('Int64')
    df = df.dropna(subset=['year'])
    df['year']=df['year'].astype(int)
    return df

def save_dataframe(df: pd.DataFrame, path:Path):
  df.to_csv(path, index = False)
  print(f'Saved dataframe to {path} (rows: {len(df)})')