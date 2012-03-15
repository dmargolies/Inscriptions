#basic layout for this script, should be a loop, hd=000001 to ...?

from django.core.management import setup_environ
import settings
setup_environ(settings)

from get_data_helper import *
from getPageData import *
from inscriptions.models import *

def saveToDB(pageData): 
    #get all data maps/lists
    inscriptionMap = pageData.getInscriptionMap()
    personList = pageData.getPersonList()

    #inscription
    (inscription, wasCreated) = createInscription(inscriptionMap)
    if not wasCreated:
        print "inscription", inscription.hd_number, "already exists"

    #persons -- delete any existing persons first
    inscription.persons.all().delete()
    for personMap in personList:
        person = createPerson(personMap)
        person.save()
        inscription.persons.add(person)

for x in range(1, 65005):
    HD_Number = "%06d"% x
    pageData = Get_Data_From_Page(HD_Number)
    saveToDB(pageData)
