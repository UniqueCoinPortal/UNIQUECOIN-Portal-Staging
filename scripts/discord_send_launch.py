import os
import requests

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
CHANNEL_ID = os.environ.get("DISCORD_CHANNEL_ID_ANNOUNCEMENTS")

def send_message(content):
    url = f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"content": content}
    r = requests.post(url, json=payload, headers=headers)
    if r.status_code >= 300:
        raise SystemExit(f"Discord API error {r.status_code}: {r.text}")

if __name__ == "__main__":
    with open("launch_message.md", "r", encoding="utf-8") as f:
        md = f.read()
    send_message(md)
