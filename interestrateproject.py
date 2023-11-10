import tkinter as tk
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
dateStart = input()
dateEnd = input()
rateCount = int(input())
def makeTitle(r):
    titlestr = " and ".join(map(str, r))
    print(f"[{titlestr}]")
    return f"{titlestr}"
def drawModel(xs,ys,r):
    #make title a list of string that append a new rate when the function is run for each new rate
    plt.title(makeTitle(r))
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.xticks(rotation=45)
    plt.plot(xs,ys,"b-")
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
def extractData(rate):
    global dateArray,rateArray,titlelist
    with open("Cleaned Interest Rates.csv","r") as file:
        content = csv.DictReader(file)
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
                    dateArray = np.append(dateArray, datetime.datetime.strptime(row["Date"], "%m/%d/%Y"))
                    rateArray = np.append(rateArray,float(row[rate]))
                    break
                else:
                    dateArray = np.append(dateArray, datetime.datetime.strptime(row["Date"], "%m/%d/%Y"))
                    rateArray = np.append(rateArray,float(row[rate]))
        drawModel(dateArray,rateArray,titlelist)
titlelist = []
for i in range(rateCount):
    rate = (input())
    titlelist.append(rate)  
    print(rate)
    extractData(rate)        
plt.show()
plt.close()
print(dateArray)
print(rateArray)