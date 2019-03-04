from faker import Faker
import gender_guesser.detector as gender
from defaultValues import COL_A, COL_B, COL_C, COL_D, COL_E, COL_J, COL_K, COL_L, COL_M, COL_N, COL_P, COL_T, COL_X, COL_Y, COL_Z, COL_AA, COL_AB, COL_AC,COL_AD, COL_AE, COL_AF, COL_AG, COL_AH, COL_AJ, COL_AK

import urllib2
import random
import json
import csv

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

# for i in range(1, 15000):
#     first, last, address = personalDetails()

# print address


L_Seed = 1409607
M_Seed = 1000002



recordValue = []
recordReset = []


finalRecord = []

sirList = ['Mrs.', 'Dr.', 'Mr.']

for i in range(0,38):
    recordValue.append(' ')
    recordReset.append(' ')


with open("mockData_updated.csv", "a") as fp: 
    wr = csv.writer(fp, dialect='excel')

    for record in range(1,16000):
        recordValue[0] = COL_A #a
        recordValue[1] = random.choice(COL_B) #b
        recordValue[2] = random.choice(COL_C) #c
        recordValue[3] = random.choice(COL_D) #d
        recordValue[4] = random.choice(COL_E) #e

        recordValue[5] = recordValue[3] #f
        recordValue[6] = recordValue[4] #g
        recordValue[7] = recordValue[3] #h
        recordValue[8] = recordValue[4] #i

        recordValue[9] = COL_J #j ' '
        recordValue[10] = COL_K #k '26'

        recordValue[11] = L_Seed + random.randint(200000, 300000) #l
        L_Seed = recordValue[11]
        recordValue[12] = M_Seed + random.randint(3, 50) #m
        M_Seed = recordValue[12]

        initial, firstName, lastName, street, apt, city, state, zipcode, email= personalDetails()
        
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
        recordValue[24] = COL_Y #y
        recordValue[25] = COL_Z #z

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
        recordValue[36] = random.choice(COL_AK) #ak

        recordValue[37] = round(random.uniform(80.5,900.5), 2) #al

        wr.writerow(recordValue)

        recordValue = recordReset







