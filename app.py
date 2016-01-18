from flask import Flask
from redis import Redis
from flask import render_template

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# @app.route('/')
# def hello():
#     # redis.incr('hits')
#     # return 'b Hello World! I have been seen %s times. (branch: develop)' % redis.get('hits')
#     return 'hello'

@app.route('/')
def home():
    return render_template('index.html', data=dict(hits=123))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
