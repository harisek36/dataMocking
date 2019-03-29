
import urllib2
import random
import json
import csv

import datetime
import radar

recordValue = [i for i in range(119)] 

with open("mockData.csv", "a") as fp: 
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(recordValue)
