# import necessary libraries and functions
from database import *
from flask import Flask, jsonify, request, redirect, render_template, url_for, flash
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
        ls = search_train(source,destination,date)
        train_list.clear()
        for ele in ls:
            seats = getAvailableSeats(ele["train_no"], ele["date"])
            if seats <= 0:
                continue
            ele["seats"] = seats
            train_list.append(ele)
        return redirect("/result")
    return render_template("index.html")

@app.route('/result',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        train_no = request.form.get("train_no")
        from_stat = request.form.get("from_stat")
        to_stat = request.form.get("to_stat")
        departure_t = request.form.get("departure_t")
        arrival_t = request.form.get("arrival_t")
        date = request.form.get("date")
        pass_list.clear()
        pass_list.append(train_no)
        pass_list.append(from_stat)
        pass_list.append(to_stat)
        pass_list.append(departure_t)
        pass_list.append(arrival_t)
        pass_list.append(date)
        return redirect("/passenger")
    return render_template("result.html",tr_list=train_list)



@app.route('/passenger',methods=['GET','POST'])
def passenger():
    if request.method == 'POST':
        data = request.form.listvalues()
        ticket_list.clear()
        for ele in data:
            ticket_list.append(ele[0])
        

        pnr, seat_no = bookTicket(ticket_list)
        ticket_list.append(pnr)
        ticket_list.append(seat_no)

        '''
        databse me ticket daalo FUNCTION

        '''

        return redirect('/ticket')
    return render_template('Passenger_details.html',pass_d=pass_list)

@app.route('/ticket',methods=['GET','POST'])
def ticket():
    if request.method == 'POST':
        return redirect('/')
    return render_template('ticket.html',ticket_list=ticket_list)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        flag = checkUser(email,password)

        '''
        make pages for false credentials
        '''

        if flag == True:
            return redirect('/')
        else:
            print(f"email: {email}")
            print(f"password: {password}")
            return redirect('/login')
    return render_template('login.html')


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name  = request.form.get('name')
        email  = request.form.get('email')
        phone_number  = request.form.get('number')
        age  = request.form.get('age')
        gender = request.form.get('gender')
        address = request.form.get('address')
        password_1 = request.form.get('password_1')
        password_2 = request.form.get('password_2')
        
        user_detail = [name,email,password_1,age,gender,phone_number,email,address]
        flag = addUser(user_detail)
        print(flag)

        '''
        handle if flag false 
        '''
        return "/login"
    return render_template('registration.html')

@app.route('/admin',methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route('/admin/create',methods=['GET','POST'])
def create():
    return render_template('create.html')

@app.route('/admin/delete',methods=['GET','POST'])
def delete():
    return render_template('delete.html')

@app.route('/admin/update',methods=['GET','POST'])
def update():
    return render_template('update.html')





# driver function
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 80)
