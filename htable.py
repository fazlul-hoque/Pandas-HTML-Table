

#Author: Md.Fazlul Hoque
#Source: Stackoverflow and answered by the author
#Source link: https://stackoverflow.com/questions/68249881/why-read-html-from-python-pandas-not-working/68250007#68250007


import pandas as pd
import requests
url_link = 'https://finance.yahoo.com/quote/NFLX/history?p=NFLX%27'
r = requests.get(url_link,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
read_html_pandas_data = pd.read_html(r.text)[0]
print(read_html_pandas_data)