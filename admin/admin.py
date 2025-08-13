# admin/admin.py
from flask import Flask, render_template, redirect, url_for
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def dashboard():
    total_messages = r.llen('messages')
    user_keys = list(r.scan_iter(match='user:*'))
    user_count = len(user_keys)
    latest_email = r.get('latest_user') or ''
    latest_name = r.hget(f'user:{latest_email}', 'name') if latest_email else ''

    # top visitors
    top = []
    for key in user_keys:
        email = key.split(':',1)[1]
        visits = int(r.hget(key, 'visits') or 0)
        top.append((email, visits))
    top.sort(key=lambda x: x[1], reverse=True)

    return render_template('admin.html',
                           user_count=user_count,
                           total_messages=total_messages,
                           latest_email=latest_email,
                           latest_name=latest_name,
                           top=top[:10])

@app.route('/reset', methods=['POST'])
def reset():
    r.flushdb()
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

