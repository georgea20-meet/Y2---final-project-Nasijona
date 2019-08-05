from flask import Flask, request, url_for, redirect
from flask import render_template
from databases import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-WILL-NEVER-GUESS'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        print(request.files)
        
        p = request.files['image']
        p.save("static/images/"+p.name)
        create_image(p.filename,request.form['title'])
            
    return render_template("index.html")

if __name__ == '__main__':
   app.run(debug = True)