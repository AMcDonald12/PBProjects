from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_endpoint():
    blog_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_endpoint)
    all_posts = response.json()
    return all_posts

@app.route('/')
def home():
    return render_template("index.html", posts = get_endpoint())

@app.route('/post/<num>')
def get_post(num):
    return render_template("post.html", num=int(num)-1, posts=get_endpoint())

if __name__ == "__main__":
    app.run(debug=True)
