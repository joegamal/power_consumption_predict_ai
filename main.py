import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def show(x):
    plt.plot(data[x], data['Energy Consumption'], marker='o', linestyle='-')

    # 3. Add details
    plt.title(f'Energy Consumption at {x}')
    plt.xlabel(x)
    plt.ylabel('Energy Consumption')

    # 4. Display or save
    plt.show()


data = pd.read_csv("./assignment1dataset.csv")

print(data.head())
##############################

#check nulls
print(data.isnull().sum())

print()
print()
##############################

#the min
print("min of all columns")
print()
print(data.min())

##############################
print()
print()
########################################################################

#the max
print("max of all columns")
print()
print(data.max())


#exploring the data

#show('Square Footage')
#show('Number of Occupants')
#show('Appliances Used')
#show('Average Temperature')
########################################################################


# we should split the data to train and test
x1_Square_Footage = data['Square Footage']
x2_Energy_Consumption = data['Energy Consumption']
x3_Appliances_Used = data['Appliances Used']
x4_Average_Temperature = data['Average Temperature']
y_Energy_Consumption = data['Energy Consumption']

#we have 1000 row
#we will split the data to train and test 30-> test 70-> train
x1_Square_Footage_train = x1_Square_Footage[:701]
x2_Energy_Consumption_train = x2_Energy_Consumption[:701]
x3_Appliances_Used_train = x3_Appliances_Used[:701]
x4_Average_Temperature_train = x4_Average_Temperature[:701]
y_Energy_Consumption_train = y_Energy_Consumption[:701]



x1_Square_Footage_test = x1_Square_Footage[701:]
x2_Energy_Consumption_test = x2_Energy_Consumption[701:]
x3_Appliances_Used_test = x3_Appliances_Used[701:]
x4_Average_Temperature_test = x4_Average_Temperature[701:]
y_Energy_Consumption_test = y_Energy_Consumption[701:]

#now we have test and train


#we should make a linear equation to each feature in the data


# formula 1 : y_Energy_Consumption_train = a * x1_Square_Footage_test + b
#to find the best a and best b we must apply gradient descent, cost function =  1/2n * sum(y- y')^2
# gradient descent


# formula 2 : y_Energy_Consumption_train = a * x2_Energy_Consumption_train + b
#the logic goes here


# formula 3 : y_Energy_Consumption_train = a * x3_Appliances_Used_train + b
#the logic goes here


# formula 4 : y_Energy_Consumption_train = a * x4_Average_Temperature_train + b
#the logic goes here














#  y =  a + o1x + o2x2 + o3x3 and so on






