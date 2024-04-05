from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>\
        <h3>Modify the URL adding de number /4 like "http://127.0.0.1:5000/4 </h3>\
        <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>'

number = random.randint(0,9)
@app.route('/<int:user_number>')
def guess_numer(user_number):
    
    if user_number > number:
        return '<h1 style = "color: blue">Too High, try again !!!</h1>\
            <img src=https://shorturl.at/kvyAB>'
    elif user_number < number:
        return '<h1 style = "color: red">Too low, try again !!!</h1>\
            <img src=https://shorturl.at/bfoH0>'
    else:
        return '<h1 style = "color: green">You find me !!!</h1>\
            <img src=https://shorturl.at/sKOZ6>'

number = random.randint(0,9)

if __name__ == '__main__':
    app.run(debug=True)