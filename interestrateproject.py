import tkinter as tk
import csv
import numpy as np
import matplotlib.pyplot as plt
dateStart = input()
dateEnd = input()
rateCount = int(input())
with open("Cleaned Interest Rates.csv","r") as file:
    content = csv.DictReader(file)
    count = 0
    rateArray = np.array([])
    dateArray = np.array([])
    def drawModel(xs,ys):
        plt.xlabel("Date")
        plt.ylabel("Rate")
        plt.plot(xs,ys,"r-")
        rate = str(input())
    i = 0
    while i <= rateCount:
        rate = str(input())
        for row in content: 
            #Todo: start work on matplotlib and changing arrays to fit with it if needed --> .key .value?
            #need to fix the xticks 8/11/23
            #there is a seperate file where I am working on changing the data extraction to a function called extractData 8/11/23
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
            i += 1
        drawModel(dateArray,rateArray)
    plt.show()
    plt.close()
print(dateArray)
print(rateArray)

                
                
        
    


