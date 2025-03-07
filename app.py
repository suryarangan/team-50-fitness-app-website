from flask import Flask, request, jsonify, render_template
import requests
import re

app = Flask(__name__)

# IVIS Labs API details
AI_API_KEY = "sk-6ecd2f574bf8434280f86547f1597ef1"
AI_API_URL = "https://chat.ivislabs.in/api/chat/completions"
MODEL_NAME = "qwen2.5:0.5b"  # Corrected model name


def clean_response(text):
    """Remove unnecessary formatting like stars (*) and excessive spaces."""
    text = re.sub(r"\*+", "", text)  # Remove all asterisks (*)
    text = re.sub(r"\n\s*\n", "\n", text)  # Remove excessive new lines
    return text.strip()


def is_fitness_related(prompt):
    """Check if the user input is related to fitness."""
    fitness_keywords = [
        "workout", "exercise", "training", "gym", "fitness", "bodybuilding",
        "yoga", "cardio", "strength", "muscle", "calories", "weight loss",
        "nutrition", "running", "squats", "push-ups", "dumbbells", "deadlift", "health"
    ]

    return any(word in prompt.lower() for word in fitness_keywords)


def fetch_ai_response(prompt):
    """Fetch AI-generated response using IVIS Labs API, but only for fitness-related queries."""
    if not is_fitness_related(prompt):
        return "I don't know. I only provide fitness descriptions and motivational quotes."

    # Enforcing fitness context for all queries
    modified_prompt = f"This is a fitness-related AI. Please respond only in the context of fitness. Here is the user's request: {prompt}"

    headers = {"Authorization": f"Bearer {AI_API_KEY}", "Content-Type": "application/json"}
    data = {
        "messages": [{"role": "user", "content": modified_prompt}],
        "model": MODEL_NAME,
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
