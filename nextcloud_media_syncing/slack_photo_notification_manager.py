import os
import sys

from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

success_msg="A new photo has been saved to your PhotoPrism folder on GoosePC"
error_msg="An error was encountered while trying to save new media to your PhotoPrism folder on GoosePC.\nFile path on phone: " + sys.argv[2]

is_success = True if sys.argv[1] == 'true' else False 
if is_success:
    MSG = success_msg
    MSG+=("\nFile path on phone: " + sys.argv[2])
else:
    error_from_bash = [" ".join(sys.argv[3:])]
    MSG = error_msg
    MSG+=("\nError message: '" + error_from_bash[0] + "'")

response = client.chat_postMessage(
    channel=os.getenv("CHANNEL_ID"),
    text=MSG
)