import tkinter as tk
import csv
import numpy
import matplotlib
dateStart = input()
dateEnd = input()
rate = str(input())
with open("Cleaned Interest Rates.csv","r") as file:
    content = csv.DictReader(file)
    count = 0
    for row in content: 
        #Todo: change the function from printing the rate and date to storing them in a numpy array
        if row["Date"] == dateStart:
            count = 1
        if count == 1:
            if row["Date"] == dateEnd:
                print(row[rate])
                print(row["Date"])
                break
            else:
                print(row[rate])
                print(row["Date"])
                
                
        
    


