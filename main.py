from http.server import BaseHTTPRequestHandler, HTTPServer
import json

planets = [
    {
        "name": "Earth",
        "type": "Rocky planet",
        "distance": "149.6 million km"
    },
    {
        "name": "Mars",
        "type": "Rocky planet",
        "distance": "227.9 million km"
    },
    {
        "name": "Jupiter",
        "type": "Gas giant",
        "distance": "778.5 million km"
    }
]

class PlanetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/planets":
            response = json.dumps(planets, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_error(404, "Path not found")

server = HTTPServer(("127.0.0.1", 8000), PlanetHandler)

print("The server has been activated")
print("Open: http://127.0.0.1:8000/planets")

server.serve_forever()