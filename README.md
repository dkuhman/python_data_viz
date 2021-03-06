# Data Visualization in Python

This repository hosts scripts related to data visualization in Python. 

---

## Line Plots
**Code:** `line_plot.py`

**Data:** data/city_weather_2019.csv

**Modules:** `pandas`, `matplotlib`

**Description:** This script generates a line plot of weather across days of the year for two separate cities. The script also provides good examples of `pandas` functionality, particularly string manipulation (for dates). In the second plot below, I used `df.rolling(5).mean()` to apply a 5-step moving average to both curves. 

**Video Tutorial:** https://youtu.be/cWXnPYJGe4g

<img src=media/line_plot.png width=47%><img src=media/line_plot_mov_avg.png width=47%>

---

## Scatter Plots
**Code:** `scatter_plot.py`

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c)

**Modules:** `pandas`, `numpy`, `matplotlib`

**Description:** This script generates a scatter plot of MPG vs HP from the mtcars dataset. The script also provides good examples of text manipulation on the plot (e.g., font style, weight, color, and padding). The script also provides a `numpy` template for adding a line of best fit (1st order ploynomial) to the scatter data.

**Video Tutorial:** https://youtu.be/6V23myHGdng

<img src=media/scatter_plot.png width=47%><img src=media/scatter_plot_bfl.png width=47%>

---

## Bar Plots
**Code:** `bar_plot.py`

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c)

**Modules:** `pandas`, `numpy`, `matplotlib`

**Description:** This script generates two bar plots - one of MPG vs cylinder count and one of multiple variables grouped by cyclinder count. All data comes from the mtcars dataset. The script also provides good examples of common `pandas` functionality (e.g., `.mean()`, `.std()`, and `.groupby()`).

**Video Tutorials:**
  * https://youtu.be/8F92B7lYV9Y 
  * https://youtu.be/vUOOOpN3dw4

<img src=media/bar_plot_basic.png width=47%><img src=media/bar_plot_grouped.png width=47%>

---

## Box Plots
**Code:** `box_plot.py`

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c) and iris (loaded from Seaborn)

**Modules:** `pandas`, `matplotlib`, `seaborn`

**Description:** This script generates two box plots - one of MPG vs cylinder count (from the mtcars data set) and one of sepal width as a function of plant species and sepal length (from the iris data set). The script incoporates functions from the `seaborn` module.

<img src=media/box_plot_basic.png width=47%><img src=media/box_plot_grouped.png width=47%>

---

## Heat Mapped Correlation Matrix
**Code:** `cormat_plot.py`

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c)

**Modules:** `pandas`, `numpy`, `matplotlib`, `seaborn`

**Description:** This script generates a heat mapped correlation matrix from the mtcars data set.

<img src=media/cor_heat_map.png width=47%><img src=media/cor_heat_map_annot.png width=47%>

---

## Histograms
**Code:** `histogram_plot.py`

**Data:** mtcars.csv (loaded from https://gist.github.com/ZeccaLehn/4e06d2575eb9589dbe8c365d61cb056c)

**Modules:** `pandas`, `matplotlib`, `seaborn`

**Description:** This script generates example histograms using the mtcars data set.

<img src=media/histogram_basic.png width=47%><img src=media/histogram_grouped.png width=47%>

---

## Joint Plots
**Code:** `joint_plot.py`

**Data:** iris (loaded from Seaborn)

**Modules:** `matplotlib`, `seaborn`

**Description:** This script generates examples of joint plots, which have a main, center panel and marginal panels.

<img src=media/scatter_plot_joint.png width=47%><img src=media/density_plot_joint.png width=47%>
