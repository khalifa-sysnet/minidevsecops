from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Secure Login Demo</h1>
    <input placeholder='email'><br><br>
    <input placeholder='password' type='password'><br><br>
    <button>Login</button>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)