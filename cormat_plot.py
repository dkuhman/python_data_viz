import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sbn

# Import mtcars data
mydata = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
# Edit element of column header
mydata.rename(columns={'Unnamed: 0':'brand'}, inplace=True)
#Create correlation matrix
cormat = mydata.corr()
#Create a mask that will remove top triangle of the correlation matrix
mask_ut=np.triu(np.ones(cormat.shape)).astype(np.bool)

#PLOT
sbn.heatmap(cormat,linewidths=2.5,
            cmap='Greens',
            mask=mask_ut,
            vmin=-1,
            vmax=1,
            annot=True)
plt.show()