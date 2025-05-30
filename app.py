from flask import Flask, request, render_template
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY", "fallbacksecret")

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
phone_number = os.environ["PHONE_NUMBER"]

@app.route('/', methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        code = request.form.get("code")
        client = TelegramClient(StringSession(), api_id, api_hash)
        client.connect()
        if not client.is_user_authorized():
            client.send_code_request(phone_number)
            client.sign_in(phone_number, code)
            session_str = client.session.save()
            with open("session/session.txt", "w") as f:
                f.write(session_str)
            return "✅ Session saved successfully!"
        return "Already authorized!"
    return render_template("verify.html")
