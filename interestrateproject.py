import tkinter as tk
from tkinter import simpledialog, ttk
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

#MATPLOTLIB AND NUMPY, graphing and extracting data

def makeTitle(r):
    titlestr = " and ".join(map(str, r))
    return f"{titlestr}"

def drawModel(xs,ys,r,ra):
    plt.title(makeTitle(r))
    plt.subplots_adjust(bottom=0.2)
    plt.xlabel("Date")
    plt.ylabel("Rate")
    plt.xticks(rotation=30)
    if ra == "Policy Rate":
        plt.plot(xs,ys,"k-", label = "Policy Rate")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    elif ra == "New Loan Rates for Businesses":
        plt.plot(xs,ys,"b-", label = "New Loan Rates for Businesses")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    elif ra == "GSB Lending Rate":
        plt.plot(xs,ys,"tab:pink", label = "GSB Lending Rate")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    elif ra == "GHB Lending Rate":
        plt.plot(xs,ys,"tab:orange", label = "GHB Lending Rate")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    elif ra == "EXIM Lending Rate":
        plt.plot(xs,ys,"r-", label = "EXIM Lending Rate")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    elif ra == "SME Bank Lending Rate":
        plt.plot(xs,ys,"c-", label = "SME Bank Lending Rate")
        plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y"))
    plt.legend()

def extractData(rate):
    global dateArray,rateArray,ratelist
    with open("Cleaned Interest Rates.csv","r") as file:
        content = csv.DictReader(file)
        count = 0
        rateArray = np.array([])
        dateArray = np.array([])
        for row in content: 
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
        drawModel(dateArray,rateArray,ratelist,rate)

def openRateSelectionWindow(rc):
    rate_count = int(rc)
    rates = []
    totalratelist = ["Policy Rate", "New Loan Rates for Businesses", "GSB Lending Rate", "GHB Lending Rate",
                "EXIM Lending Rate", "SME Bank Lending Rate"]
    for i in range(rate_count):
        rate = simpledialog.askstring(f"Enter rate {i + 1}", f"Enter rate {i + 1}:")
        if rate is not None:
            if rate in totalratelist:
                rates.append(rate)
            else:
                errorlabel2.config(text="Invalid Interest Rate, the inputted value will not be added to the model")             
    
    return rates

#MAIN FUNCTIONS

def processInput():
    global dateStart, dateEnd, rateCount, main_frame, errorlabel
    try:
        dateStart = entryStart.get()
        datetime.datetime.strptime(dateStart, "%m/%d/%Y")
    except ValueError:
        errorlabel.config(text="Error: Invalid start date format. Please use the format 1/mm/yyyy.")
        return
    try:
        dateEnd = entryEnd.get()
        datetime.datetime.strptime(dateEnd, "%m/%d/%Y")
    except ValueError:
        errorlabel.config(text="Error: Invalid end date format. Please use the format 1/mm/yyyy.")
        return
    if dateStart > dateEnd:
        errorlabel.config(text = "Error: the starting date must come before the ending date")
        return
    try:
        rateCount = int(entryCount.get())
        if not (1 <= rateCount <= 6):
            raise ValueError("Invalid rate count. Please enter a number between 1 and 6.")
    except ValueError as e:
        errorlabel.config(text=f"Error: {str(e)}")
        return
    errorlabel.config(text="")
    main_frame.pack_forget()
    rate_selection_frame.pack()

def plotGraph():
    global dateStart, dateEnd, rateCount, dateArray, rateArray, ratelist, main_frame
    ratelist = openRateSelectionWindow(rateCount)
    plt.figure(figsize=(12, 6))
    for w in ratelist:
        extractData(w)
    rate_selection_frame.pack_forget()
    main_frame.pack()
    plt.show()
    plt.close()

#CODE FOR UI
root = tk.Tk()
root.title("Graph Interest Rates")
root.geometry("500x300")
root.resizable(height=False, width=False)
#MAINPAGE/FIRSTPAGE
main_frame = tk.Frame(root)
main_frame.pack()
labelDateStart = tk.Label(main_frame, text="Enter Start Date(1/mm/yyyy):")
labelDateEnd = tk.Label(main_frame, text="Enter End Date(1/mm/yyyy):")
labelRateCount = tk.Label(main_frame, text="Select Number of Rates(1 to 6):")
entryStart = tk.Entry(main_frame, width=20)
entryEnd = tk.Entry(main_frame, width=20)
entryCount = tk.Entry(main_frame, width=20)
errorlabel = tk.Label(main_frame, text="", fg="red")

errorlabel.grid(row=4, column=0, columnspan=2, pady=5)
labelDateStart.grid(row=0, column=0, padx=5, pady=5)
entryStart.grid(row=0, column=1, padx=5, pady=5)
labelDateEnd.grid(row=1, column=0, padx=5, pady=5)
entryEnd.grid(row=1, column=1, padx=5, pady=5)
labelRateCount.grid(row=2, column=0, padx=5, pady=5)
entryCount.grid(row=2, column=1, padx=0, pady=0)

beginButton = tk.Button(main_frame, text="Begin!", command=processInput)
beginButton.grid(row=3, column=0, columnspan=2, padx=5, pady=20)

#RATESELECTIONPAGE/SECONDPAGE + RATE SELECTION POP-UP

rate_selection_frame = tk.Frame(root)
plotButton = tk.Button(rate_selection_frame, text="Plot Graph", command=plotGraph)
plotButton.pack()

labelInstructions1 = tk.Label(rate_selection_frame,text = "The rates that are available in the dataset are the following:")
labelInstructions1["font"] = ["Arial",10,"bold"]
labelInstructions1.pack()

labelPR = tk.Label(rate_selection_frame,text = "1. Policy Rate")
labelPR.pack()
labelNB = tk.Label(rate_selection_frame, text = "2. New Loan Rates for Businesses")
labelNB.pack()
labelGSB = tk.Label(rate_selection_frame,text = "3. GSB Lending Rate")
labelGSB.pack()
labelGHB = tk.Label(rate_selection_frame,text = "4. GHB Lending Rate")
labelGHB.pack()
labelEXIM = tk.Label(rate_selection_frame,text = "5. EXIM Lending Rate")
labelEXIM.pack()
labelSME = tk.Label(rate_selection_frame, text = "6. SME Bank Lending Rate")
labelSME.pack()
errorlabel2 = tk.Label(rate_selection_frame, text="", fg="red")
errorlabel2.pack()
#BEGIN MAINLOOP

root.mainloop()