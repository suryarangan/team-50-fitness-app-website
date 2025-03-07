from flask import Flask, request, jsonify, render_template
import requests
import re

app = Flask(__name__)

# IVIS Labs API details
AI_API_KEY = "sk-6ecd2f574bf8434280f86547f1597ef1"
AI_API_URL = "https://chat.ivislabs.in/api/chat/completions"
MODEL_NAME = "gwen2.5:0.5b"

def clean_response(text):
    """Remove unnecessary formatting like stars (*) and excessive spaces."""
    text = re.sub(r"\*+", "", text)  # Remove all asterisks (*)
    text = re.sub(r"\n\s*\n", "\n", text)  # Remove excessive new lines
    return text.strip()

MODEL_NAME = "qwen2.5:0.5b"  # Corrected model name

def fetch_ai_response(prompt):
    """Fetch AI-generated response using IVIS Labs API."""
    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": MODEL_NAME,  # Ensure this model exists
        "max_tokens": 1000,
        "temperature": 0.7,
    }

    response = requests.post(AI_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        raw_text = response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
        return clean_response(raw_text)
    else:
        return f"Error: {response.json().get('detail', 'Unknown error')}"



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.json.get("text", "")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    response = fetch_ai_response(user_input)
    return jsonify({"response": response})

@app.route("/motivation", methods=["POST"])
def motivation():
    response = fetch_ai_response("Give me a fitness motivational quote.")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
