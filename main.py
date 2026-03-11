import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
##############################

#the max
print("max of all columns")
print()
print(data.max())


#exploring the data
plt.plot(data['Square Footage'], data['Energy Consumption'], marker='o', linestyle='-')

# 3. Add details
plt.title('Energy Consumption at Square Footage')
plt.xlabel('Square Footage')
plt.ylabel('Energy Consumption')
plt.grid()

# 4. Display or save
plt.show()


plt.plot(data['Number of Occupants'], data['Energy Consumption'], marker='o', linestyle='-')

# 3. Add details
plt.title('Energy Consumption at Square Footage')
plt.xlabel('Number of Occupants')
plt.ylabel('Energy Consumption')
plt.grid()

# 4. Display or save
plt.show()




plt.plot(data['Appliances Used'], data['Energy Consumption'], marker='o', linestyle='-')

# 3. Add details
plt.title('Energy Consumption at Square Footage')
plt.xlabel('Appliances Used')
plt.ylabel('Energy Consumption')
plt.grid()

# 4. Display or save
plt.show()



plt.plot(data['Average Temperature'], data['Energy Consumption'], marker='o', linestyle='-')

# 3. Add details
plt.title('Energy Consumption at Square Footage')
plt.xlabel('Average Temperature')
plt.ylabel('Energy Consumption')
plt.grid()

# 4. Display or save
plt.show()






