from flask import Flask, request
import requests
import os

app = Flask(__name__)
app.debug = True

VERIFY_TOKEN = os.environ['verify_token']
PAGE_ACCESS_TOKEN = os.environ['page_access_token']

url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token={0}".format(PAGE_ACCESS_TOKEN)
payload = {
	'setting_type': 'greeting',
	'greeting': {
		'text': 'Welcome to the new testing bot!'
	}
}

response = requests.post(url, json=payload)
print(response.content)

def send_message(user_id, message):
	url = "https://graph.facebook.com/v2.6/me/messages?access_token={0}".format(PAGE_ACCESS_TOKEN)
	payload = {
		'recipient': {'id': user_id},
		'message': {'text':message}
	}

	json_response = requests.post(url, json=payload)
	return json_response

@app.route("/webhook", methods=['GET','POST'])
def hook():
	if request.method == 'POST':
		response = request.get_json()
		print(response)
		json_response = send_message(response['entry'][0]['messaging'][0]['recipient']['id'], 'This is a robot')
		print(json_response.content)
		return '200'
	else:
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		else:
			return 'Error, wrong validation token'
