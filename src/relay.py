import websocket
import json

    

if __name__ == "__main__":

    
    # Sockets Setup
    
    ws = websocket.WebSocket()
    ws.connect("wss://nos.lol")

    # Global Setup

    relay_req = '"REQ"'
    kind = '[1]'
    limit = 20
    subscription = '"6393049621547051"'
    author = '"authors":["e3aefda887252a72cee3578d33b2dcd90e9fe53b8bed6347ef5e26f74211adbb"]'

    request = '['+relay_req+', '+ subscription+', {"kinds":'+ kind +', "limit":'+ str(limit) + ', ' +author +'}]'


    ws.send(request)
    

    print("Here is the content of my last 10 notes:\n")

    i = 0
    n = 0

    while i <= 10:
        
        event = ws.recv()

        json_start = event.rfind('{')
  
        clean_event = event[json_start:]

        stripped_event = clean_event.rstrip(clean_event[-1])

        event_json = json.loads(stripped_event)

        print(n,event_json["content"],"\n")
 
        i += 1
        n += 1