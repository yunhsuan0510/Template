from linebot import LineBotApi, WebhookHandler
# 需要額外載入對應的函示庫
from linebot.models import PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
import os
# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(os.getenv('CHANNEL_ACCESS_TOKEN'))

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
