from flask import Flask, Response
from middleware import setup_metrics
import prometheus_client


app = Flask(__name__)
setup_metrics(app)

@app.route('/test/')
def test():
    return 'rest'

@app.route('/test1/')
def test1():
    1/0
    return 'rest'

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')
@app.route('/metrics/')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run('0.0.0.0', 9000)
