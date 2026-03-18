from flask import Flask, render_template, request
from rules import rule_based_decision
from ml_model import ml_prediction

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    result = None
    advice = []

    if request.method == "POST":

        score = int(request.form["score"])
        skills = int(request.form["skills"])
        internship = int(request.form["internship"])

        rule_result = rule_based_decision(score,skills,internship)
        ml_result = ml_prediction(score,skills,internship)

        # Hybrid decision
        result = f"Placement Chance: {ml_result}"

        # Recommendations
        if score < 75:
            advice.append("Improve academic score above 75.")

        if skills < 7:
            advice.append("Improve technical skills (target skill level ≥ 7).")

        if internship == 0:
            advice.append("Complete at least one internship.")

    return render_template("index.html", result=result, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)