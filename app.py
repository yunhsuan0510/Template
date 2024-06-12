import openai
import os
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
import json

app = Flask(__name__)

# Initialize LineBotApi and WebhookHandler
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('CHANNEL_SECRET'))

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)
    json_data = json.loads(body)
    print(json_data)
    try:
        signature = request.headers['X-Line-Signature']
        handler.handle(body, signature)

        tk = json_data['events'][0]['replyToken']
        msg = json_data['events'][0]['message']['text']

        # Extract the first five characters and convert to lowercase
        ai_msg = msg[:6].lower()
        reply_msg = ''

        if ai_msg == 'hi ai:':
            openai.api_key = os.getenv("OPENAI_API_KEY")
            # Send the message to OpenAI
            response = openai.Completion.create(
                model='text-davinci-003',
                prompt=msg[6:],
                max_tokens=256,
                temperature=0.5,
            )
            # Get the response text and remove newline characters
            reply_msg = response["choices"][0]["text"].replace('\n', '')
        else:
            reply_msg = msg

        text_message = TextSendMessage(text=reply_msg)
        line_bot_api.reply_message(tk, text_message)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
    except Exception as e:
        print(f'Error: {e}')
    return 'OK'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
