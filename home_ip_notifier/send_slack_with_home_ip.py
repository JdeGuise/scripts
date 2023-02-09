import os
from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

externalIP  = os.popen('curl -s ifconfig.me').readline()

response = client.chat_postMessage(
    channel=os.getenv("CHANNEL_ID"),
    text="Your home network IP is currently " + externalIP
)