import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import datetime
from datetime import date

finalData = pd.DataFrame(pd.np.empty((0, 5)))

#############################################################################################
#Drawdown calculation
#############################################################################################
countryETFs = {
              'United States': 'SPY',
              'China': 'MCHI', 
              'Japan': 'EWJ',
              'Germany': 'EWG',
              'India': 'INDA', 
              'United Kingdom': 'EWU',
              'France': 'EWQ',
              'Italy': 'EWI',
              'Brazil': 'EWZ',
              'Canada': 'EWC'
              }

countryDrawdowns = {
              'United States': 0.00,
              'China': 0.00,
              'Japan': 0.00,
              'Germany': 0.00,
              'India': 0.00,
              'United Kingdom': 0.00,
              'France': 0.00,
              'Italy': 0.00,
              'Brazil': 0.00,
              'Canada': 0.00,
              }

for country in list(countryETFs.keys()):
  b = countryETFs[country]
  tgt_website = r'https://sg.finance.yahoo.com/quote/'+b+'/key-statistics?p='+b
  stock_company = f"https://finance.yahoo.com/quote/{b}"
  soup = BeautifulSoup(requests.get(stock_company).text, "html.parser")
  ticker_data_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{b}?symbol={b}&period1=1546300800&period2=9999999999&interval=1d"
  ticker_data = json.loads(requests.get(ticker_data_url).text)
  closingPrices = pd.Series(ticker_data['chart']['result'][0]['indicators']['quote'][0]['close'])

  dollarDrawdown = (closingPrices - closingPrices.cummax()).min()
  maxPrice = -list(closingPrices.cummax())[-1]
  maxDrawdown = dollarDrawdown/maxPrice
  
  countryDrawdowns[country] = maxDrawdown
  
#############################################################################################
#Coronavirus cases
#############################################################################################
coronavirusCases = {
              'United States': 0.00,
              'China': 0.00,
              'Japan': 0.00,
              'Germany': 0.00,
              'India': 0.00,
              'United Kingdom': 0.00,
              'France': 0.00,
              'Italy': 0.00,
              'Brazil': 0.00,
              'Canada': 0.00,
              }

coronavirusData = pd.read_json('https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json')
updateDate = datetime.datetime.today().strftime('%Y-%m-%d')

for country in list(countryETFs.keys()):
  pass

#############################################################################################
#Coronavirus Deaths
#############################################################################################
coronavirusDeaths = {
              'United States': 0.00,
              'China': 0.00,
              'Japan': 0.00,
              'Germany': 0.00,
              'India': 0.00,
              'United Kingdom': 0.00,
              'France': 0.00,
              'Italy': 0.00,
              'Brazil': 0.00,
              'Canada': 0.00,
              }

for country in list(countryETFs.keys()):
  pass

#############################################################################################
#Country populations
#############################################################################################
populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')

for country in list(countryETFs.keys()):
  pass

#############################################################################################
#Creation of the finalized DataFrame
#############################################################################################
for country in list(countryETFs.keys()):
#     finalData = finalData.append(pd.Series[country,countryDrawdowns[country],CoronaCases[country],coronaDeaths[country],populationData[country]], ignore_index=True)
    pass
#############################################################################################
#Plot
#############################################################################################
