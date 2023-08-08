import websocket
import json
ws = websocket.WebSocket()
ws.connect("wss://relay.snort.social")

relay_need = '"REQ"'
kind = '"kinds":[1]'
limit = '"limit":5'
subscription = '"ec3e6238-5ef3-4162-899c-a58825845a4c"'

request = '['+relay_need+', '+ subscription+', {'+ kind +', '+ limit + '}]'

while True:

    ws.send(request)
    event = ws.recv()
    event = event[50:]
    event_json = json.loads(event)
    print(event_json)

