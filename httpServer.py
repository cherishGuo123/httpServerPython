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
        self.wfile.write("--------Hello World !".encode())
        return
        
    def do_POST(self):
        #message = '\n'.join(['client_address=%s (%s)' % (self.client_address, self.address_string()).encode(),'command=%s' % self.command.encode(),'path=%s' % self.path.encode(), '',])
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_POST")
        time.sleep(5)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~ do_POST after sleep")
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("hello".encode())
        return

with socketserver.TCPServer(("", PORT), myHandler) as httpd:
    print("--------------------------Start", PORT)
    httpd.serve_forever()