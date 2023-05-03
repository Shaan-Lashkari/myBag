import requests
import airtable

BASE_ID = "appTZGqtLSClGCdCo"
TABLE_NAME = "grade_data"
API_KEY = "keyxJJCgmuon6ezwN"


BASE_ID = "appTZGqtLSClGCdCo"
TABLE_NAME = "grade_data"
API_KEY = "keyxJJCgmuon6ezwN"

endpoint = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

header = {
        "Authorization":f"Bearer {API_KEY}",
        "Content-Type":"application/json"
}
def add_to_db(API_KEY,grade,name):    
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
