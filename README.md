# AI-mentor

Setup
python --version
pip install flask google-genai
pip install python-dotenv

Create .env file:
GEMINI_API_KEY=your_actual_api_key_here

Create your own API key
1. Go to Google AI Studio
2. Get API key
3. Copy the key
4. Replace in .env file

Securely read the API key:

In app.py:
from dotenv import load_dotenv
load_dotenv()

Link the Frontend to the Backend:

Add the following code to the app.py : 
@app.route("/")
def index():
    return render_template("index.html")

At terminal:
python app.py

