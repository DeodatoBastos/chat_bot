from flask import Flask, request
import json
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def get_response(incoming_message):
	with open('intents.json', 'r') as file:
		intents = json.load(file)

	msg = ''

	for intent in intents["intents"]:
		for pattern in intent["patterns"]:
			if pattern in incoming_message:
				msg = intent["response"]
	
	return msg

def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	body = get_response(incoming_msg)

	if body == '':
		msg.body('Sorry, I don\'t understand!')
	else:
		msg.body(body)

	return str(resp)

if __name__ == '__main__':
	app.run()
