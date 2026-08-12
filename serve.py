#!/usr/bin/env python3
"""
HH Goa 2026 — Builder ID Local Dev Server
==========================================
Serves the app on http://0.0.0.0:8000 and routes all /share/* paths
to code.html so the JS client-side router can handle them.

Usage:
    python serve.py            # default port 8000
    python serve.py 9000       # custom port

Access from phone on same LAN:
    http://<YOUR-LAN-IP>:8000
"""

import os
import sys
import socketserver
import json
import threading
import urllib.request
import http.server

# ── Resolve the workspace directory (where this script lives) ──────────────────
WORKSPACE_ROOT = os.path.dirname(os.path.abspath(__file__))

SimpleHTTPRequestHandler = http.server.SimpleHTTPRequestHandler


# ── Builder Storage & Cloud Sync ────────────────────────────────────────────────
BUILDERS_CACHE_FILE = os.path.join(WORKSPACE_ROOT, 'builders_cache.json')
BUILDERS_DB = {}

def load_builders_cache():
    global BUILDERS_DB
    if os.path.exists(BUILDERS_CACHE_FILE):
        try:
            with open(BUILDERS_CACHE_FILE, 'r', encoding='utf-8') as f:
                BUILDERS_DB = json.load(f)
        except Exception:
            BUILDERS_DB = {}

def save_builders_cache():
    try:
        with open(BUILDERS_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(BUILDERS_DB, f, indent=2)
    except Exception as e:
        print(f"Error saving cache: {e}")

load_builders_cache()

def sync_builder_to_cloud(builder_id, payload):
    try:
        blob_url = 'https://jsonblob.com/api/jsonBlob'
        data_bytes = json.dumps(payload).encode('utf-8')
        req = urllib.request.Request(blob_url, data=data_bytes, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, method='POST')
        with urllib.request.urlopen(req, timeout=5) as resp:
            blob_id = resp.headers.get('X-jsonblob-id')
            if not blob_id and resp.headers.get('Location'):
                blob_id = resp.headers.get('Location').split('/')[-1]
            
            if blob_id:
                app_key = os.environ.get("API_KEY", "9ogy9ct9")
                kv_url = f'https://keyvalue.immanuel.co/api/KeyVal/UpdateValue/{app_key}/{builder_id}/{blob_id}'
                req_kv = urllib.request.Request(kv_url, data=b'', method='POST')
                with urllib.request.urlopen(req_kv, timeout=5) as kv_resp:
                    print(f"  \033[32m[Cloud Sync] Synced {builder_id} -> blob {blob_id}\033[0m")
    except Exception as e:
        print(f"  \033[33m[Cloud Sync Warning] {builder_id}: {e}\033[0m")

def fetch_builder_from_cloud(builder_id):
    try:
        app_key = os.environ.get("API_KEY", "9ogy9ct9")
        kv_url = f'https://keyvalue.immanuel.co/api/KeyVal/GetValue/{app_key}/{builder_id}'
        req_kv = urllib.request.Request(kv_url, method='GET')
        with urllib.request.urlopen(req_kv, timeout=5) as resp:
            raw_blob_id = resp.read().decode('utf-8').strip().strip('"')
            if raw_blob_id and raw_blob_id != 'null' and len(raw_blob_id) > 5:
                blob_url = f'https://jsonblob.com/api/jsonBlob/{raw_blob_id}'
                req_blob = urllib.request.Request(blob_url, method='GET')
                with urllib.request.urlopen(req_blob, timeout=5) as b_resp:
                    return json.loads(b_resp.read().decode('utf-8'))
    except Exception as e:
        print(f"  \033[33m[Cloud Fetch Warning] {builder_id}: {e}\033[0m")
    return None


# ── Custom handler: rewrite /share/* → /code.html & handle /api/builder/* ──────
class ShareRouteHandler(SimpleHTTPRequestHandler):
    """Serve code.html for any /share/<builderId> path so the JS router works, and handle builder persistence API."""

    def translate_path(self, path):
        # Strip query params and hash fragments to get clean path
        clean = self.path.split('?')[0].split('#')[0]
        parts = clean.split('/')

        # Root / → serve code.html (app entry point)
        if clean == '' or clean == '/':
            path = '/code.html'

        # /share/<anything> → serve code.html (JS client-side router handles it)
        elif len(parts) >= 3 and parts[1] == 'share':
            path = '/code.html'

        return super().translate_path(path)

    def do_GET(self):
        clean = self.path.split('?')[0].split('#')[0]
        
        if clean == '/health':
            resp_bytes = json.dumps({'status': 'ok'}).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Content-Length', str(len(resp_bytes)))
            self.end_headers()
            self.wfile.write(resp_bytes)
            return

        parts = clean.split('/')
        if len(parts) >= 4 and parts[1] == 'api' and parts[2] == 'builder':
            builder_id = parts[3]
            data = BUILDERS_DB.get(builder_id)
            if not data:
                data = fetch_builder_from_cloud(builder_id)
                if data:
                    BUILDERS_DB[builder_id] = data
                    save_builders_cache()

            if data:
                resp_bytes = json.dumps(data).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(resp_bytes)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp_bytes)
            else:
                resp_bytes = json.dumps({'error': 'not_found'}).encode('utf-8')
                self.send_response(404)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(resp_bytes)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp_bytes)
            return

        return super().do_GET()

    def do_POST(self):
        clean = self.path.split('?')[0].split('#')[0]
        parts = clean.split('/')
        if len(parts) >= 4 and parts[1] == 'api' and parts[2] == 'builder':
            builder_id = parts[3]
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length) if content_length > 0 else b'{}'
                payload = json.loads(body.decode('utf-8'))
                BUILDERS_DB[builder_id] = payload
                save_builders_cache()

                threading.Thread(target=sync_builder_to_cloud, args=(builder_id, payload), daemon=True).start()

                resp_bytes = json.dumps({'success': True}).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(resp_bytes)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp_bytes)
            except Exception as e:
                print(f"  \033[31m[API POST Error] {e}\033[0m")
                resp_bytes = json.dumps({'error': str(e)}).encode('utf-8')
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', str(len(resp_bytes)))
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(resp_bytes)
            return

        return super().do_POST()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def log_message(self, fmt, *args):
        # Coloured output for readability
        status = args[1] if len(args) > 1 else ''
        color = '\033[32m' if str(status).startswith('2') else (
                '\033[33m' if str(status).startswith('3') else '\033[31m')
        reset = '\033[0m'
        print(f"  {color}{fmt % args}{reset}")


