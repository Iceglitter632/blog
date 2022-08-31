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

line_bot_api = LineBotApi('ThaPFKPUR+qFoh+jU51rJP0A/F2+z3+EBlprxBIKabObObE12cX5LKGh+Wpa4xpkno2bfKtl+Q0yC/P40oiGi8dfXGJCx+sYYnOTtJ7VS5zV+Rsr76WMpQMJOTRb8qe2vxB/49i3LIH3ViHCPvDqTwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bfabea898dfc1d49e2ff5106368d0360')


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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()