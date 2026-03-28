from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/blog")
def blog():
    posts = {
        "no_posts": "coming soon..."
    }
        
    return render_template("blog.html", posts=posts)

@app.route("/projects")
def projects():
    projects = [
        {
            "title": "DonBuilt Labs",
            "description": "A software brand focused on digital tools",
            "image": "donbuilt.jpg"
        },

        {
            "title": "Verto",
            "description":"An online hub connecting creatives with potential clients",
            "image": "verto.jpg"
        }
    ]

    return render_template("projects.html", projects=projects)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)