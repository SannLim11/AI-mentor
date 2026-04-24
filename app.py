import os
from google import genai
from flask import Flask, request, jsonify

app = Flask(__name__)

client = genai.Client(api_key="GEMINI_API_KEY")

@app.route("/review", methods=["POST"])
def review_code():
    code = request.json.get("code")

    if not code:
        return jsonify({"error": "No code provided"}), 400

    try:
        response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        contents="Fix the code:",
        )

        feedback = response.text
        return jsonify({"feedback": feedback})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to get review from Gemini."}), 500

if __name__ == "__main__":
    app.run(debug=True)