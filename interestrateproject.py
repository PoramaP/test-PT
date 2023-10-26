import tkinter as tk
import csv
import numpy
import matplotlib

dateRange = input()
rate = str(input())
with open("Cleaned Interest Rates.csv","r") as file:
    content = csv.DictReader(file)
    count = 0
    for row in content:
        if row["Date"] == dateRange:
            break
        print(row[rate])
        print(row["Date"])
        count += 1
    


