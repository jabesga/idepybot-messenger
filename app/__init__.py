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
	'greeting.text': 'Welcome to the new testing bot!'
}

response = requests.post(url, json=payload)
print(response.content)

@app.route("/webhook", methods=['GET','POST'])
def hook():
	if request.method == 'POST':
		print(request.get_json())
		
	else:
		if request.args.get('hub.verify_token') == VERIFY_TOKEN:
			return request.args.get('hub.challenge')
		else:
			return 'Error, wrong validation token'

	