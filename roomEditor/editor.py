import http.server
import socketserver
import os

PORT = 8000

os.chdir(os.path.dirname(__file__) + "/gui")

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print("Serving static website at", PORT)
    httpd.serve_forever()
