import http.server
import socketserver
from http.server import BaseHTTPRequestHandler
import time

PORT = 30000

class myHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_GET")
        time.sleep(5)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_GET after sleep")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("--------Hello World !")
        return
        
    def do_POST(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_POST")
        time.sleep(5)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_POST after sleep")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("--------Hello World !")
        return

with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    print("--------------------------Start", PORT)
    httpd.serve_forever()