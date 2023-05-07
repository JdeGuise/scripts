import os
import sys

from slack_sdk import WebClient
from dotenv import load_dotenv

load_dotenv()

slack_token = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=slack_token)

success_msg="A new photo has been saved to your PhotoPrism folder on GoosePC.\n"
error_msg="An error was encountered while trying to save new media to your PhotoPrism folder on GoosePC.\nFile path on phone: " + sys.argv[2]

computer_file_path = "C:\PhotoPrism\originals\Camera\\" + (sys.argv[2].split('InstantUpload/Camera/')[1].replace("/", "\\"))

is_success = True if sys.argv[1] == 'true' else False 
if is_success:
    MSG = success_msg
    MSG+=("\n*File path on Nextcloud:* \n" + sys.argv[2])
    MSG+=("\n*File path on GoosePC:* \n" + computer_file_path)
else:
    error_from_bash = [" ".join(sys.argv[3:])]
    MSG = error_msg
    MSG+=("\n*Error message:* \n'" + error_from_bash[0] + "'")

response = client.chat_postMessage(
    channel=os.getenv("CHANNEL_ID"),
    text=MSG
)

# Call the files.upload method using the WebClient
# Uploading files requires the `files:write` scope
response = client.files_upload_v2(
    channel=os.getenv("CHANNEL_ID"),
    initial_comment="*Transferred file:*",
    file=sys.argv[2],
)