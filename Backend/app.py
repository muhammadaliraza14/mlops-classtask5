from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    if name and email:
        user = {'name': name, 'email': email}
        collection.insert_one(user)
        return jsonify({'message': 'Data stored successfully'}), 200
    else:
        return jsonify({'error': 'Name and email are required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
