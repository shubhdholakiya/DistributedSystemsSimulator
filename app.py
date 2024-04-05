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

@app.route('/nodes/<int:node_id>', methods=['PUT'])
def update_node(node_id):
    data = request.json
    node = next((node for node in nodes if node['id'] == node_id), None)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    node.update({
        'status': data.get('status', node['status']),
        'load': data.get('load', node['load'])
    })
    return jsonify(node)

@app.route('/nodes/<int:node_id>', methods=['DELETE'])
def delete_node(node_id):
    global nodes  # Since we're modifying the list
    node = next((node for node in nodes if node['id'] == node_id), None)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    nodes = [node for node in nodes if node['id'] != node_id]
    return jsonify({'message': 'Node deleted'})


@app.route('/simulate/communication', methods=['POST'])
def simulate_communication():
    # This endpoint would be more complex in a real application
    # For now, it just returns a success message
    return jsonify({'message': 'Communication simulated successfully'})

@app.route('/simulate/failure', methods=['POST'])
def simulate_failure():
    data = request.json
    node_id = data.get('node_id')
    node = next((node for node in nodes if node['id'] == node_id), None)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    node['status'] = 'failed'
    return jsonify({'message': f'Node {node_id} failed'})

@app.route('/simulate/recovery', methods=['POST'])
def simulate_recovery():
    data = request.json
    node_id = data.get('node_id')
    node = next((node for node in nodes if node['id'] == node_id), None)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    node['status'] = 'active'
    return jsonify({'message': f'Node {node_id} recovered'})


if __name__ == '__main__':
    app.run(debug=True)

# Runs the app in debug mode, which is helpful during development as it will reload the app for you upon changes.
# if __name__ == '__main__':
#     app.run(debug=True)