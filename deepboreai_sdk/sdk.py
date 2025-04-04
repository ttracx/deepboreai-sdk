import requests
import websocket
import threading
import json

class DeepBoreAI:
    def __init__(self, host='http://localhost:8000'):
        self.host = host

    def post_telemetry(self, data: dict):
        url = f"{self.host}/ingest"
        response = requests.post(url, json=data)
        return response.json()

    def get_recent_alerts(self):
        url = f"{self.host}/history"
        response = requests.get(url)
        return response.json()

    def export_csv(self, out_path='drilling_data.csv'):
        url = f"{self.host}/export"
        r = requests.get(url)
        with open(out_path, 'wb') as f:
            f.write(r.content)
        return out_path

    def watch_live(self, callback):
        def on_message(ws, message):
            data = json.loads(message)
            callback(data)

        ws = websocket.WebSocketApp(f"{self.host.replace('http', 'ws')}/ws",
                                    on_message=on_message)
        thread = threading.Thread(target=ws.run_forever)
        thread.daemon = True
        thread.start()
        return ws