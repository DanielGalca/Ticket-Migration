from base64 import b64encode
from operator import itemgetter
import ast #IS THIS NEEDED?
import sys #AND THIS?
import json
from telnetlib import AUTHENTICATION ##AAAA WHAT'S THIS AND WHY DID IT SUDDENLY APPEAR HERE
import requests
import configparser

config = configparser.RawConfigParser()
config.read('./src/auth.ini')
EXPORT_FILE = config['default']['Import'].strip('"')
DOMAIN = config['zendesk']['Domain'].strip('"')
AUTH = config['zendesk']['Credentials'].strip('"')

def main(args):
    ''' main function '''
# d = json.JSONDecoder()

with open(EXPORT_FILE, 'r') as jsonFile:
    jList = [json.loads(line)
            for line in jsonFile.readlines()]

print("The number of items in this JSON is: " + str(len(jList)))

ticket_data = {"tickets" : []}

for item in range(len(jList)):

    commentlist = []

    for comment in jList[item]['comments']:
        
        commentlist.append({'created_at' : comment['created_at'], ###### TO CHECK IF THIS SORTS COMMENTS IN ZENDESK
                            #'id' : comment['id'],
                            #'author_id' : comment['author_id'], 
                            'body' :comment['body']})
    
    single_ticket_data = {'assignee' : jList[item]['assignee'],
                          'tags' : jList[item]['tags'],
                          'subject' : jList[item]['subject'],
                          'submitter' : {#'id' : jList[item]['submitter']['id'], 
                                         #'name' : jList[item]['submitter']['name'], 
                                         'email' : jList[item]['submitter']['email']},
                          'comments' : commentlist}
    
    ticket_data['tickets'].append(single_ticket_data)
    
# with open('/Users/dgalca/Documents/GitHub/Ticket-Migration/src/test.json', 'w') as outfile:
#         print(type(outfile))
#         json.dump(ticket_data, outfile) #### TO TEST IF THE CODE WRITES TO JSON, DELETE L8R

def create_tickets(AUTH, DOMAIN):
  print(b64encode(AUTH.encode('utf-8'))[2:-1])
  header = {"Authorization": "Basic {}".format(str(b64encode(AUTH.encode('utf-8')))[2:-1])}
  url = f"https://{DOMAIN}.zendesk.com/api/v2/imports/tickets/create_many.json"

  try:
    result = requests.post(url, data=json.dumps(ticket_data), headers=header)
    print(result)
    
    if result.status_code != 201:
        print('Status:', result.status_code, 'Problem with the request. Exiting.')
        print(result.text)
        exit()
    else:
        print('n   i   c   e')
        return result
  except Exception as err: 
    print('Error making zendesk POST request:', str(err))
    exit()


create_tickets(AUTH, DOMAIN)


    
        
        # TODO: Take the info pulled from above and make a request to create new tickets with it. (Using Zen API; Create Many maybe;)



#if __name__ == "__main__":
 #  main(sys.argv)
