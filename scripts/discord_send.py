import os
import requests

DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.getenv("DISCORD_CHANNEL_ID_ONBOARDING")

def send_message(content: str, channel_id: str = None):
    channel_id = channel_id or CHANNEL_ID
    url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "content": content
    }
    r = requests.post(url, headers=headers, json=payload)
    if r.status_code >= 300:
        raise RuntimeError(f"Discord API error {r.status_code}: {r.text}")

if __name__ == "__main__":
    with open("onboarding_message.md", "r", encoding="utf-8") as f:
        msg = f.read()
    send_message(msg)
