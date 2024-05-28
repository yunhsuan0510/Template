from flask import Flask
from linebot import LineBotApi
from linebot.models import PostbackAction, URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
import os


app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))

@app.route('/push_message')
def push_message():
    line_bot_api.push_message(os.getenv('USER_ID'), TemplateSendMessage(
        alt_text='ButtonsTemplate',
        template=ButtonsTemplate(
            thumbnail_image_url='https://steam.oxxostudio.tw/download/python/line-template-message-demo.jpg',
            title='OXXO.STUDIO',
            text='這是按鈕樣板',
            actions=[
                PostbackAction(
                    label='postback',
                    data='發送 postback'
                ),
                MessageAction(
                    label='說 hello',
                    text='hello'
                ),
                URIAction(
                    label='前往 STEAM 教育學習網',
                    uri='https://steam.oxxostudio.tw'
                )
            ]
        )
    ))
    return 'Message sent!'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
