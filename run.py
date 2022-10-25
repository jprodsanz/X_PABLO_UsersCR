from flask import Flask, render_template, url_for, request, redirect

from users import User 

app = Flask(__name__)
app.config ['SECRET_KEY'] = '05a21ff3e3c04f281944e3f8'  

@app.route('/')                 
def index():
    return redirect('/users')

@app.route('/users')         
def users():
    return render_template('users.html', users=User.get_all(), title='Users')

@app.route('/users/new')
def new_user():
    return render_template('new_user.html', title='New User')

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form,"request.form")
    User.save(request.form)
    return redirect('/users')

if __name__=="__main__":   
    app.run(debug=True)    