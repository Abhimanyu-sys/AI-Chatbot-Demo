from flask import Flask, request, jsonify
from flask_cors import CORS

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
# client_sheet = gspread.authorize(creds)

# sheet = client_sheet.open("Leads Data").sheet1


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Detect phone number
    if any(char.isdigit() for char in user_message):

        name = user_message.split()[0]
        phone = ''.join(filter(str.isdigit, user_message))
        time = datetime.now().strftime("%Y-%m-%d %H:%M")

        # sheet.append_row([name, phone, time])

        reply = "Thank you! Our team will contact you soon."

    elif "buy" in user_message.lower() or "flat" in user_message.lower():
        reply = "Great! We have multiple options available. Can I know your name and phone number?"

    elif "coaching" in user_message.lower():
        reply = "We offer coaching programs. Please share your name and contact number."

    else:
        reply = "Please share your requirement and contact number."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=5001)
