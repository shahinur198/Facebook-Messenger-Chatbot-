from flask import Flask, request
import json
from bot import Bot

PAGE_ACCESS_TOKEN = 'EAAjpHJXWzoMBAMkH6ZBqC9U4C9ZBc0ebbimEvZBjPQaVkxYgNPeWmSgzub1K12SQlrJS5fDFiq9iOdwyTsODzvGTXTdPLm3ZBLNFgb7tx8ByiZBRp8N3UZAHSpV9UlbDPZByJu6vkpCZBCxvOoWiIfkPI5sC940YCw4r8FAUzZAHCPwvyrWECArAZB'

app = Flask(__name__)
bot = Bot(PAGE_ACCESS_TOKEN)
@app.route('/',methods=['GET', 'POST'])
def webhook():
	if request.method == 'GET':
		print("yes...")
		token = request.args.get('hub.verify_token')
		challenge = request.args.get('hub.challenge')
		if token == 'secret':
			return str(challenge)
		return '400'
	else:
		# print("hello......")
		# print(request.data)
		data =json.loads(request.data)
		messaging_events = data['entry'][0]['messaging']
		# print(messaging_events)

		for message in messaging_events:
			user_id = message['sender']['id']
			text_input = message['message'].get('text')

			print('Message from user ID {} - {}'.format(user_id,text_input))
			# print()
			bot.send_text_message(user_id,text_input)
		
		return '200'


if __name__ == '__main__':
	app.run(debug=True)