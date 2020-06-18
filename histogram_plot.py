import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

# Import mtcars data
mydata = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
# Edit element of column header
mydata.rename(columns={'Unnamed: 0':'brand'}, inplace=True)

#Format font
font = {
    'family' : 'serif',
    'size' : 12,
    'weight' : 'bold',
    'color' : 'black',
}

#PLOT BASIC HISTOGRAM
sbn.distplot(mydata['mpg'],
             color='DarkBlue',
             label='4 Cylinders',
             hist_kws=dict(edgecolor="white", linewidth=2))
plt.xlabel('Fuel Efficiency (MPG)',
           fontdict=font,
           labelpad=10)
plt.show()

#PLOT GROUPED HISTOGRAM
sbn.distplot(mydata['mpg'].loc[mydata['cyl']==4],
             color='DarkBlue',
             label='4 Cylinders',
             hist_kws=dict(edgecolor="white", linewidth=2),
             rug=True)
sbn.distplot(mydata['mpg'].loc[mydata['cyl']==6],
             color='DarkRed',
             label='6 Cylinders',
             hist_kws=dict(edgecolor="white", linewidth=2),
             rug=True)
sbn.distplot(mydata['mpg'].loc[mydata['cyl']==8],
             color='DarkGreen',
             label='8 Cylinders',
             hist_kws=dict(edgecolor="white", linewidth=2),
             rug=True)
plt.xlabel('Fuel Efficiency (MPG)',
           fontdict=font,
           labelpad=10)
plt.legend()
plt.show()