import sys
import os
from time import sleep
from datetime import datetime
  
# append the path of the parent directory
sys.path.append("..")

from time import sleep
import modules.csvlog as csvlog

filename = 'log.csv'

csvlog.createLog(os.getcwd())

for count in range(20):
    csvlog.updateLog(count,count*2,count*3,count*4)
    sleep(0.5)