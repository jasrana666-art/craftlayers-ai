from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import subprocess
import threading
import time

PORT = 8080
BASE_DIR = "C:/Users/Administrator/Projects/getlayers-autonomous"

class AutonomousHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/products":
            db_path = os.path.join(BASE_DIR, "data", "products.json")
            if os.path.exists(db_path):
                with open(db_path, "r", encoding="utf-8") as f:
                    data = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(data.encode("utf-8"))
                return
        elif self.path == "/api/trigger-autonomy":
            # Manually trigger autonomous product generation
            subprocess.run(["python", os.path.join(BASE_DIR, "autonomous_worker.py")])
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success", "message": "Autonomous product generated!"}).encode("utf-8"))
            return
        
        # Serve static files from base dir
        return super().do_GET()

def run_server():
    os.chdir(BASE_DIR)
    server = HTTPServer(("0.0.0.0", PORT), AutonomousHandler)
    print(f"Autonomous GetLayers server running at http://localhost:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    run_server()
