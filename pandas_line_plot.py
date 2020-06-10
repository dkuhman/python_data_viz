import pandas as pd
from matplotlib import pyplot as plt

mydata = pd.read_csv('data/city_weather_2019.csv')

mydata = mydata[['city', 'date', 'temp_high1', 'temp_high2', 'temp_high3', 'temp_high4']]
mydata['temp_high_avg'] = (mydata['temp_high1'] + mydata['temp_high2'] +mydata['temp_high3'] + mydata['temp_high4'])/4

mydata['date'] = mydata['date'].astype(str) + '-2019'
mydata['date'] = mydata['date'].str.lstrip(' ')
mydata['date'] = mydata['date'].replace(' ', '-', regex=True)
mydata['date'] = mydata['date'].replace('Jan', '01', regex=True)
mydata['date'] = mydata['date'].replace('Feb', '02', regex=True)
mydata['date'] = mydata['date'].replace('Mar', '03', regex=True)
mydata['date'] = mydata['date'].replace('Apr', '04', regex=True)
mydata['date'] = mydata['date'].replace('May', '05', regex=True)
mydata['date'] = mydata['date'].replace('Jun', '06', regex=True)
mydata['date'] = mydata['date'].replace('Jul', '07', regex=True)
mydata['date'] = mydata['date'].replace('Aug', '08', regex=True)
mydata['date'] = mydata['date'].replace('Sep', '09', regex=True)
mydata['date'] = mydata['date'].replace('Oct', '10', regex=True)
mydata['date'] = mydata['date'].replace('Nov', '11', regex=True)
mydata['date'] = mydata['date'].replace('Dec', '12', regex=True)
mydata['date'] = pd.to_datetime(mydata['date'])

plt.plot(mydata['date'][mydata['city']=='birmingham'], mydata['temp_high_avg'][mydata['city']=='birmingham'], 'b-')
plt.plot(mydata['date'][mydata['city']=='cleveland'], mydata['temp_high_avg'][mydata['city']=='cleveland'], 'r-')
plt.title('Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.legend(['Birmingham', 'Cleveland'])
plt.show()
