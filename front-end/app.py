from flask import Flask,request,render_template;
import requests;

app = Flask(__name__);

backend_URL = 'http://0.0.0.0:9000';

@app.route('/')
def home():
    return render_template('form.html');

@app.route('/submit',methods = ["POST"])
def submit():
    form_data =  dict(request.form);
    requests.post(backend_URL+'/submit',json=form_data);
    return "Data Submitted Successfully";

@app.route('/get_data')
def get_data():
    response = requests.get(backend_URL+'/view');
    return response.json();
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True); 