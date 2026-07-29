from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import webbrowser

ROOT = Path(__file__).resolve().parent
PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt, *args):
        print(f"[{self.log_date_time_string()}] {fmt % args}")

server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
print(f"jol.kg test server: http://127.0.0.1:{PORT}/")
print(f"Admin panel: http://127.0.0.1:{PORT}/admin.html")
print("Press Ctrl+C to stop.")
try:
    webbrowser.open(f"http://127.0.0.1:{PORT}/")
except Exception:
    pass
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\\nServer stopped.")
finally:
    server.server_close()
