# -*- coding: utf-8 -*-
"""DS410 CODE ALVARO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R_NGRfUj00DUX0Tv8FPf86y3wK1n5LBE

# Code for DS410
"""

# Creating Correlation Matrix

import matplotlib.pyplot as mp
import seaborn as sb
# create a correlation matrix of the features
corr_matrix = round(df.corr(), 2) ##################### Change for name of the dataset in "df"

# create heatmap
sb.heatmap(corr_matrix, annot=True, cmap='YlGnBu')
mp.show()

# Creating the bar graph category vs. sentiment
import matplotlib.pyplot as plt

# create a color map
cmap = plt.cm.get_cmap('coolwarm')

# normalize the sentiment values to the range of the color map
norm = plt.Normalize(df['quantitativeCOLUMN'].min(), df['quantitativeCOLUMN'].max()) ##################### Change for name of the dataset in "df"

# create a list of colors corresponding to the sentiment values
colors = [cmap(norm(i)) for i in df['quantitativeCOLUMN']] ##################### Change for name of the dataset in "df"

# reverse the order of the colors
colors = colors[::-1]

# create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# create the horizontal bar plot
ax.barh(df['qualitativeCOLUMN'], df['quantitativeCOLUMN'], color=colors) ##################### Change for name of the dataset in "df"

# set the axis labels and title
ax.set_xlabel('Name of the quantitative feature')
ax.set_ylabel('Name of the qualitative feature')
ax.set_title('Title for the graph')

# show the plots

# Creating the linear model, lasso regression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score

# Reshape the data (required for scikit-learn)
time = time.reshape(-1, 1)
demand = demand.reshape(-1, 1)

# Create and train the Lasso regression model
alpha = 0.1  # L1 regularization strength (you can adjust this parameter)
model = Lasso(alpha=alpha)
model.fit(time, demand)

# Make predictions
feature_pred = model.predict(time)

# Calculate the mean squared error and R-squared (accuracy)
mse = mean_squared_error(demand, feature_pred)
r2 = r2_score(demand, feature_pred)

# Plot the data and the Lasso regression line
plt.scatter(time, demand, label="Actual Demand")
plt.plot(time, feature_pred, color="red", label="Trend Line")

plt.title("Lasso Regression for Demand Prediction")
plt.xlabel("Time")
plt.ylabel("Demand")
plt.legend()
plt.grid(True)

plt.show()

print(f"Lasso Regression Equation: Demand = {model.coef_[0]:.2f} * Time + {model.intercept_[0]:.2f}")
print(f"Mean Squared Error: {mse:.2f}")
print(f"R-squared (Accuracy): {r2:.2f}")