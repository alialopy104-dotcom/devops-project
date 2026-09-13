from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(r.lrange('tasks', 0, -1))

@app.route('/tasks', methods=['POST'])
def add_task():
    r.rpush('tasks', request.json['task'])
    return jsonify({"status": "added"}), 201

@app.route('/health')
def health():
    return "OK", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
