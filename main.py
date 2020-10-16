from flask import Flask, request, render_template
import pyrebase 
import datetime
config = {
    "apiKey": "AIzaSyBk9v3O9ihHUO1bTaEP1dUt3eWbugKF8Uc",
    "authDomain": "attendance-marking-5f177.firebaseapp.com",
    "databaseURL": "https://attendance-marking-5f177.firebaseio.com",
    "storageBucket": "attendance-marking-5f177.appspot.com",
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__,)
@app.route('/',methods=['POST','GET'])   
def attend():
    submit = False
    if request.method == 'POST':
        if request.form['submit'] == 'Submit':
            x = datetime.datetime.now()
            x = x.strftime("%Y-%m-%d %H:%M:%S")

            name = request.form.get('name')
            email = request.form.get('email')
            number = request.form.get('number')
            regno = request.form.get('regno')

            print(name,email,number,regno)
            payload = {'time': x, 'name' : name,'email': email,'number':number, "regno" : regno}
            db.child('attendance').push(payload)
            return render_template('attend.html', submit=True, name = payload['name'])
    return render_template('attend.html', submit = False)
if __name__ =='__main__':  
    app.run(host='0.0.0.0',debug=True) 
