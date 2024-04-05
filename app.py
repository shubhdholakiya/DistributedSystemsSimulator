# Imports the Flask class.
# Creates an instance of the Flask class. 
# This instance is our WSGI application.
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data structure to store nodes
nodes = []

@app.route('/nodes', methods=['POST'])
def create_node():
    data = request.json
    new_node = {
        'id': len(nodes) + 1,
        'status': data.get('status', 'active'),
        'load': data.get('load', 0)
    }
    nodes.append(new_node)
    return jsonify(new_node), 201

@app.route('/nodes', methods=['GET'])
def get_nodes():
    return jsonify(nodes)

if __name__ == '__main__':
    app.run(debug=True)

# Runs the app in debug mode, which is helpful during development as it will reload the app for you upon changes.
# if __name__ == '__main__':
#     app.run(debug=True)