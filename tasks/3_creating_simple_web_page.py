from temperature import Get_Temp

import socketpool
import wifi
import time

from adafruit_httpserver.mime_type import MIMEType
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.server import HTTPServer

import microcontroller


T_A = Get_Temp()

def myFunction():
    print("Labytis draugyti")

wifi.radio.connect("Galaxy A53 5G 974B", "ur mom gay")
time.sleep(1)
pool = socketpool.SocketPool(wifi.radio)
server = HTTPServer(pool)
def GimmeWebPage():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta http-equiv="Cache-Control" content="no-cache">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <title>Pico W HTTP Server</title>
    <h1>Pico W HTTP Server</h1>
    <p> {str(Get_Temp())} </p>
    <button onclick="window.location.href='http://192.168.234.107:80/cpu';">Go_To_Cpu_honey</button>

    <form>
    <input type="button" value="Hello">
    </form>

    </body></html>
    """
    return html
    
def GimmeWebPage2():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta http-equiv="Content-type" content="text/html;charset=utf-8">
    <meta http-equiv="Cache-Control" content="no-cache">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
    <title>Pico W HTTP Server</title>
    <h1>Pico W HTTP Server</h1>
    <p> CPU </p>
    <p> {str(microcontroller.cpu.temperature)} </p>
    <p> {str(microcontroller.cpu.frequency)} </p>
    <button onclick="window.location.href='http://192.168.234.107:80';">Go Back</button>
    
    </body></html>
    """
    return html
    

@server.route("/")
def base(request: HTTPRequest):
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{GimmeWebPage()}")
        
@server.route("/cpu")
def base(request: HTTPRequest):
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{GimmeWebPage2()}")
        


server.start(str(wifi.radio.ipv4_address))
print(f"Listening on http://{wifi.radio.ipv4_address}:80")



while True:
    #print(T_A)
    #print("My IP address is", wifi.radio.ipv4_address)
    #google_ip= ipaddress.ip_address("8.8.4.4")
    #print("Ping google.com: %f ms" % (wifi.radio.ping(google_ip)*1000))
    
    server.poll()
    time.sleep(1)
