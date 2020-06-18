import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sbn

# Import mtcars data
mydata = pd.read_csv('https://gist.githubusercontent.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c/raw/64f1660f38ef523b2a1a13be77b002b98665cdfe/mtcars.csv')
# Edit element of column header
mydata.rename(columns={'Unnamed: 0':'brand'}, inplace=True)

#Import iris data
mydata_2 = sbn.load_dataset('iris')
#Create a categorical column based on sepal length > or < 5 (arbitrary)
mydata_2['sepal_length_cat'] = 'Small'
mydata_2.loc[mydata_2['sepal_length'] > 5, 'sepal_length_cat'] = 'Large'
print(mydata_2.info())

#Format font styling
font = {'family': 'serif',
        'color': 'black',
        'weight': 'bold',
        'size': 12
        }

#BASIC BOX PLOT USING MTCARS DATA
ax = sbn.boxplot(x="cyl", y="mpg", data=mydata, color='#3399ff', whis=3, linewidth=2.5)
#Add individual data points
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

#GROUPED BOX PLOT USING IRIS DATA
ax = sbn.boxplot(x="species", y="sepal_width", data=mydata_2, hue='sepal_length_cat', whis=3, linewidth=2.5)
ax = plt.xlabel('Species',
                fontdict=font,
                labelpad=10
                )
ax = plt.ylabel('Sepal Width',
                fontdict=font,
                labelpad=10
                )
plt.show()