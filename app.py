from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load questions from JSON
with open("questions.json") as f:
    questions = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/check_answers", methods=["POST"])
def check_answers():
    data = request.json
    user_answers = data["answers"]
    
    score = sum(1 for i, q in enumerate(questions) if user_answers[i] == q["answer"])

    return jsonify({"score": score, "total": len(questions)})

if __name__ == "__main__":
    app.run(debug=True)
