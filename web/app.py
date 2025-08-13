from flask import Flask, render_template, request, redirect, url_for
import redis, json
from datetime import datetime

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

def now_ts():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

@app.route('/', methods=['GET','POST'])

def index():

    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip().lower()
        message = request.form['message'].strip()
        ts = now_ts()

        msg = {'name': name, 'email': email, 'message': message, 'ts': ts}
        r.rpush('messages', json.dumps(msg))

        r.hincrby(f'user:{email}', 'visits', 1)
        r.hset(f'user:{email}', 'name', name)
        r.hset(f'user:{email}', 'last_visit', ts)

        r.set('latest_user', email)

        return redirect (url_for('messages'))
    return render_template('index.html')

@app.route('/messages')

def messages():
    raw = r.lrange('messages', 0, -1)
    messages = [json.loads(x) for x in raw]
    users = {key.split(':',1)[1]: r.hgetall(key) for key in r.scan_iter(match='user:*')}
    return render_template('messages.html', messages=messages, users=users)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)