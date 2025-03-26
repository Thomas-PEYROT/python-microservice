import discovery
from flask import Flask, request, jsonify

# Register
SERVER_UUID, SERVER_PORT = discovery.register()
print(f"Registered Server {SERVER_UUID} on port {SERVER_PORT}")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from python service!"


@app.route('/hello', methods=['POST'])
def hello_with_name():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Missing "name" field'}), 400

    name = data['name']
    return jsonify({'message': f'Hello {name}'})

if __name__ == "__main__":
    app.run(port=SERVER_PORT)

# Unregister
unregister_response = discovery.unregister(SERVER_UUID)
print(unregister_response['message'])