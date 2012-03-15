#imports
import urllib2
import urllib
from BeautifulSoup import BeautifulSoup

from get_data_helper import *

#065004 total files

positionAndValue = {2:"HD-Number", 5:"TM-Number", 8:"Province", 11:"Modern country",
                    14:"Find Spot(ancient name)", 17:"Find Spot (modern name)", 20:"Region",
                    23:"Year of Find", 26:"Find Spot (street, etc.)", 29:"Present location",
                    32:"state of preservation", 35:"decoration", 38:"inscription-type",
                    41:"inscription bearer", 44:"fields", 47:"material",
                    50:"height", 53:"width", 56:"depth",
                    59:"height of inscribed field", 62:"width of inscribed field", 65:"letters size",
                    68:"ligature", 71:"meter", 74:"language",
                    77:"date:day:", 80:"date:month:", 83:"date:year(terminus a quo)",
                    86:"date:specific:", 89:"social,economic, legal history", 92:"religion",
                    95:"communal groups", 98:"geography",
                    101:"political communities", 104:"military", 107:"status of the EDH-version",
                    110:"responsible individual", 113:"last update", 116:"palaeography: longa",
                    119:"palaeography: apice ornata", 122:"palaeography: parva", 125:"palaeography: inserta",
                    128:"writing type", 131:"punctuation"}
important_K_Number = {134:"literature"}
important_L_Number = {137:"comment"}
important_M_Number = {140:"connections"}
important_N_Numbers = {143:"person", 146:"name", 149:"praenomen", 152:"nomen",
                    155:"cognoment", 158:"supernomen", 161:"filiation", 164:"tribus", 167:"origo", 170:"other", 173:"gender",
                    176:"relations", 179: "status", 182:"official positions", 185:"occupation", 188:"lifetime:years:", 191:"lifetime:months:",
                    193:"lifetime:days:", 196:"lifetime:hours:"}
important_O_Number = {199:"A-Text"}
important_P_Number = {202:"B-Text"}
important_Q_Number = {205:"Alphabetical list of words in inscription"}

def encode(data):
        if data == None:
                return ""
        else:
                return data.encode("utf-8")
                
def Get_Data_From_Page(HD_Number):
    
    #inputs to the pageData obj
    inscriptionMap = {}
    #literatureList = []
    #commentList = []
    #connectionList = []
    personList = []
    #a_textList = []
    #b_textList = []
    
    #the heavy lifting
    
    #url setup, obviously need to fix this LOCALE!!
    url = "http://edh-www.adw.uni-heidelberg.de/EDH/inschrift/" + HD_Number
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 GTB7.1 (.NET CLR 3.5.30729)'
    values = {'language' : 'English' }
    headers2 = { 'User-Agent' : user_agent , 'Accept-Language' : 'en-us,en;q=0.5'}
    user_agent = ''
    data = urllib.urlencode(values)
    req = urllib2.Request(url, headers = headers2)
    page = urllib2.urlopen(req)
    
    #setup
    dataToFile= file("ins_folder/" + HD_Number + ".txt",'w')
    soup = BeautifulSoup(page)
    listofTDTags = (soup.findAll('td'))
    offset = 0
    importantNumbers = positionAndValue.keys()
    importantNumbers.sort()
    while listofTDTags[0].get("class") != "A":
        listofTDTags.pop(0)
        listofTDTags.pop(0)
        listofTDTags.pop(0)
        listofTDTags.pop(0)
        print "EFH-Foto(s) present in this file"
       
        
    #get the "inscription" part data
    for importantnumber in importantNumbers:
        data = listofTDTags[importantnumber + offset].getText()
        Description = positionAndValue[importantnumber]
        print importantnumber + offset
        print Description
        print data
        dataToFile.write(Description + ": " + encode(data) + "\n")
        #add the desc->data to the inscription map
        inscriptionMap[Description] = encode(data) 
        if listofTDTags[importantnumber + offset + 1].getText() == "&nbsp;":
            offset += 1
            
    #get the literature(s)
    data = listofTDTags[133 + offset]
    class_start = 133
    while data.get("class") != "L":
        litMap = {}
        for importantnumber in important_K_Number:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_K_Number[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            litMap[Description] = encode(data)
            print importantnumber + offset
            print Description
            print data
        offset += 3
        data = listofTDTags[class_start + offset] 
        #literatureList.append(litMap)
        
    #get the comment(s)
    class_start = 136
    offset = offset - 2
    data = listofTDTags[class_start + offset]
    while data.get("class") != "M":
        #comMap = {}
        for importantnumber in important_L_Number:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_L_Number[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            inscriptionMap[Description] = encode(data)
            print importantnumber + offset
            print important_L_Number[importantnumber]
            print data
        offset += 3
        data = listofTDTags[class_start + offset]
        #commentList.append(comMap)
        
    #get the connection(s)
    class_start = 139
    offset = offset - 2
    data = listofTDTags[class_start + offset]
    while data.get("class") != "N" and data.get("class") != "O":
        #conMap = {}
        for importantnumber in important_M_Number:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_M_Number[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            inscriptionMap[Description] = encode(data)
            print importantnumber + offset
            print important_M_Number[importantnumber]
            print data           
        offset += 3
        data = listofTDTags[class_start + offset]
        #connectionList.append(conMap)
    
    #get the person(s)
    class_start = 142
    offset = offset - 2
    data = listofTDTags[class_start + offset]
    important_Sorted_Numbers = important_N_Numbers.keys()
    important_Sorted_Numbers.sort()
    while data.get("class") != "O":
        personMap = {}
        for importantnumber in important_Sorted_Numbers:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_N_Numbers[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            personMap[Description] = encode(data)
            print importantnumber + offset
            print important_N_Numbers[importantnumber]
            print data
        offset += 58
        data = listofTDTags[class_start + offset]
        personList.append(personMap)
        
    #get the a-text(s)
    class_start = 198
    offset = offset - 56
    data = listofTDTags[class_start + offset]
    while data.get("class") != "P":
        #a_textMap = {}
        for importantnumber in important_O_Number:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_O_Number[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            inscriptionMap[Description] = encode(data)
            print importantnumber + offset
            print important_O_Number[importantnumber]
            print data
        offset += 3
        data = listofTDTags[class_start + offset]
        #a_textList.append(a_textMap)
        
    #get the b-text(s)
    class_start = 201
    offset = offset - 2
    data = listofTDTags[class_start + offset]
    while data.get("class") != "Q":
        #b_textMap = {}
        for importantnumber in important_P_Number:
            data = listofTDTags[importantnumber + offset].getText()
            Description = important_P_Number[importantnumber]
            dataToFile.write(Description + ": " + encode(data) + "\n")
            inscriptionMap[Description] = encode(data)
            print importantnumber + offset
            print important_P_Number[importantnumber]
            print data
        offset += 3
        data = listofTDTags[class_start + offset]
        #b_textList.append(b_textMap)
        
    #get the list of words
    class_start = 204
    offset = offset - 2
    data = listofTDTags[class_start + offset]
    for importantnumber in important_Q_Number: #THIS DOES NOT NEED TO BE A FOR LOOP --ONLY 1
        data = listofTDTags[importantnumber + offset].getText()
        Description = important_Q_Number[importantnumber]
        dataToFile.write(Description + ": " + encode(data) + "\n")
        inscriptionMap[Description] = encode(data)
        print importantnumber + offset
        print important_Q_Number[importantnumber]
        print data
        
    dataToFile.close()
    
     
    #after all the hard work, create and return the pageData object
    pageData = PageData(inscriptionMap, personList)
    return pageData
