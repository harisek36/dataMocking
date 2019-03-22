from faker import Faker
import gender_guesser.detector as gender
from defaultValues import COL_A, COL_B, COL_C, COL_D, COL_E, COL_J, COL_K, COL_L, COL_M, COL_N, COL_P, COL_T, COL_X, COL_Y, COL_Z, COL_AA, COL_AB, COL_AC,COL_AD, COL_AE, COL_AF, COL_AG, COL_AH, COL_AJ, COL_AK, COL_AL, COL_BT, COL_BU,COL_BQ, COL_CF, COL_DG, COL_DK, COL_RANDOM

import urllib2
import random
import json
import csv

import datetime
import radar

# myKey = "mZzCruSLxfvbbmwVwj"
# data = json.load(urllib2.urlopen("https://gender-api.com/get?key=" + myKey + "&name=markus"))
# print "Gender: " + data["gender"]; #Gender: male

fake = Faker('en_US')
detectGender = gender.Detector()

nameSet = set()
addressSet = set()


def getStreetAndApt(streetWithApt):

    list_streetWithApt = streetWithApt.split(' ')

    apt = ' '
    street = streetWithApt

    if ('Apt.' in list_streetWithApt) or ('Suite' in list_streetWithApt) or ('Box' in list_streetWithApt):
        apt = list_streetWithApt[-2] + ' ' + list_streetWithApt[-1]
        list_streetWithApt = list_streetWithApt[:len(list_streetWithApt)-2]
        street  = ' '.join(list_streetWithApt)

    # print('Street: ' + street)
    # print('Apt: '+apt)
    return street, apt


def getCityStateZip(cityStateZip):
    cityStateZipcodeList = cityStateZip.split(' ')

    zipcode = cityStateZipcodeList[-1]
    state = cityStateZipcodeList[-2]

    cityStateZipcodeList = cityStateZipcodeList[:len(cityStateZipcodeList)-2]

    city = ' '.join(cityStateZipcodeList)
    city = city
        
    # print('city: ' + city)
    # print('state: '+ state)
    # print('zipcode: '+ zipcode)

    return city, state, zipcode


def personalDetails():

    found = False
    while(found != True):
        name = fake.name()
        address = fake.address()
        initial = ''
        print name
        # print address

        nameList = name.split(' ')

        if name not in nameSet and address not in address:
            continue

        firstName = nameList[0]
        lastName = nameList[1]

        if firstName in sirList:
            initial = nameList[0]
            firstName = nameList[1]
            lastName = nameList[2]

        
        email = firstName + '.' + lastName + '@example.org'
        streetWithApt, cityStateZip = address.split('\n')
            
        street, apt = getStreetAndApt(streetWithApt)
        city, state, zipcode = getCityStateZip(cityStateZip)
        
        break
    
    return initial, firstName, lastName, street, apt, city, state, zipcode, email


def dateFormat(date):
    year = str(date.year)
    month = str(date.month)
    day = str(date.day)
    
    if int(month) < 10:
        month = '0' + month
    if int(day) < 10:
        day = '0' + day

    return year + month + day
        


# for i in range(1, 15000):
#     first, last, address = personalDetails()

# print address


L_Seed = 1409607
M_Seed = 1000002

ssn_seed = COL_L

recordValue = [None] * 120
recordReset = [None] * 120


finalRecord = []

sirList = ['Mrs.', 'Dr.', 'Mr.']

# DOB Start date - End Date
startDobYear = 1970
endDobYear = 1973

contributionSum = 0
recordcount = 0

with open("mockData.csv", "a") as fileone: 
    hdr = csv.writer(fileone, dialect='excel')
    header = [None] * 10
    header[0] = 'SPARKH'
    header[1] = '04'
    header[2] = 'NYU LANGONE MEDICAL CENTER'
    header[3] = `startDobYear+45`+'0915-113500'
    header[4] = 'Sample 123-456-7890'
    header[5] = 'NYU LANGONE MEDICAL CENTER'
    header[6] = '2.0'
    header[7] = `startDobYear+45`+'0901'
 
    hdr.writerow(header)

