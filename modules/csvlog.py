import csv
import os
from time import sleep
from datetime import datetime

logFile = ""

def createLog(filePath):
    headers = ['Time', 'Pit Temp (F)', 'Meat Temp (F)', 'Ambient Temp (F)', 'Ambient Humidity(%)'] 
    fileName = f'smokerLog_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    global logFile
    logFile = os.path.join(filePath,fileName)
    if __debug__:print(f'log file is: {logFile}')
    with open(logFile, 'w', encoding = 'UTF8', newline = '') as csvlog:
        csvlogger = csv.writer(csvlog)
        csvlogger.writerow(headers)

def updateLog(pitTemp,foodTemp,localTemp,localHumidity):
    with open(logFile, 'a', encoding = 'UTF8', newline = '') as csvlog:    
        csvlogger = csv.writer(csvlog)
        dateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        csvlogger.writerow([dateTime,pitTemp,foodTemp,localTemp,localHumidity])