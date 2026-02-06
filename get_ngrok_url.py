import time
import json
import urllib.request

def get_ngrok_url():
    # Wait a bit for ngrok to start
    time.sleep(2)
    try:
        with urllib.request.urlopen("http://127.0.0.1:4040/api/tunnels") as response:
            data = json.loads(response.read().decode())
            public_url = data['tunnels'][0]['public_url']
            print(f"NGROK_URL={public_url}")
    except Exception as e:
        print(f"Error getting URL: {e}")

if __name__ == "__main__":
    get_ngrok_url()
