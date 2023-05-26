from requests import get, post, delete

def request_get():
    url = "https://jsonplaceholder.typicode.com/todos/"
    req = get(url)
    req = req.json()
    return req

def request_post(number):
    url = "https://jsonplaceholder.typicode.com/todos/"
    req = delete(f'{url}/{number}')
    req = req.json()
    return req

def request_delete(number):
    url = "https://jsonplaceholder.typicode.com/todos/"
    req = delete(f'{url}/{number}')
    req = req.json()
    return req

response = request_post(1)
print(response)