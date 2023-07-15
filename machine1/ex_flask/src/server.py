from flask import Flask, make_response, request, redirect, render_template
from functools import wraps
import jwt


app = Flask(__name__)

with open('/app/private.pem', 'rb') as f:
   app.config['PRIVATE_KEY'] = f.read()
with open('/app/public.pem', 'rb') as f:
   app.config['PUBLIC_KEY'] = f.read()

def create_session(user={'username': f'Hacker', 'money': 5, 'luck': 0}):
    token = jwt.encode(user, app.config['PRIVATE_KEY'], algorithm='RS256')
    return token

def token_handler(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'token' in request.cookies:
            token = request.cookies['token']
        else:
            response = make_response(redirect('/'))
            response.set_cookie('token', create_session())
            return response

        try:
            user = jwt.decode(token, app.config['PUBLIC_KEY'], algorithms=['RS256','HS256'])
        except:
            return {"status": -1, "message": "Invalid token!"}, 401
        return f(user, *args, **kwargs)
    return decorator

@app.route('/', methods=['GET'])
@token_handler
def home(user):
    return render_template('index.html', username=user['username'], money=user['money'])

if __name__ == "__main__":
    app.run(debug=False , host='0.0.0.0', port=8080)