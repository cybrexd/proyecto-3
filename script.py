import datetime
import requests
import pandas as pd
from client import FtxClient
from local_settings import ftx as settings

api_url = 'https://ftx.us/api'
api = '/markets'
url = api_url+api

market_name = 'ETH/USD'
path = f'/markets/{market_name}'
url = api_url + path

res = requests.get(url).json()
df = pd.DataFrame(res)['result']
print(df)