from flask import Flask, render_template, request, redirect, url_for
from models import Project, BlogPost

app = Flask(__name__)

# Dummy data
projects = [
    Project('Plate Reader', 'Vehical Number Plate Reader'),
    Project('Alexa', 'AI Assistant'),
]

blog_posts = [
    BlogPost('Code Reader', 'Content of blog post 1'),
    BlogPost('A List Apart', 'Content of blog post 2'),
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects, blog_posts=blog_posts)

# Admin page to manage projects and blog posts
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        if request.form['type'] == 'project':
            title = request.form['title']
            description = request.form['description']
            projects.append(Project(title, description))
        elif request.form['type'] == 'blog_post':
            title = request.form['title']
            content = request.form['content']
            blog_posts.append(BlogPost(title, content))
        return redirect(url_for('admin'))

    return render_template('admin.html', projects=projects, blog_posts=blog_posts)

if __name__ == '__main__':
    app.run(debug=True)
