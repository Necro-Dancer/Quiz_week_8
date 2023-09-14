import matplotlib.pyplot as plt
import pandas as pd

database = pd.read_csv("./climate.csv")

years = []
co2 = []
temp = []

yData = database["Year"]
cData = database["CO2"]
tData= database["Temperature"]

for x in yData:
    years.append(x)
for x in cData:
    co2.append(x)
for x in tData:
    temp.append(x)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

