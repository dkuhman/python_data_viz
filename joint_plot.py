import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

#Import iris data
mydata = sbn.load_dataset('iris')

#Format font
font = {
    'family' : 'serif',
    'size' : 12,
    'weight' : 'bold',
    'color' : 'black',
}

#PLOT - SCATTER PLOT WITH DISTRIBUTIONS IN MARGINS
ax = sbn.jointplot("petal_length",
              "sepal_length",
              data=mydata,
              marginal_kws=dict(bins=15, rug=True),
              s=40,
              edgecolor="w",
              linewidth=1,
              color='red')
ax.set_axis_labels('Petal Length',
                   'Sepal Length',
                   fontdict=font)
plt.show()

#PLOT - DENSITY
ax = sbn.jointplot("petal_length",
              "sepal_length",
              data=mydata,
              kind='kde',
              linewidth=1,
              color='red')
ax.set_axis_labels('Petal Length',
                   'Sepal Length',
                   fontdict=font)
plt.show()