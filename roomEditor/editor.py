import http.server
import socketserver
import os

PORT = 8000

os.chdir(os.path.dirname(__file__) + "/gui")
handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
