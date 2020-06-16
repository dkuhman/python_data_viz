import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sbn


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

print(mydata.info())

ax = sbn.boxplot(x="cyl", y="mpg", data=mydata, color='#3399ff', whis=3, linewidth=2.5)
ax = sbn.swarmplot(x="cyl", y="mpg", data=mydata, color="black", size=6)
ax = plt.xlabel('Cylinders',
                fontdict=font,
                labelpad=10
                )
ax = plt.ylabel('Miles per Gallon (MPG)',
                fontdict=font,
                labelpad=10
                )
plt.show()