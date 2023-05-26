from flask import Flask, redirect
from requests import get, post, delete
from serviceone import request_get, request_post, request_delete

app = Flask(__name__)

@app.route('/')
def red():
    return redirect('/todos')

@app.route('/todos', methods=['GET'])
def index():
    response = request_get()
    return response

@app.route('/todos/newtask/<int:user_id>', methods=['POST'])
def get_user(user_id):
    response = request_post(user_id)
    return response

@app.route('/todos/deltask/<int:user_id>', methods=['DELETE'])
def get_del(user_id):
    response = request_delete(user_id)
    return response

if __name__ == '__main__':
    app.run(port=5000, debug=True)