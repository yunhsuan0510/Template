from linebot import LineBotApi, WebhookHandler
# 需要額外載入對應的函示庫
from linebot.models import PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate
line_bot_api = LineBotApi('te/bzWwRmL8YVwG2nJdEUaaen2qBMvUDjvMxiWxylV3B5zt9Tto+N4IVKxMAB9uUG6yq4981CsitJ6IDTkFegFs8mmaYCw7bhFDgMA+2BJkqP3rrQKYTU1meE4QfcbyNgWbsYiY07EsYnh+YgXdMaQdB04t89/1O/w1cDnyilFU=')
line_bot_api.push_message('Ueb0d6dea2a95c12fdf716b078d624834', TemplateSendMessage(
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
