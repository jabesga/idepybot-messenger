from flask import Flask, request
from .bot import Bot
import requests
import os

app = Flask(__name__)
app.debug = True

VERIFY_TOKEN = os.environ['verify_token']
PAGE_ACCESS_TOKEN = os.environ['page_access_token']


bot = Bot(PAGE_ACCESS_TOKEN)
bot.change_greeting('Hello, this is a new greeting')

@app.route("/webhook", methods=['GET'])
def verify():
	if request.args.get('hub.verify_token') == VERIFY_TOKEN:
		return request.args.get('hub.challenge')
	else:
		return 'Error, wrong validation token'

@app.route("/webhook", methods=['POST'])
def webhook():
	response = request.get_json()
	print(response)
	if 'is_echo' in response['entry'][0]['messaging'][0]:
		if response['entry'][0]['messaging'][0]['is_echo']:
			return '200'
	json_response = bot.send_message(response['entry'][0]['messaging'][0]['sender']['id'], 'This is a robot')
	print('RESPONDIDO {0}'.format(json_response))
	return '200'

