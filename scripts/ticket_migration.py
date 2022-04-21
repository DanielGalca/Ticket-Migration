from base64 import b64encode
from operator import itemgetter
import ast
import sys
import json
import requests
import configparser


def main(args):
    ''' main function '''
# d = json.JSONDecoder()

file = open('/Users/dgalca/Documents/GitHub/Ticket-Migration/src/testest.json', "r")
data = file.read().replace("}{","},{")
data = "["+data+"]"
test = ast.literal_eval(data)
# test=ast.literal_eval(str(map(str,data.split(','))))
print(test, type(test))
exit()

# jsonFile = open('/Users/dgalca/Documents/GitHub/Ticket-Migration/src/testest.json', 'r').read() #Get concatenated json in jsonFile
jList = []
n = 0
while len(jsonFile) > n:
   try:
      print(len(jsonFile), n)
      j,k = d.raw_decode(jsonFile) #decodes and separates different json files one from other
      n += k
      jList.append(j) #Appends each line
    #   print(j)
    #   print(type(j))
    #   print(n)
    #   print(type(n))
   except Exception as err:      
      print('Error:', err)
   jsonFile=jsonFile[k:] #Drop into a string
# result_as_json = dict( items=jList )#From dict to a list baby.

print(len(jList))
ticket_data = {"tickets" : []}

for item in range(len(jList)):

    testestest = {'tags' : jList[item]['tags']}
    ticket_data['tickets'].append(testestest)

    # commentlist = []

    # for comment in jList[item]['comments']:
    #     commentlist.append({'created_at' : comment['created_at'], ###### TO CHECK IF THIS SORTS COMMENTS IN ZENDESK
    #                         'id' : comment['id'],
    #                         'author_id' : comment['author_id'], 
    #                         'body' :comment['body']})
    #     # commentlist = sorted(commentlist, key=itemgetter(0))
    
    # single_ticket_data = {'tags' : jList[item]['tags'], 
    #                'subject' : jList[item]['subject'],
    #                'submitter' : {'id' : jList[item]['submitter']['id'], 
    #                               'name' : jList[item]['submitter']['name'], 
    #                               'email' : jList[item]['submitter']['email']},
    #                'comments' : commentlist}
    
    # ticket_data['tickets'].append(single_ticket_data)
    
with open('/Users/dgalca/Documents/GitHub/Ticket-Migration/src/test.json', 'w') as outfile:
        json.dump(ticket_data, outfile) #### TO TEST IF THE CODE WRITES TO JSON, DELETE L8R

# def create_tickets(dom, auth):
#   print(b64encode(auth.encode('utf-8'))[2:-1])
#   header = {"Authorization": "Basic {}".format(str(b64encode(auth.encode('utf-8')))[2:-1])}
#   url = f"https://{dom}.zendesk.com/api/v2/tickets/create_many"

#   try:
#     result = requests.post(url, data=json.dumps(ticket_data), headers=header)
#     return result
#   except Exception as err: 
#     print('Error making zendesk POST request:', str(err))
#     exit()

    
        
        # TODO: Take the info pulled from above and make a request to create new tickets with it. (Using Zen API; Create Many maybe;)



#if __name__ == "__main__":
 #  main(sys.argv)