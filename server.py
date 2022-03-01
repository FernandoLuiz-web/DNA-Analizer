import os

try:
    from http.server import SimpleHTTPRequestHandler as Handler
    from http.server import HTTPServer as Server
except ImportError as ex:
    print(f"Error name:{ex.name}")

HOST = 'localhost'
PORT = int(os.getenv('PORT', 8000))

os.chdir('static')

httpd = Server((HOST, PORT), Handler)
try:
    print(f"Server now running... {HOST}:{PORT}")
    print(f"Port: {PORT}")
    print(f"Host: {HOST}")
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()