from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # GET
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, GET request!')

    # POST
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, POST request! You sent: ' + post_data)

    # PUT
    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, PUT request! You sent: ' + put_data)

    # PATCH
    def do_PATCH(self):
        content_length = int(self.headers['Content-Length'])
        patch_data = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, PATCH request! You sent: ' + patch_data)

    # DELETE
    def do_DELETE(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, DELETE request!')

# main function
def main():
    host = 'localhost'
    port = 8000
    server_address = (host, port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('Server running on {}:{}'.format(host, port))
    httpd.serve_forever()

if __name__ == '__main__':
    main()
