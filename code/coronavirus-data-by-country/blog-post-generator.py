import pandas as pd

data = pd.read_json('https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json')

data = data.reindex(sorted(data.columns), axis=1)

for country in data.columns:
    print("""
## """+country+"""

!["""+country+""" Coronavirus Cases](https://coronavirus-country-charts.s3.ca-central-1.amazonaws.com/"""+country+"""+Cases.png)

!["""+country+""" Coronavirus Deaths](https://coronavirus-country-charts.s3.ca-central-1.amazonaws.com/"""+country+"""+Deaths.png)
