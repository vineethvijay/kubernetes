#!/usr/bin/python
import socket
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8000
counter = 0

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        global counter
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        counter += 0.5
        # Send the html message
        self.wfile.write("Hello %d from  %s" % (counter,socket.gethostname()))
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ' , PORT_NUMBER

    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
