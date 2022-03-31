import sys
import json

def main(args):
    ''' main function '''
d = json.JSONDecoder()
jsonFile = open('/pathto.json', 'r').read() #Get concatenated json in jsonFile
jList = []
while True:
   try:
      j,n = d.raw_decode(jsonFile) #decodes and separates different json files on from other
      jList.append(j) #Appends each line
   except ValueError: 
      break
   jsonFile=jsonFile[n:] #Drop into a string
   result_as_json = dict( items=jList )#From dict to a list baby.

    #print (data[0]['metric_set']['ticket_id']) #Show first tickets' 'ticket_id'
    #print(type(data[0]['submitter']['name'])) #Show the type of second dict
    #print(data[0]['submitter']['name']) #Tells us the name of submitter
    #print(data[0]['submitter']['email']) #Tells us email address of submitter
for item in range(len(jList)):
    print(type(jsonFile))#[item]['submitter'], ' - This is submitter data')
    ##print(jList[item]['tags'], '- These are the tags' )
    #print(jList[item]['comments'])
    #print(jList[item]['metric_set']['ticket_id'], ' - This is the ticket ID')
    #print(jList[item]['submitter']['id'], ' - This is the submitter ID')
    #print(jList[item]['submitter']['name'], ' - This is the submitter name')
    #print(jList[item]['submitter']['email'], ' - This is the submitter email address')
    #print(jList[item]['assignee'], ' - This is the Assignee data')
    # TODO: Take the info pulled from above and make a request to create new tickets with it. (Using Zen API; Create Many maybe;)


#if __name__ == "__main__":
 #  main(sys.argv)