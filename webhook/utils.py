import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_ID = os.getenv("WHATSAPP_PHONE_ID")
BASE_URL = f"https://graph.facebook.com/v17.0/{PHONE_ID}/messages"

def send_whatsapp_message(to_number: str, message: str):
    """
    Send a WhatsApp text message via Cloud API
    :param to_number: full international number e.g. 212612345678
    :param message: text message
    """
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(BASE_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print("Error sending WhatsApp message:", response.text)
    else:
        print("Message sent:", message)
    return response.json()
