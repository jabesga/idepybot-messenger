import requests

class BaseBot:
    def __init__(self, page_access_token):
        self.page_access_token = page_access_token

    def change_greeting(self, text):
        url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token={0}".format(self.page_access_token)
        payload = {
            'setting_type': 'greeting',
            'greeting': {
                'text': text
            }
        }
        json_response = requests.post(url, json=payload)
        return json_response

    def send_message(self, user_id, message):
        url = "https://graph.facebook.com/v2.6/me/messages?access_token={0}".format(self.page_access_token)
        payload = {
            'recipient': {'id': user_id},
            'message': {'text': message}
        }
        json_response = requests.post(url, json=payload)
        return json_response