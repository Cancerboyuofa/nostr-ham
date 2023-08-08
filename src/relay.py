import websocket
import json



if __name__ == "__main__":

    
    ws = websocket.WebSocket()
    ws.connect("wss://nos.lol")

    relay_req = '"REQ"'
    kind = '"kinds":[1]'
    limit = '"limit":10'
    subscription = '"6393049621547051"'
    author = '"authors":["e3aefda887252a72cee3578d33b2dcd90e9fe53b8bed6347ef5e26f74211adbb"]'


    request = '['+relay_req+', '+ subscription+', {'+ kind +', '+ limit + ', ' +author +'}]'

    i = 0

    print("Here is the content of my last 10 notes:\n")

    while i <= 10:
        
        ws.send(request)
        event = ws.recv()

        json_start = event.rfind('{')
  
        clean_event = event[json_start:]

        clean_event = clean_event.rstrip(clean_event[-1])

        event_json = json.loads(clean_event)

        print(event_json["content"],"\n")
 
        i = i + 1