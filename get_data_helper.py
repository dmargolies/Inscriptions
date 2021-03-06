from django.core.management import setup_environ
import time
import settings
setup_environ(settings)

from inscriptions.models import *
from datetime import datetime #remove after testing ??

def toFloat(dub):
        if dub == None:
                return None
        elif dub=="":
                return None
        else:
            try:
                retVal = float(dub)
            except ValueError:
                retVal = None
                return retVal
def toInt(integ):
        if integ == None:
                return None
        elif integ =="":
                return None
        else:
            try:
                retVal = int(integ)
            except ValueError:
                retVal = None
            return retVal
                
def lookup(theKey, theMap):
        try:
            val = theMap[theKey]
        except KeyError:
            val = None
            print 'there was a key error with lookup of', theKey, 'in map', theMap
        return val

def createInscription(insMap):
    #Every Inscription must be unique, so we check if it exists (no duplicates allowed)
    (inscription, wasCreated) = Inscription.objects.get_or_create(
        hd_number = lookup("HD-Number", insMap),
        tm_number = lookup("TM-Number", insMap),
        province = lookup("Province", insMap),
        modern_country = lookup("Modern country", insMap),
        find_spot_ancient_name = lookup("Find Spot(ancient name)", insMap),
        find_spot_modern_name = lookup("Find Spot (modern name)", insMap),
        region = lookup("Region", insMap),
        year_of_find= toInt(lookup("Year of Find", insMap)),
        find_spot = lookup("Find Spot (street, etc.)", insMap),
        present_location = lookup("Present location", insMap),
        state_of_preservation = lookup("state of preservation", insMap),
        decoration = lookup("decoration", insMap),
        inscription_type = lookup("inscription-type", insMap),
        inscription_bearer = lookup("inscription bearer", insMap),
        field = lookup("fields", insMap),
        material = lookup("material", insMap),
        height= toFloat(lookup("height", insMap)),
        width= toFloat(lookup("width", insMap)),
        depth= toFloat(lookup("depth", insMap)),
        height_i_field= toFloat(lookup("height of inscribed field", insMap)),
        width_i_field= toFloat(lookup("width of inscribed field", insMap)),
        letters_size = lookup("letters size", insMap),
        ligature = lookup("ligature", insMap),
        meter = lookup("meter", insMap),
        language = lookup("language", insMap),
        date_day= lookup("date:day:", insMap),
        date_month= lookup("date:month:", insMap),
        date_year= lookup("date:year(terminus a quo)", insMap),
        date_specific= lookup("date:specific:", insMap),
        sel_history = lookup("social,economic, legal history", insMap),
        religion = lookup("religion", insMap),
        communal_groups = lookup("communal groups", insMap),
        geography = lookup("geography", insMap),
        political_communities = lookup("political communities", insMap),
        military = lookup("military", insMap),
        status_EDH_version = lookup("status of the EDH-version", insMap),
        responsible_individual = lookup("responsible individual", insMap),
        last_update= datetime.strptime(lookup("last update", insMap), '%Y-%m-%d'), #should work now
        palaeography_longa = lookup("palaeography: longa", insMap),
        palaeography_apica_ornata = lookup("palaeography: apice ornata", insMap),
        palaeography_parva = lookup("palaeography: parva", insMap),
        palaeography_inserta = lookup("palaeography: inserta", insMap),
        writing_type = lookup("writing type", insMap),
        punctuation = lookup("punctuation", insMap),
        comment = lookup("comment", insMap),
        #connections is just blank
        a_text = lookup("A-Text", insMap),
        b_text = lookup("B-Text", insMap),
        words = lookup("Alphabetical list of words in inscription", insMap))
    return (inscription, wasCreated)
    
def createPerson(personMap):
    #Create a brand new person, even if one with the same attributes already exists
    person= Person(
        name = lookup("name", personMap),
        praenomen = lookup("praenomen", personMap),
        nomen = lookup("nomen", personMap),
        cognoment = lookup("cognoment", personMap),
        supernomen = lookup("supernomen", personMap),
        filiation = lookup("filiation", personMap),
        tribus = lookup("tribus", personMap),
        origo = lookup("origo", personMap),
        other = lookup("other", personMap),
        gender = lookup("gender", personMap),
        relations = lookup("relations", personMap),
        status = lookup("status", personMap),
        official_positions = lookup("official positions", personMap),
        occupation = lookup("occupation", personMap),
        lifetime_years = toInt(lookup("lifetime:years:", personMap)),
        lifetime_months = toInt(lookup("lifetime:months:", personMap)),
        lifetime_hours = toInt(lookup("lifetime:hours:", personMap)))
    return person
    
class PageData:
    def __init__(self, insMap, persList):
        self.inscriptionMap = insMap
        self.personList = persList
        
    #getters
    def getPersonList(self):
        return self.personList
    def getInscriptionMap(self):
        return self.inscriptionMap
        
    #setters, not really necessary?  
    def setPersonList(self, persList):
        self.personList = persList
    def setInscriptionMap(self, insMap):
        self.inscriptionMap = insMap
