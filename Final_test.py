#######################################################################################################################################################
# 
# Name: Snehasish Kaibartta
# SID: 740100109
# Exam Date: 28/03/2025
# Module: BEMM458
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-friday-EXsk1002.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# My sid is 740100109 
# My first and last numbers are 7 and 9
# Initialize a dictionary to store keyword counts
keyword_counts = {}
SID_keys = [7, 9]
# Write your code to process the text and count keyword occurrences
for key in SID_keys:
    word = keywords[key]
    keyword_counts[word] = customer_reviews.count(word)
    
# Print the keyword counts
print("Counts are for the keywords",keyword_counts)  # OUTPUT will be added here

# creating a empty list to store the (start positions,end positions) positions
my_list=[]

# Looping through
for keys in SID_keys:
    #store the value in word the keys values
    word=keywords[keys]
    # find the start and end positions of the word
    start_index = customer_reviews.find(word)
    # if keywords is not equal to -1 then add the start and end positions to the list
    if start_index != -1:
        end_index = start_index + len(word)
        my_list.append((start_index, end_index))
        
# print the list values
print("Positions are:",my_list)

##########################################################################################################################################################

# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:10

# Placeholder functions for metrics
def gross_profit_margin(revenue, cost_of_goods_sold):
    return (revenue - cost_of_goods_sold) / revenue * 100

def inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory

def customer_retention_rate(customers_at_start, customers_at_end):
    return (customers_at_end - customers_at_start) / customers_at_start * 100

def break_even_analysis(fixed_costs, price_per_unit, variable_cost_per_unit):
    return fixed_costs / (price_per_unit - variable_cost_per_unit)

# Example calls to the functions
# gross_profit_margin(1000, 400)  # Example values
# inventory_turnover(800, 200)     # Example values
# customer_retention_rate(100, 80) # Example values
# break_even_analysis(1000, 50, 30) # Example values
# print(gross_profit_margin(74, 10))
# print(inventory_turnover(740, 100))
# print(customer_retention_rate(740, 10))
# print(break_even_analysis(7401, 10, 10))


##########################################################################################################################################################

# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here

import numpy as np
print(np.__version__)
import pandas as pd
from sklearn.linear_model import LinearRegression

# Data preparation
data = {
    'Delivery Cost': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    'Shipment Volume': [500, 480, 450, 420, 400, 370, 340, 310, 290, 250]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Reshape the data
X = df['Delivery Cost'].values.reshape(-1, 1)  # Features
y = df['Shipment Volume'].values  # Target variable

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict shipment volume for a cost of £68
predicted_volume = model.predict(np.array([[68]]))

# Output results
print(f"Predicted shipment volume at £68: {predicted_volume[0]}")

##########################################################################################################################################################

# Question 4 - Debugging and Data Visualization

import rand as random
import matplotlib.pyplt as plt
import rand as random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student ID number
# your_ID=input("Enter your Student ID: ")
# max_value = int(your_ID)
# random_numbers = [random.randint(your_ID, max_valu) in range(100)]

# Corrected line
your_ID=740100109
max_value = int(740100109)
random_numbers = [random.randint(1, max_value) for _ in range(100)]  

# Plotting the numbers in a histogram
plt.plot(random_numbers, marker='o', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title("Histogram of 100 Random Numbers")
plt.xlabel("Value Range")
plt.ylabel("Value Range")
plt.grid(True)
plt.show()  
