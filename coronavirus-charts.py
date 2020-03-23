import datetime
from datetime import date
import pandas as pd
import numpy as np
import boto3
import smtplib
import matplotlib.pyplot as plt

data = pd.read_json('https://raw.githubusercontent.com/pomber/covid19/master/docs/timeseries.json')
countryData = pd.DataFrame(pd.np.empty((0, 4)))

#############################################################################################
#Comment this out for production
#############################################################################################  

countryData = countryData['Thailand']

#############################################################################################
#Loop to create all DataFrames
#############################################################################################  

for country in data.columns:
    countryData = pd.DataFrame(pd.np.empty((0, 4)))
    for dataPoint in data[country]:
        date = dataPoint['date']
        confirmed = dataPoint['confirmed']
        deaths = dataPoint['deaths']
        recovered = dataPoint['recovered']
        countryData = countryData.append(pd.Series([date, confirmed, recovered, deaths]),ignore_index=True)
        print(countryData)
    
    countryData.columns = ['Date', 'Confirmed Cases','Confirmed Deaths','Confirmed Recoveries']
    
#############################################################################################
#Get today's date
#############################################################################################  

timeForS3Push = datetime.datetime.today().strftime('%Y-%m-%d')

#############################################################################################
#Push the .xlsx documents to AWS S3
#############################################################################################  

# #initialize an s3 object

# s3 = boto3.resource('s3')

# #delete and re-upload each file

# s3.meta.client.delete_object(Bucket='sure-dividend-data-feeds', Key= securityGroup[:-4] + '.xlsx')
# s3.meta.client.upload_file("output_files/"+securityGroup[:-4]+'.xlsx', 'sure-dividend-data-feeds', securityGroup[:-4]+'.xlsx', ExtraArgs={'ACL':'public-read'})


#############################################################################################
#Send email to Nick notifying him that the script has run successfully
#############################################################################################  

# time = datetime.datetime.now().strftime("%I%M%p on %B %d, %Y")
# content = 'Subject: {}\n\n{}'.format('Generic Builder - Complete', 'The generic data feeds builder Python script has been completed at ' + time + ' Universal Coordinated Time (UTC)')
# mail = smtplib.SMTP('smtp.gmail.com', 587)
# mail.ehlo()

# mail.starttls()

# password = 'EngineeringPass123'

# mail.login('engineering@suredividend.com',password)
# mail.sendmail('engineering@suredividend.com','nick@suredividend.com',content)

# #Close the connection.
# mail.close()
