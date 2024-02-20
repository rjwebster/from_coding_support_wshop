# Tuesday 20th Feb Coding support workshop

import pandas as pd
import opendatasets as od
import os

# Once loaded into environment, Python sees it not as a file, as a dataframe

df =  pd.read_csv('heart.csv') # A word plus () tells python its a fn
df

df.describe(df)

dataset = 'https://www.kaggle.com/datasets/malayvyas/google-stock-data'
od.download(dataset)

# Get from kaggle file - api in settings -> json file with 

# {"username":"rebeccajw1","key":"4b3107f8266ff2f7b6a4cbc86b695eab"}

data_dir = '.\google-stock-data'
os.listdir(data_dir)

