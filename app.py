from flask import Flask, request, url_for, redirect
from flask import render_template
from databases import *
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-WILL-NEVER-GUESS'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nasijona.contect@gmail.com' #
app.config['MAIL_PASSWORD'] = 'NasiJona@14' #
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

email = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        print(request.files)
        
        p = request.files['image']
        p.save("static/images/"+p.name)
        create_image(p.filename,request.form['title'])
            
    return render_template("index.html")


@app.route('/sammer_camp', methods=['GET', 'POST'])
def sammer_camp():

	return render_template("sammer_camp_page.html")

@app.route('/courses', methods=['GET', 'POST'])
def go_courses():

	return render_template("courses.html")

@app.route('/special_events', methods=['GET', 'POST'])
def go_special_events():

	return render_template("events.html")


@app.route('/sent_mail', methods=['GET', 'POST'])
def message():
	name = request.form['Name']
	message = request.form['Message']
	mail = request.form['Mail']
	phone = request.form['Phone']
	msg = Message(' for Nasijona ', sender = 'nasijona.contect@gmail.com', recipients = ['nasijona.nazareth@gmail.com'])
	msg.body = "for Nasijona "+ " \n"+ message + " \n" + "name:"+ name + " \n" +" phone namber: "+phone + " \n"+" email " +mail
	email.send(msg)
	return render_template("index.html")


if __name__ == '__main__':
   app.run(debug = True)