import websocket
import json


#________________________________________________________________________________
# Future request for conact list 

#user_id = "e3aefda887252a72cee3578d33b2dcd90e9fe53b8bed6347ef5e26f74211adbb"

# ["REQ", "2669485454", {"kinds":[3], "authors":user_id}]

#________________________________________________________________________________

def open_socket(author):
    
    # Sockets Setup
    
    ws = websocket.WebSocket()
    ws.connect("wss://nos.lol")

    # Global Setup

    relay_req = '"REQ"'
    kind = '[1]'
    limit = 20
    subscription = '"6393049621547051"'
    post_author = '"authors":["' + author + '"]'
    

    request = '['+relay_req+', '+ subscription+', {"kinds":'+ kind +', "limit":'+ str(limit) + ', ' + post_author +'}]'


    ws.send(request)
    
    if ws.recv() != None:

        print("Here is the content of my last 10 notes:\n")

        i = 1
        n = 1

        while i <= 10:
            
            event = ws.recv()
                
            json_start = event.rfind('{')

            clean_event = event[json_start:]

            stripped_event = clean_event.rstrip(clean_event[-1])

            event_json = json.loads(stripped_event)

            print(n,event_json["content"],"\n")

            i += 1
            n += 1
    else:
        print("Nothing to get")
