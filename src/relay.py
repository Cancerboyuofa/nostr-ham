import websocket
import json
ws = websocket.WebSocket()
ws.connect("wss://relay.snort.social")

relay_need = '"REQ"'
kind = '"kind":[0,2]'
limit = '"limit":20'
subscription = '"ec3e6238-5ef3-4162-899c-a58e82586a4b"'

request = '['+relay_need+', '+ subscription+', {'+ kind +', '+ limit + '}]'

while True:

    ws.send(request)
    print(ws.recv())


