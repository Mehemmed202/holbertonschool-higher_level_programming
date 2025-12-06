#!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# requestleri idare eden class
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write("Hello, this is a simple API")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_header()
            self.wfile.write("OK")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_header()
            self.wfile.write("Endpoint not found")

# serverin qurulmasi ve ise salinmasi
if __name__ == "__main__":
    port = 8000
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHandler)
    print(f"serving on port {port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        httpd.server_close()
        print("Server successfully shut down.")
