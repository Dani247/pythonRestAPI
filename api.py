from bottle import run, get, post, request

#datos
users = [{'username': 'julio', 'password': '1234'},
        {'username': 'pepita244', 'password': 'auh412'},
        {'username': 'raulito56', 'password': 'raulGol123'},
        {'username': 'RandyRandom', 'password': 'random'},
        {'username': 'elweon048', 'password': 'elwon'}]

#todos los usuarios
@get('/users')
def getUsers():
    return {'users': users}

#usuario por nombre
@get('/users/<name>')
def getUsersbyName(name):
    for data in users:
        print(data['username'])
        if data['username'] == str(name):
            return data
    return "no encontrado"

#insertar usuario
@post('/users')
def insertUsers():
    newUser = {'username': request.json.get('username'), 'password': request.json.get('password')}
    users.append(newUser)
    return {'users': users}

run(reLoader=True, debug=True)