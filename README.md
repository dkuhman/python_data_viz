# Data Visualization in Python
**IN PROGRESS!**

This repository hosts scripts related to data visualization in Python.

---

## Line Plots
**Code:** pandas_line_plot.py

**Data:** data/city_weather_2019.csv

**Description:** This script generates a line plot of weather across days of the year for two separate cities. The script also provides good examples of Pandas functionality, particularly string manipulation (for dates). In the second plot below, I used `df.rolling(5).mean()` to apply a 5-step moving average to both curves. 

<img src=media/line_plot.png width=70%>

<img src=media/line_plot_mov_avg.png width=70%>

---

## Scatter Plots
**Code:** pandas_scatter_plot.py

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c)

**Description:** This script generates a scatter plot of MPG vs HP from the mtcars dataset. The script also provides good examples of text manipulation on the plot (e.g., font style, weight, color, and padding).

<img src=media/scatter_plot.png width=70%>
