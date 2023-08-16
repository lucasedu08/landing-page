from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_message = request.values.get('Body', '').lower()

    response = MessagingResponse()

    if 'olá' in incoming_message:
        response.message('Olá! Como posso ajudar?')
    elif 'ajuda' in incoming_message:
        response.message('Claro, estou aqui para ajudar!')
    else:
        response.message('Desculpe, não entendi sua mensagem.')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
