from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "jordan"

debug = DebugToolbarExtension(app)


@app.route("/")
def ask_questions():
    """Generate and show form to ask for words."""
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def show_story():
    """Show Madlib result."""

    # arguments received from form
    answers = request.args
    text = story.generate(answers)
    return render_template("story.html", text=text)
