import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')

finalData = pd.DataFrame(pd.np.empty((0, 5)))

for country in countries:
  for dataPoint in populationData:
