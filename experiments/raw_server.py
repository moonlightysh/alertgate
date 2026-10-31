from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class WebhookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/webhook":
            self.send_error(404, "Not Found")
            return
        length_header = self.headers.get("Content-Length")
        if length_header is None:
            self.send_error(411, "Length Required")
            return
        try:
            length = int(length_header)
        except ValueError:
            self.send_error(400, "Bad Content-Length")
            return
        raw = self.rfile.read(length)
        print("--- raw headers ---")
        for key, value in self.headers.items():
            print(f"{key}: {value}")
        print("--- raw body ---")
        print(raw)
        try:
            payload = json.loads(raw)
        except ValueError:
            self.send_error(400, "Invalid JSON")
            return
        print("-- parser result ---")
        print(payload)

        body = b'{"accepted": 1}'
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8080), WebhookHandler)
    print("Listening on http://127.0.0.1:8080")
    server.serve_forever()