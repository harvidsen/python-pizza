#%%
import os
import pandas as pd
from io import StringIO
from azure.storage.blob import ContainerClient
""" Get solardata from Plant 1 

TODO: 
- Get solardata from Plant 2 also
- Check for missing data
- Do we need continuity on 15min frequency?
"""

#%%

datasets_url_path = os.environ.get('BPEXT_DATASETS_SAS_URL')
assert datasets_url_path is not None, 'No SAS url was found for datasets'
with open(datasets_url_path, 'r') as f:
    container = ContainerClient.from_container_url(f.read())

# %%

# blobs_paths = [
#     'kaggle-solarpower/Plant_1_Generation_Data.csv',
#     'kaggle-solarpower/Plant_2_Generation_Data.csv',
#     'kaggle-solarpower/Plant_1_Weather_Sensor_Data.csv',
#     'kaggle-solarpower/Plant_2_Weather_Sensor_Data.csv',
# ]

stream = container.download_blob('kaggle-solarpower/Plant_1_Generation_Data.csv')
content = stream.content_as_text()

df_generation = pd.read_csv(
    StringIO(content),
    usecols=['DATE_TIME', 'AC_POWER'],
    index_col=0,
)
df_generation.index = pd.to_datetime(df_generation.index, format='%d-%m-%Y %H:%M')
df_generation = df_generation.resample('15min').mean()

#%%

stream = container.download_blob('kaggle-solarpower/Plant_1_Weather_Sensor_Data.csv')
content = stream.content_as_text()

df_weather = pd.read_csv(
    StringIO(content),
    usecols=['DATE_TIME', 'AMBIENT_TEMPERATURE', 'IRRADIATION'],
    index_col=0,
)
df_weather.index = pd.to_datetime(df_weather.index, format='%Y-%m-%d %H:%M:%S')

# %%

df = df_generation.join(df_weather).dropna()

# %%
