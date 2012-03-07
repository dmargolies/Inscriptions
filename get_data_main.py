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
    literatureList = pageData.getLiteratureList()
    commentList = pageData.getCommentList()
    connectionList = pageData.getConnectionList()
    personList = pageData.getPersonList()
    a_textList = pageData.getA_textList()
    b_textList = pageData.getB_textList()

    #inscription
    
    (inscription, wasCreated) = createInscription(inscriptionMap)
    if not wasCreated:
        print "inscription", inscription.hd_number, "already exists"

    #add in all the other data
    
    #literature(s)
    for literatureMap in literatureList:
        (literature, wasCreated) = createLiterature(literatureMap)
        inscription.literatures.add(literature)

    for commentMap in commentList:
        (comment,wasCreated) = createComment(commentMap)
        inscription.comments.add(comment)
    
    for connectionMap in connectionList:
        (connection, wasCreated) = createConnection(connectionMap)
        inscription.connections.add(connection)

    for personMap in personList:
        (person, wasCreated) = createPerson(personMap)
        inscription.persons.add(person)

    for a_textMap in a_textList:
        (a_text, wasCreated) = createA_text(a_textMap)
        inscription.a_texts.add(a_text)

    for b_textMap in b_textList:
        (b_text, wasCreated) = createB_text(b_textMap)
        inscription.b_texts.add(b_text)

for x in range(1, 65005):
    HD_Number = "%06d"% x
    pageData = Get_Data_From_Page(HD_Number)
    saveToDB(pageData)
