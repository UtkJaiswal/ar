#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os

# Change to the directory containing this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Create HTTPS server
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

# Create server
with socketserver.TCPServer(("", 8443), http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("HTTPS server running on https://localhost:8443")
    print("For iPhone access, use your computer's IP address instead of localhost")
    print("Example: https://192.168.68.111:8443")
    httpd.serve_forever() 