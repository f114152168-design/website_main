# Sets up the routes for all the pages

from flask import Flask, render_template, request, make_response, jsonify
from flask_caching import Cache
from config import TEMPLATES_PATH, TEXT_PATH
from application.helpers import *
from application.ai_service import generate_text


app = Flask(__name__, template_folder=TEMPLATES_PATH)
app.jinja_env.filters["is_active"] = is_active
app.jinja_env.filters["get_language_image"] = get_language_image

app.config["CACHE_TYPE"] = "simple"
app.config["CACHE_DEFAULT_TIMEOUT"] = 3600
cache = Cache(app)


@app.route("/")
def loading():
    """Renders the 'Loading' page of the website."""

    #response = make_response(render_template("loading.html"))
    #response.headers["Cache-Control"] = "public, max-age=3"

    #return response
    return render_template("home.html")


@app.route("/home")
@cache.cached()
def home():
    """Renders the 'Home' page of the website."""

    return render_template("home.html")


@app.route("/about")
@cache.cached()
def about():
    """Renders the 'About Me' page of the website."""

    content = read_description(f"{TEXT_PATH}/about.txt")

    return render_template("about.html", content=content)


@app.route("/skills")
@cache.cached()
def skills():
    """Renders the 'Skills' page of the website."""

    skills = get_skills(f"{TEXT_PATH}/skills.json")

    return render_template("skills.html", skills=skills)


@app.route("/portfolio")
@cache.cached()
def portfolio():
    """Renders the 'Portfolio' page of the website."""

    repos = get_repositories()

    return render_template("portfolio.html", repos=repos)


@app.route("/contact", methods=["GET", "POST"])
@cache.cached()
def contact():
    """Renders the 'Contact' page of the website."""

    # User reached route via POST
    if request.method == "POST":
        return render_template("result.html")

    # User reached route via GET
    return render_template("contact.html")


@app.route("/result")
@cache.cached()
def result():
    """Renders the 'Result' page of the website."""

    return render_template("result.html")


@app.route("/ai-generator")
def ai_generator():
    """Renders the 'AI Text Generator' page of the website."""
    
    return render_template("ai_generator.html")


@app.route("/generate-text", methods=["POST"])
def generate_ai_text():
    """Generate text using AI based on user prompt."""
    
    try:
        data = request.get_json()
        prompt = data.get("prompt", "").strip()
        
        if not prompt:
            return jsonify({"error": "提示詞不能為空"}), 400
        
        if len(prompt) > 1000:
            return jsonify({"error": "提示詞過長，請限制在1000字以內"}), 400
        
        # Generate text using AI service
        result = generate_text(prompt)
        
        if result.startswith("Error:"):
            return jsonify({"error": result}), 500
        
        return jsonify({"result": result}), 200
    
    except Exception as error:
        print(f"ERROR! {error}.")
        return jsonify({"error": "伺服器錯誤，請稍後重試"}), 500
