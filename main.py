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
