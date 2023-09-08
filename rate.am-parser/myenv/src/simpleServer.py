from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class MyHandler(BaseHTTPRequestHandler):
    parsed_dom_object = ""  # Class attribute

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Important for CORS
        self.end_headers()
        self.wfile.write(self.parsed_dom_object.encode('utf-8'))

def run_server(my_string):
    MyHandler.parsed_dom_object = json.dumps(my_string)
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print('Server running on port 8000...')
    httpd.serve_forever()