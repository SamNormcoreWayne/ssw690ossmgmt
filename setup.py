from flask import Flask, jsonify, request
import time


app = Flask(__name__)
usersaw = {}

@app.route("/", methods = ['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'you sent': 'some json'}), 201
    else:
        return jsonify({"about": "Hello world"})

@app.route('/hi', methods =[ 'GET', 'POST'])
def hi():
    user = request.headers.get('user')
    return jsonify("Hello and welcome %s" % user)

@app.route('/checkin/<user>', methods=['GET', 'POST'])
def checkin(user):
    usersaw[user] = time.strftime('%Y-%m-%d')
    return jsonify(sucess=True, user=user)

@app.route('/last_seen/<user>', methods=['GET', 'POST'])
def last_seen(user):
    if user in usersaw:
        return jsonify(user=user, date=usersaw[user])
    else:
        return jsonify(error="Kept track of you", user=user), 404

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiple10(num):
    return jsonify({"result": num*10})


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0', port=5000)