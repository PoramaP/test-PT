import tkinter as tk
import csv
import numpy as np
import matplotlib.pyplot as plt
dateStart = input()
dateEnd = input()
rateCount = int(input())
def makeTitle(rate):
    title = []
    title.append(str(rate))
    #titlestr = 
    #return titlestr
def drawModel(xs,ys,r):
    #make title a list of string that append a new rate when the function is run for each new rate
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.plot(xs,ys,"r-")
def extractData(rate):
    with open("Cleaned Interest Rates.csv","r") as file:
        content = csv.DictReader(file)
        global dateArray,rateArray
        count = 0
        rateArray = np.array([])
        dateArray = np.array([])
        for row in content: 
            #Todo: start work on matplotlib and changing arrays to fit with it if needed --> .key .value?
            #change the code to extract the data into a function extract rate with method rx
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
        drawModel(dateArray,rateArray,rate)
i = 0
while i < rateCount:
    rate = str(input())
    print(rate)
    makeTitle(rate)
    extractData(rate)
    i += 1          
plt.show()
plt.close()
print(dateArray)
print(rateArray)