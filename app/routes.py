from app import app

@app.route('/')
@app.route('/index')
@app.route('/getname')
@app.route('/login')
@app.route('/register')


def index():
    return "Hello, World!"

def getname(id):
    id = 10
    return id

def login():
    return "Login"

def register():
    print("Check")
    return "Register"        