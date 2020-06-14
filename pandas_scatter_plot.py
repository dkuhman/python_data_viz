import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# Import CSV mtcars
mydata = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
# Edit element of column header
mydata.rename(columns={'Unnamed: 0':'brand'}, inplace=True)
print(mydata.head(20))
print(mydata.info())

#Format font styling
font = {'family': 'serif',
        'color': 'black',
        'weight': 'bold',
        'size': 12
        }

#Plot
plt.scatter(mydata['mpg'],
            mydata['hp'],
            c='DarkBlue',
            s=30
            )
#Add line of best fit
plt.plot(np.unique(mydata['mpg']),
         np.poly1d(np.polyfit(mydata['mpg'],
                              mydata['hp'], 1))(np.unique(mydata['mpg'])),
         c='DarkBlue'
         )
plt.xlabel('Fuel Efficiency (MPG)',
           fontdict=font,
           labelpad=10
           )
plt.ylabel('Horse Power',
           fontdict=font,
           labelpad=10
           )
plt.title('MPG vs HP',
          fontdict=font)
plt.show()