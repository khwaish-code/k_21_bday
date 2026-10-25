
from flask import Flask, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(BASE_DIR, "birthday_site")


@app.route("/")
def home():
    return send_from_directory(SITE_DIR, "index.html")


@app.route("/photos/<path:filename>")
def photos(filename):
    return send_from_directory(
        os.path.join(SITE_DIR, "photos"),
        filename
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