# ── Entry point ────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    port = int(os.environ.get("PORT", sys.argv[1] if len(sys.argv) > 1 else 8000))
    bind = '0.0.0.0'

    # Change to workspace root so files are served from the correct directory
    os.chdir(WORKSPACE_ROOT)

    # Allow rapid restart (reuse address) & handle concurrent requests concurrently
    class ReuseTCPServer(socketserver.ThreadingTCPServer):
        allow_reuse_address = True

    with ReuseTCPServer((bind, port), ShareRouteHandler) as httpd:
        import socket
        # Find best LAN IP to show the user
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            lan_ip = s.getsockname()[0]
            s.close()
        except Exception:
            lan_ip = '127.0.0.1'

        print()
        print('  +--------------------------------------------------+')
        print('  |  HH GOA 2026 -- Builder ID Dev Server            |')
        print('  +--------------------------------------------------+')
        print(f'  |  Local:   http://localhost:{port}' + ' ' * max(0, 21 - len(str(port))) + '|')
        print(f'  |  Network: http://{lan_ip}:{port}' + ' ' * max(0, 12 - len(lan_ip) - len(str(port))) + '|')
        print('  |                                                  |')
        print('  |  Share routes handled: /share/<builderId>        |')
        print('  +--------------------------------------------------+')
        print()

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\n\n  Server stopped.\n')
