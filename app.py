from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('Bd2D5jUgAx37Cpzc7pka4HSH8efn+dGFiGIs4uk1ftLfZM624tG+Mia+Hd/S9WOV7FSi3/ZWe3z8Td6gcsRWWRrIUN+U5dlBGpEb/yYd8hphXUZORET0R5oiSHP+K/gSYnezMtdi1ulOYvEdTHqaGgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1a6f3f162ba333fb449dc7018fe9812f')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()