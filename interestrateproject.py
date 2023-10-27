import tkinter as tk
import csv
import numpy as np
import matplotlib
dateStart = input()
dateEnd = input()
rate = str(input())
with open("Cleaned Interest Rates.csv","r") as file:
    content = csv.DictReader(file)
    count = 0
    rateArray = np.array([])
    dateArray = np.array([])
    for row in content: 
        #Todo: start work on matplotlib and changing arrays to fit with it if needed
        if row["Date"] == dateStart:
            count = 1
        if count == 1:
            if row["Date"] == dateEnd:
                dateArray = np.append(dateArray,row["Date"])
                rateArray = np.append(rateArray,row[rate])
                break
            else:
                dateArray = np.append(dateArray, row["Date"])
                rateArray = np.append(rateArray,row[rate])
print(dateArray)
print(rateArray)

                
                
        
    


