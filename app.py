import os
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from database import add_signup

account_sid = "AC509761f04f98b3836ab74182e554a3fc"
auth_token = "113855c9e67c1b103d20fa410f7e038e"

client = Client(account_sid, auth_token)
FROM = "+12018856050"
message = client.messages.create(body="Hello word", from_=FROM, to="+16238662766")

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
