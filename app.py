from flask import Flask
import twilio.twiml
app = Flask(__name__)
import requests


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
    #resp = twilio.twiml.Response()
    #resp.message("Hello, Mobile Monkey")

    cat_url = requests.get("http://thecatapi.com/api/images/get?format=src&type=gif")
    resp = '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>Meow</Body><Media>%s</Media></Message></Response>' % (cat_url.url)
    return str(resp)


@app.route("/call", methods=['GET', 'POST'])
def answer_call():

    resp = '<?xml version="1.0" encoding="UTF-8"?><Response><Say voice="woman">Hello! How are you?</Say></Response>'
    return str(resp)
"""
if __name__ == "__main__":
    app.run(debug=True)
"""