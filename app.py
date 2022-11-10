#載入LineBot所需要的模組 
from flask import Flask, request, abort  
from linebot import (LineBotApi, WebhookHandler) 
from linebot.exceptions import (InvalidSignatureError) 
from linebot.models import *

app = Flask(__name__)  
# 必須放上自己的Channel Access Token 
line_bot_api = LineBotApi('6rEFES/spFG3K7H3CK0q7Kn+pfD3zr+cljnFX0WsedUnjqEja9Bat+4lIh9b+wlfVXQITfIus47Rwglh1tx/oZv3lGbHCtshhR0hCrDvGla5ePJ3m/B1o/XafXewpxsQY/7H9W4xwIFZFGHC6cudqAdB04t89/1O/w1cDnyilFU=')  
# 必須放上自己的Channel Secret
handler = WebhookHandler('d77805be5e4c58ab1d6b084a62d99158')

line_bot_api.push_message('U59382c25fdcba8e44ea029bd7075838c', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request 
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

#訊息傳遞區塊 
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage) 
def handle_message(event):     
    message = event.message.text     
    line_bot_api.reply_message(event.reply_token,TextSendMessage(message))

#主程式 
import os 
if __name__ == "__main__":    
    port = int(os.environ.get('PORT', 5000))     
    app.run(host='0.0.0.0', port=port)