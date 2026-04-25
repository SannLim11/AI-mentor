import os
from google import genai
from flask import Flask, request, jsonify

app = Flask(__name__)

client = genai.Client(api_key="GEMINI_API_KEY")

@app.route("/review", methods=["POST"])
def review_code():
    data = request.get_json()
    user_code = data.get('code')

    if not user_code or user_code.strip() == "":
        return jsonify({"error": "No code provided"}), 400

    try:
        response = client.models.generate_content(
        model="gemini-3.1-pro-preview",
        # Update the contents line in app.py
        contents=f"You are an expert Senior Software Engineer. Provide a concise code review for the following snippet. Focus on bugs, security, and performance:\n\n{user_code}"
        )

        feedback = response.text
        return jsonify({"feedback": response.text})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to get review from Gemini."}), 500

if __name__ == "__main__":
    app.run(debug=True)