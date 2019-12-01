import requests
import json

FACEBOOK_GRAPH_URL = 'https://graph.facebook.com/v2.6/me/'

class Bot(object):
	"""docstring for Bot"""
	def __init__(self, access_token,api_url=FACEBOOK_GRAPH_URL):
		self.access_token = access_token
		self.api_url = api_url + 'messages'

	def send_text_message(self,psid,message,messaging_type="RESPONSE"):
		headers = {
			'Content-Type': 'application/json'
		}


		data= {
			'messaging_type': messaging_type,
			'recipient': {'id': psid},
			'message': {'text': message}
		}
		print(data)

		params = {'access_token': self.access_token}
		# self.api_url = self.api_url + 'messages'
		response = requests.post(self.api_url,
								headers=headers, params=params,
								data=json.dumps(data))
		# print(response.content)

# bot =Bot('EAAjpHJXWzoMBAMkH6ZBqC9U4C9ZBc0ebbimEvZBjPQaVkxYgNPeWmSgzub1K12SQlrJS5fDFiq9iOdwyTsODzvGTXTdPLm3ZBLNFgb7tx8ByiZBRp8N3UZAHSpV9UlbDPZByJu6vkpCZBCxvOoWiIfkPI5sC940YCw4r8FAUzZAHCPwvyrWECArAZB')
# bot.send_text_message(2863689613663494,'hi')
		