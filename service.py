import json
from flask import Flask, jsonify, request
from chatbot import predict_class, get_response

# configurar API
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
intents = json.loads(open('intents.json').read())


@app.route('/')
def home():
    return 'API está online'


@app.route('/answers')
def answers():
    user_ask = request.args.get('ask')
    return bot_answer(user_ask)


def convert_message(message):
    return str(message).lower().strip()


def bot_answer(ask_to_robot):
    if ask_to_robot.strip() == "":
        bot_response = "Vamos lá, me mande uma mensagem!!!"
    else:
        ints = predict_class(convert_message(ask_to_robot))
        bot_response = get_response(ints, intents)
    return jsonify({
        "answer": str(bot_response)
    })


if __name__ == "__main__":
    app.run()
