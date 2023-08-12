import sys
import matplotlib
import numpy as np

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

output = np.dot(weights, inputs) + biases
# print(output)

# Given annual income
annual_income = float(input("How much do you make annually: "))

# Number of weeks and days
weeks_per_year = 52
days_per_week = 7
minutes_per_hour = 60
hours_per_day = 24

# Calculating income per week, day, and minute
income_per_week = annual_income / weeks_per_year
income_per_day = income_per_week / days_per_week
income_per_minute = income_per_day / (minutes_per_hour * hours_per_day)

# Display the results
print("Income per week: ${:,.2f}".format(income_per_week))
print("Income per day: ${:,.2f}".format(income_per_day))
print("Income per minute: ${:,.2f}".format(income_per_minute))
