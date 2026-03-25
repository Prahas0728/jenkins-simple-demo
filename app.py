from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    # This is the main message your users will see
    return "<h1>Automation Success!</h1><p>Python app is running inside Docker via Jenkins.</p>"

@app.route('/health')
def health_check():
    # This helps Jenkins or Docker verify the app is 'alive'
    return jsonify(status="up"), 200

if __name__ == '__main__':
    # host='0.0.0.0' is REQUIRED to access the app from outside the container
    app.run(host='0.0.0.0', port=5000, debug=True)
