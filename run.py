# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from datetime import date

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Your miles were successfully added.")

    body = request.values.get('Body', None)
    amount = body
    print(body)
    today = date.today()
    d3 = today.strftime("%m/%d/%y")
    url = "https://lesson-link-api.herokuapp.com/milage"
    if body == None:
        print("hi")

    else:
        myobj = {"date": d3, "amount": amount}

        x = requests.post(url, data = myobj)

    return str(resp) 

if __name__ == "__main__":
    app.run(debug=True)