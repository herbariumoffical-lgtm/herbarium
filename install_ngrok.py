import urllib.request
import zipfile
import os

url = "https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip"
zip_path = "ngrok.zip"
extract_path = "."

print(f"Downloading ngrok from {url}...")
try:
    urllib.request.urlretrieve(url, zip_path)
    print("Download complete.")

    print(f"Extracting to {extract_path}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    print("Extraction complete.")

    if os.path.exists("ngrok.exe"):
        print("ngrok.exe is ready!")
    else:
        print("Error: ngrok.exe not found after extraction.")

    # Cleanup zip
    os.remove(zip_path)

except Exception as e:
    print(f"An error occurred: {e}")
