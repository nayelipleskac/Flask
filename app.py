from flask import Flask
from flask import render_template, request
from flask import redirect, url_for
from database import Database
app = Flask(__name__)
#get users from database.py
users = Database.get_users()

@app.before_request #name not method, before_first_request deprecated
def initialize_database():
    Database.initialize()
    # if not app.config['_got_first_request']:
    #     print('hello')
    #     app.config['_got_first_request']= True
    # print('world')
#could call static funcs to retrieve/insert 
@app.route('/')
def home():
    return render_template('base.html', users =users)
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        #renders login page
        return render_template('login.html', users = users)

    #post request- form data, similar to a dictionary, if request.form.get('key') is used 
    #look for key in the form from POST request
    elif request.method == 'POST':
    #redirects to home page if login is successful
        user = request.form.get('user')
        print(user)
        
        name=Database.insert_record(user)
        print(name)

        return redirect(url_for('home', user = name))
    
@app.route('/orders', methods =['GET', 'POST'])
def orders():
    return render_template('orders.html')
    
    #after user logs in 
    # print('Redirecting ... ')
    # return redirect(url_for('login'))
if __name__ == '__main__':
    app.config['_got_first_request'] = False
    app.run(debug=True)

