import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from database import add_signup

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
if not account_sid or not auth_token:
    print("Cannot find Twilio auth creds")
    exit(1)

app = Flask(__name__)


@app.route("/")
def boo():
    return "👻"


@app.route("/sms", methods=["POST"])
def sms_reply():
    message = request.values.get("Body", None)
    from_phone_number = request.values.get("From", None)
    print(request.values)

    ok = add_signup(message, from_phone_number)
    if ok:
        print("successfully saved signup")
    else:
        print("signup save failed")

    resp = MessagingResponse()
    resp.message("😈 Excellent. We'll be in touch soon 🙌")
    return str(resp)


if __name__ == "__main__":
    app.run()
