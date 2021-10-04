import json

bot_name = "Oliver"

def get_response(incoming_message):
	with open('intents.json', 'r') as file:
		intents = json.load(file)

	incoming_message = incoming_message.lower()
	msg = ''

	for intent in intents["intents"]:
		for pattern in intent["patterns"]:
			if pattern in incoming_message:
				msg = intent["response"]
				return msg
	
	msg = "Sorry, but I can't understand."
	return msg