with open("mockData.csv", "a") as fp: 
    wr = csv.writer(fp, dialect='excel')

    for record in range(1,100):
        recordcount = recordcount + 1
        recordValue[0] = COL_A #a

        institution_code = random.choice(COL_RANDOM)

        recordValue[1] = COL_B[institution_code] #b
        recordValue[2] = COL_C[institution_code] #c
        recordValue[3] = random.choice(COL_D) #d
        recordValue[4] = random.choice(COL_E) #e
        

        recordValue[5] = recordValue[3] #f
        recordValue[6] = recordValue[4] #g
        recordValue[7] = recordValue[3] #h
        recordValue[8] = recordValue[4] #i

        recordValue[9] = COL_J[0] #j ' ' ----- [0] 001 = 403(b)(1) 
        recordValue[10] = COL_K[3] #k '26' ------ [3] 12 monthly

    
        recordValue[11] =  ssn_seed #l
        recordValue[12] =  ssn_seed #m
        
        ssn_seed = ssn_seed + 1 

        initial, firstName, lastName, street, apt, city, state, zipcode, email = personalDetails()
        
        recordValue[13] = initial #n
        recordValue[14] = firstName #o
        recordValue[15] = COL_P #p
        recordValue[16] = lastName #q
        recordValue[17] = street #r
        recordValue[18] = apt #s
        recordValue[19] = COL_T #t
        recordValue[20] = city #u
        recordValue[21] = state #v
        recordValue[22] = zipcode #w
        recordValue[23] = COL_X #x
        recordValue[24] = COL_Y[0] #y Residency Code - U

        dob = radar.random_date(start = datetime.date(year=startDobYear, month=1, day=1),stop = datetime.date(year=endDobYear, month=12, day=30))
        
        recordValue[25] =  dateFormat(dob) #z

        recordValue[26] = random.choice(COL_AA) #aa
        recordValue[27] = random.choice(COL_AB) #ab
        recordValue[28] = COL_AC #ac
        recordValue[29] = COL_AD #ad
        recordValue[30] = COL_AE #ae
        recordValue[31] = COL_AF #af
        recordValue[32] = COL_AG #ag
        recordValue[33] = COL_AH #ah
        recordValue[34] = email #ai
        recordValue[35] = COL_AJ #aj
        # Employee Plan Remittance Data
        recordValue[36] = `startDobYear+45`+'09'+`15` #ak
        recordValue[37] = random.choice(COL_AL) # al
        contributionOne = round(random.uniform(80.5,900.5), 2)
        contributionSum = contributionSum + contributionOne
        recordValue[38] =  contributionOne #am
        yearOfHire = startDobYear+30
        originalDateOfHire  = radar.random_date(start = datetime.date(year=yearOfHire, month=1, day=1),stop = datetime.date(year=startDobYear+35, month=12, day=30))

        recordValue[66] = dateFormat(originalDateOfHire) # bm
        recordValue[67] = dateFormat(originalDateOfHire)# bn

        empStatus = random.choice(COL_BQ)
        empSubStatus = ''
        if(empStatus == 'E'):
            list_E = ['O', 'R']  
            empSubStatus = random.choice(list_E)
        if(empStatus == 'R'):
            list_E = ['N', 'E', 'P']  
            empSubStatus = random.choice(list_E)
        if(empStatus == 'T'):
            list_E = ['V', 'I']  
            empSubStatus = random.choice(list_E)
        if(empStatus == 'L'):
            list_E = ['A', 'U', 'F', 'M']  
            empSubStatus = random.choice(list_E)
        
        recordValue[68] = random.choice(COL_BQ) #bq
        recordValue[69] = empSubStatus #br
        recordValue[70] = recordValue[66] #bs
        recordValue[71] = random.choice(COL_BT) #bt
        recordValue[72] = COL_BU #bu

        currentDate = datetime.datetime.now()
        yearsOfService = currentDate.year - originalDateOfHire.year

        recordValue[73] = yearsOfService #bv
        recordValue[75] = round(random.uniform(50000.1,140000.9), 2) #bx

        recordValue[83] = random.choice(COL_CF)
        recordValue[110] = random.choice(COL_DG)

        recordValue[114] = random.choice(COL_DK)
        recordValue[118] = ''

        wr.writerow(recordValue)

        recordValue = recordReset

# Trailer row

with open("mockData.csv", "a") as fp: 
    wr = csv.writer(fp, dialect='excel')
    trailer= [None] * 5
    trailer[0] = 'SPARKTR'
    trailer[1] = recordcount + 2
    trailer[2] = round(contributionSum, 2)
    trailer[3] = ' '
    trailer[4] = ' '

    wr.writerow(trailer)





