
# import requests
# import os
# from dotenv import load_dotenv
#
# # Load environment variables from .env
# load_dotenv()
#
#
# class SlackNotifier:
#     @staticmethod
#     def send_message(message: str):
#         """Send a plain text message to Slack."""
#         slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
#         if not slack_webhook_url:
#             print("❌ SLACK_WEBHOOK_URL is not set in .env")
#             return
#
#         payload = {"text": message}
#
#         try:
#             response = requests.post(slack_webhook_url, json=payload)
#             response.raise_for_status()
#             print(f"✅ Slack notification sent: {message}")
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Failed to send Slack notification: {e}")
#
#     @staticmethod
#     def send_screenshot_notification(message: str, screenshot_path: str):
#         """Send a Slack message with a screenshot attachment."""
#         slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
#         if not slack_webhook_url:
#             print("❌ SLACK_WEBHOOK_URL is not set in .env")
#             return
#
#         # Read the screenshot as bytes
#         with open(screenshot_path, "rb") as image_file:
#             image_data = image_file.read()
#
#         payload = {
#             "text": message,
#             "attachments": [
#                 {
#                     "title": "📸 Screenshot",
#                     "image_url": f"data:image/png;base64,{image_data}"
#                 }
#             ]
#         }
#
#         try:
#             response = requests.post(slack_webhook_url, json=payload)
#             response.raise_for_status()
#             print(f"✅ Slack screenshot notification sent: {message}")
#         except requests.exceptions.RequestException as e:
#             print(f"❌ Failed to send screenshot notification: {e}")


import requests
import os
from dotenv import load_dotenv

load_dotenv()

def slack_notify(message: str, screenshot_path: str = None):
    """Send a notification to Slack, optionally with a screenshot."""
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if not slack_webhook_url:
        print("❌ SLACK_WEBHOOK_URL is not set in .env")
        return

    payload = {"text": message}

    # Attach screenshot if provided
    if screenshot_path:
        with open(screenshot_path, "rb") as image:
            payload["attachments"] = [{
                "title": "📸 Screenshot",
                "image_url": f"data:image/png;base64,{image.read().encode('base64').decode()}"
            }]

    try:
        response = requests.post(slack_webhook_url, json=payload)
        response.raise_for_status()
        print(f"✅ Slack notification sent: {message}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send Slack notification: {e}")
