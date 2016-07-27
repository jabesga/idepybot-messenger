from flask import Flask, request
import os

app = Flask(__name__)
app.debug = True

VERIFY_TOKEN = os.environ['verify_token']

@app.route("/webhook")
def hook():
	response = request.get_json()
	if response['hub.verify_token'] == VERIFY_TOKEN:
		return response['hub.challenge']
	else:
		return 'Error, wrong validation token'