from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# List of batchmates
batchmates = [
    "Vishal", "Tushar", "Devendra", "Nikhil", "Vishnu", "Harsh", "Vinay", "Pawan", "Hemant", "Ankit", "Yash","Shreyas","Lokesh", "Kanishk"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random')
def random_name():
    name = random.choice(batchmates)
    return jsonify({'name': name})

if __name__ == '__main__':
    app.run()
