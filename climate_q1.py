import matplotlib.pyplot as plt
import sqlite3

database = sqlite3.connect("./climate.db")
cursor = database.cursor()

years = []
co2 = []
temp = []

cursor.execute("SELECT * FROM ClimateData")
data = cursor.fetchall()

for x in data:
    years.append(x[0])
    co2.append(x[1])
    temp.append(x[2])

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
plt.savefig("co2_temp_1.png") 

database.close()
