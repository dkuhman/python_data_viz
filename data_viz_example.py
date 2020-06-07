import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

mydata = pd.read_csv('data/city_weather_2019.csv')
mydata = mydata[['city', 'week_day', 'date', 'temp_low1', 'temp_low2', 'temp_low3', 'temp_low4',
                 'temp_high1', 'temp_high2', 'temp_high3', 'temp_high4']]
mydata['temp_low1'] = pd.to_numeric(mydata['temp_low1'], errors='coerce')
mydata['temp_low2'] = pd.to_numeric(mydata['temp_low2'], errors='coerce')
mydata['temp_low3'] = pd.to_numeric(mydata['temp_low3'], errors='coerce')
mydata['temp_low4'] = pd.to_numeric(mydata['temp_low4'], errors='coerce')
mydata['temp_high_avg'] = (mydata['temp_high1'] + mydata['temp_high2'] + mydata['temp_high3'] + mydata['temp_high4'])/4
mydata['temp_low_avg'] = (mydata['temp_low1'] + mydata['temp_low2'] + mydata['temp_low3'] + mydata['temp_low4'])/4

plt.plot(mydata.date[mydata['city']=='birmingham'], mydata.temp_high_avg[mydata['city']=='birmingham'])
plt.plot(mydata.date[mydata['city']=='cleveland'], mydata.temp_high_avg[mydata['city']=='cleveland'])
plt.title('Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (F)')
plt.legend(['Birmingham', 'Cleveland'])
plt.show()
