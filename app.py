import os
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the home route
@app.route('/')
def home():
    return "Hello, World! Your Flask application is running successfully."

# Define a sample API endpoint that returns JSON data
@app.route('/api/status')
def status():
    return jsonify({
        "status": "online",
        "message": "The application server is healthy."
    })

# Ensure the server only runs if this script is executed directly
if __name__ == '__main__':
    # Fetch port from environment variables (defaults to 5000 for local development)
    port = int(os.environ.get('PORT', 5000))
    
    # Run the application
    # Set debug=True only for local testing; disable it in production
    app.run(host='0.0.0.0', port=port, debug=True)

