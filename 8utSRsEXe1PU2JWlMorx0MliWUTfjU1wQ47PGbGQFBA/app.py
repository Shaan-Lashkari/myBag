
    
#______________________________________________________________________________________________________________________________________________    
from flask import Flask, render_template
from flask import request as rq
import requests
import airtable


BASE_ID = "appTZGqtLSClGCdCo"
TABLE_NAME = "grade_data"
API_KEY = "keyxJJCgmuon6ezwN"

app= Flask(__name__)


endpoint = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

header = {
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
}


def add_to_db(grade,name):    
    new_data = {
        "records": [
            {
                "fields": {
                    "grade": grade,
                    "teacher_name": name
                }
            },
        ]
    }
    r = requests.post(endpoint,json=new_data,headers=header)
    
@app.route('/')

def single():
    return render_template('home.html')


@app.route('/success')
def single():
    t_name=rq.form['t_name']
    print(f"the teacher's name is {t_name}")
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

#something ---------______________________________________________________________________________


print(
    'hello and welcome to aertable db saver. Please follow the instructions below to\
    add your data to the DB.'
)
condition = "t"
while condition == "t":
    name = input('Hello Dear CUSTOMER, please enter the name of class teacher : \n')
    grade = input('Please enter the grade of the same class teacher : \n')
    
    add_to_db(API_KEY,grade,name)
    condition = input("Do you want to add more records to our DB? (t/f) : \n")
