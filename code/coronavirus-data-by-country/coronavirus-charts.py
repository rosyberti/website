import datetime
from datetime import date
import pandas as pd
import numpy as np
import boto3
import smtplib
import matplotlib.pyplot as plt



data = pd.read_json('https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json')

s3 = boto3.resource('s3')

updateDate = datetime.datetime.today().strftime('%Y-%m-%d')

#############################################################################################
#Loop to create all DataFrames
#############################################################################################  

for country in data.columns:
    countryData = pd.DataFrame(pd.np.empty((0, 4)))
    confirmed = 0
    deaths = 0
    recovered = 0
    for dataPoint in data[country]:
        date = dataPoint['date']
        if(dataPoint['confirmed']>confirmed):
            confirmed = dataPoint['confirmed']
        if(dataPoint['deaths']>deaths):
            deaths = dataPoint['deaths']
        if(dataPoint['recovered']>recovered):
            recovered = dataPoint['recovered']
        countryData = countryData.append(pd.Series([date, confirmed, deaths, recovered]),ignore_index=True)
        
    
    countryData.columns = ['Date', 'Confirmed Cases','Confirmed Deaths','Confirmed Recoveries']
    

    plot1 = countryData.plot(kind='line',x='Date',y='Confirmed Cases',color='#135485', figsize=(15,6))
    plot1.set_title(country + ' Coronavirus Cases, Updated ' + updateDate + ', Current Level: ' + str(confirmed), fontsize=22)
    plt.savefig("output_files/"+country+' Cases.png')

    plot2 = countryData.plot(kind='line',x='Date',y='Confirmed Deaths',color='#135485', figsize=(15,6))
    plot2.set_title(country + ' Coronavirus Deaths, Updated ' + updateDate + ', Current Level: ' + str(deaths), fontsize=22)
    plt.savefig("output_files/"+country+' Deaths.png')

    plot3 = countryData.plot(kind='line',x='Date',y='Confirmed Recoveries',color='#135485', figsize=(15,6))
    plot3.set_title(country + ' Coronavirus Recoveries, Updated ' + updateDate + ', Current Level: ' + str(recovered), fontsize=22)
    plt.savefig("output_files/"+country+' Recoveries.png')

    #delete and re-upload each file

    s3.meta.client.upload_file("output_files/"+country+' Cases.png', 'coronavirus-country-charts', country+' Cases.png', ExtraArgs={'ACL':'public-read'})
    s3.meta.client.upload_file("output_files/"+country+' Deaths.png', 'coronavirus-country-charts', country+' Deaths.png', ExtraArgs={'ACL':'public-read'})
    s3.meta.client.upload_file("output_files/"+country+' Recoveries.png', 'coronavirus-country-charts', country+' Recoveries.png', ExtraArgs={'ACL':'public-read'})
