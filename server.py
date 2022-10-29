# import necessary libraries and functions
from database import *
from flask import Flask, jsonify, request, redirect, render_template, url_for
import jinja2

  
# creating a Flask app
app = Flask(__name__)
train_list = []
pass_list = []
ticket_list = []
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
# @app.route('/')
# def home():
        # data = "Hello World"
        # return jsonify({'data': data})

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST': 
        source = request.form.get("source-station")
        destination = request.form.get("destination-station")
        date = request.form.get("dateOfJourney")
        print(source + "dateOfJourney is = " + date)
        ls = search_train(source,destination)
        train_list.clear()
        for ele in ls:
            train_list.append(ele)
        return redirect("/result")
    return render_template("index.html")

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        data = request.form
        ele = data.to_dict()
        pass_list.clear()
        for e in ele:
            pass_list.append(e)
        return redirect("/passenger")
    return render_template("result.html",tr_list=train_list)



@app.route('/passenger',methods=['GET','POST'])
def passenger():
    if request.method == 'POST':
        data = request.form.listvalues()
        ticket_list.clear()
        for ele in data:
            ticket_list.append(ele[0])
        return redirect('/ticket')
    return render_template('Passenger_details.html',pass_d=pass_list)

@app.route('/ticket',methods=['GET','POST'])
def ticket():
    if request.method == 'POST':
        return redirect('/')
    return render_template('ticket.html',ticket_list=ticket_list)


@app.route('/login')
def login():
    return render_template('login_registration_page.html')


@app.route('/register')
def register():
    return render_template('Register_page.html')

# driver function
if __name__ == '__main__':
  
    app.run(debug = True, host = '0.0.0.0', port = 80)
