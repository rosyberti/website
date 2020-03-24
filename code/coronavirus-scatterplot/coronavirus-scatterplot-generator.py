import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

countries = ['China', 
             'India', 
             'United States', 
             'Indonesia', 
             'Pakistan', 
             'Brazil', 
             'Nigeria', 
             'Bangladesh', 
             'Russia', 
             'Mexico']

populationData = pd.read_json('https://raw.githubusercontent.com/samayo/country-json/master/src/country-by-population.json')
