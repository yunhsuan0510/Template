import openai
import os
from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import TextSendMessage
import json

app = Flask(__name__)

# 獲取環境變數
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN')
channel_secret = os.getenv('CHANNEL_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')

# 檢查環境變數是否設置
if not channel_access_token:
    raise ValueError("CHANNEL_ACCESS_TOKEN 環境變數未設置。")
if not channel_secret:
    raise ValueError("CHANNEL_SECRET 環境變數未設置。")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY 環境變數未設置。")

# 初始化 LineBotApi 和 WebhookHandler
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

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

        # 提取前六個字符並轉換為小寫
        ai_msg = msg[:6].lower()
        reply_msg = ''

        if ai_msg == 'hi ai:':
            openai.api_key = openai_api_key
            # 使用新版的 OpenAI Chat API
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": msg[6:]},
                ],
                max_tokens=256,
                temperature=0.5,
            )
            # 獲取回覆文本並去除換行符
            reply_msg = response['choices'][0]['message']['content'].replace('\n', '')
        else:
            reply_msg = msg

        text_message = TextSendMessage(text=reply_msg)
        line_bot_api.reply_message(tk, text_message)
    except InvalidSignatureError:
        print('簽名無效。請檢查您的 channel access token 和 channel secret。')
    except Exception as e:
        print(f'錯誤：{e}')
    return 'OK'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
