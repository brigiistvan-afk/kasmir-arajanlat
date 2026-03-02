#!/usr/bin/env python3
"""
Kasmir Árajánlat Generátor – Helyi Szerver
Futtatás: python szerver.py
Majd böngészőben: http://localhost:8765
"""
import http.server
import json
import urllib.request
import urllib.error
import os
import sys
import webbrowser
import threading
import time

PORT = 8765
API_KEY_FILE = "api_kulcs.txt"

class Handler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Csendes naplózás
        pass

    def send_cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, x-api-key, anthropic-version")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors()
        self.end_headers()

    def do_GET(self):
        # Főoldal: az arajanlat.html kiszolgálása
        path = self.path.split("?")[0]
        if path == "/" or path == "/index.html":
            fname = "arajanlat.html"
        else:
            fname = path.lstrip("/")

        if os.path.exists(fname):
            ext = fname.rsplit(".", 1)[-1].lower()
            ctypes = {"html": "text/html; charset=utf-8", "js": "application/javascript",
                      "css": "text/css", "png": "image/png", "jpg": "image/jpeg"}
            ctype = ctypes.get(ext, "application/octet-stream")
            with open(fname, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_cors()
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not found")

    def do_POST(self):
        if self.path == "/api/claude":
            # Anthropic API proxy
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)

            # API kulcs betöltése
            api_key = ""
            if os.path.exists(API_KEY_FILE):
                with open(API_KEY_FILE, "r") as f:
                    api_key = f.read().strip()

            if not api_key:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Hiányzó API kulcs. Írd be az api_kulcs.txt fájlba!"}).encode())
                return

            try:
                req = urllib.request.Request(
                    "https://api.anthropic.com/v1/messages",
                    data=body,
                    headers={
                        "Content-Type": "application/json",
                        "x-api-key": api_key,
                        "anthropic-version": "2023-06-01"
                    },
                    method="POST"
                )
                with urllib.request.urlopen(req, timeout=60) as resp:
                    result = resp.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(result)

            except urllib.error.HTTPError as ex:
                err_body = ex.read()
                self.send_response(ex.code)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(err_body)

            except Exception as ex:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.send_cors()
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(ex)}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def open_browser():
    time.sleep(1.2)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    # API kulcs ellenőrzés
    if not os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, "w") as f:
            f.write("")
        print(f"\n⚠️  Első indítás!")
        print(f"   Az '{API_KEY_FILE}' fájlba írd be az Anthropic API kulcsodat.")
        print(f"   (Az AI funkció ehhez szükséges — az árajánlat generálás API kulcs nélkül is megy.)\n")

    print(f"✦ Kasmir Árajánlat Generátor")
    print(f"  Szerver fut: http://localhost:{PORT}")
    print(f"  Leállítás: Ctrl+C\n")

    # Böngésző automatikus megnyitás
    t = threading.Thread(target=open_browser, daemon=True)
    t.start()

    server = http.server.HTTPServer(("localhost", PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Szerver leállítva.")
