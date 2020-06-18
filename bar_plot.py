import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Import CSV mtcars
mydata = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
# Edit element of column header
mydata.rename(columns={'Unnamed: 0':'brand'}, inplace=True)

#Format font styling
font = {'family': 'serif',
        'color': 'black',
        'weight': 'bold',
        'size': 12
        }

#PREPARE BASIC PLOT
means_4cyl = mydata[mydata['cyl']==4].mean()
means_6cyl = mydata[mydata['cyl']==6].mean()
means_8cyl = mydata[mydata['cyl']==8].mean()
stds_4cyl = mydata[mydata['cyl']==4].std()
stds_6cyl = mydata[mydata['cyl']==6].std()
stds_8cyl = mydata[mydata['cyl']==8].std()

cylinders = ['4 Cyl', '6 Cyl', '8 Cyl']
axis_position = np.arange(len(cylinders))
mpg_means = [means_4cyl['mpg'], means_6cyl['mpg'], means_8cyl['mpg']]
mpg_stds = [stds_4cyl['mpg'], stds_6cyl['mpg'], stds_8cyl['mpg']]

fig, ax = plt.subplots()
ax.bar(axis_position, mpg_means, yerr=mpg_stds, align='center', alpha=0.7, color='blue', ecolor='black', capsize=10, edgecolor='black')
ax.set_ylabel('Fuel Efficiency (MPG)',
              fontdict=font,
              labelpad=10
              )
ax.set_xticks(axis_position)
ax.set_xticklabels(cylinders,
                   fontdict=font,
                   )
plt.show()

#PREPARE GROUPED PLOT
#Create df with figure data
df_means = mydata.groupby('cyl').mean()
df_stds = mydata.groupby('cyl').std()
df_means = df_means[['mpg', 'hp', 'qsec']]
df_stds = df_stds[['mpg', 'hp', 'qsec']]

#Plot
df_means.plot(kind='bar', edgecolor='black')
plt.xlabel('Cylinders',
           fontdict=font,
           labelpad=10
           )
plt.ylabel('',
           fontdict=font,
           labelpad=10
           )
plt.show()