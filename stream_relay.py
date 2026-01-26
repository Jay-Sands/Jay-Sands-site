#!/usr/bin/env python3
"""
ICY Stream Proxy - Handles Shoutcast/Icecast ICY protocol
"""

import http.server
import socketserver
import socket
import sys

INPUT_STREAM = "http://stream.abyss-shoutcast.com:4632"
LOCAL_PORT = 8000

class ICYStreamHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            # Parse the remote URL
            from urllib.parse import urlparse
            parsed = urlparse(INPUT_STREAM)
            
            # Connect to Shoutcast server with ICY headers
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((parsed.hostname, parsed.port or 80))
            
            # Send ICY request
            request = f"GET {parsed.path or '/'} HTTP/1.0\r\n"
            request += "Host: " + parsed.hostname + "\r\n"
            request += "Icy-MetaData: 0\r\n"
            request += "Connection: close\r\n"
            request += "User-Agent: Mozilla/5.0\r\n"
            request += "\r\n"
            
            sock.sendall(request.encode())
            
            # Read response headers
            response = b""
            while True:
                chunk = sock.recv(1)
                if not chunk:
                    break
                response += chunk
                if response.endswith(b"\r\n\r\n"):
                    break
            
            # Send HTTP 200 with proper audio headers
            self.send_response(200)
            self.send_header('Content-Type', 'audio/mpeg')
            self.send_header('Cache-Control', 'no-cache')
            self.send_header('Connection', 'close')
            self.end_headers()
            
            # Proxy the audio stream
            while True:
                chunk = sock.recv(8192)
                if not chunk:
                    break
                self.wfile.write(chunk)
            
            sock.close()
            
        except Exception as e:
            print(f"Error: {e}")
            self.send_error(500)
    
    def log_message(self, format, *args):
        print(f"[{args[0]}]")

if __name__ == '__main__':
    try:
        with socketserver.TCPServer(("0.0.0.0", LOCAL_PORT), ICYStreamHandler) as httpd:
            print(f"\n✓ ICY Stream proxy running at http://localhost:{LOCAL_PORT}")
            print(f"✓ Input stream: {INPUT_STREAM}")
            print(f"\nPress Ctrl+C to stop\n")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Proxy stopped")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
