# Imports the Flask class.
# Creates an instance of the Flask class. 
# This instance is our WSGI application.
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import random
from flask_cors import CORS

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://simulator_user:rootshubh@localhost/distributed_systems_simulator'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Node(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80), nullable=False)
    load = db.Column(db.Integer, nullable=False)
    is_online = db.Column(db.Boolean, default=True, nullable=False)  


# Wrap database creation in an application context
with app.app_context():
    db.create_all()

# In-memory data structure to store nodes
nodes = []

CORS(app)
@app.route('/')
def home():
    return 'Home page'

@app.route('/nodes', methods=['POST'])
def create_node():
    data = request.json
    new_node = Node(status=data.get('status', 'active'), load=data.get('load', 0))
    db.session.add(new_node)
    db.session.commit()
    return jsonify({'id': new_node.id, 'status': new_node.status, 'load': new_node.load}), 201

@app.route('/nodes', methods=['GET'])
def get_nodes():
    nodes_query = Node.query.all()
    nodes_data = [{'id': node.id, 'status': node.status, 'load': node.load} for node in nodes_query]
    return jsonify(nodes_data)

@app.route('/nodes/<int:node_id>', methods=['PUT'])
def update_node(node_id):
    data = request.json
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    if 'status' in data:
        node.status = data['status']
    if 'load' in data:
        node.load = data['load']
    db.session.commit()
    return jsonify({'id': node.id, 'status': node.status, 'load': node.load})

@app.route('/nodes/<int:node_id>', methods=['DELETE'])
def delete_node(node_id):
    node = Node.query.get(node_id)
    if node is None:
        return jsonify({'message': 'Node not found'}), 404
    db.session.delete(node)
    db.session.commit()
    return jsonify({'message': 'Node deleted'})


@app.route('/simulate/communication', methods=['POST'])
def simulate_communication():
    online_nodes = Node.query.filter_by(is_online=True).all()
    
    if len(online_nodes) < 2:
        # Not enough online nodes
        return jsonify({'message': 'Not enough online nodes to simulate communication'}), 400
    
    try:
        # Simulate communication logic here...
        # For example, randomly select two nodes and simulate a message being sent from one to the other
        # This is just a placeholder logic
        sender, receiver = random.sample(online_nodes, 2)
        
        # Assuming you have a function to simulate sending a message
        # simulate_send_message(sender, receiver)
        
        return jsonify({'message': 'Communication simulated successfully', 'sender': sender.id, 'receiver': receiver.id}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

    # Fallback return, in case all else fails
    return jsonify({'message': 'Unexpected error occurred in simulating communication'}), 500


@app.route('/simulate/failure', methods=['POST'])
def simulate_failure():
    # Simulate failure logic here
    return jsonify({'message': 'Failure simulation not implemented'})

@app.route('/simulate/recovery', methods=['POST'])
def simulate_recovery():
    # Simulate recovery logic here
    return jsonify({'message': 'Recovery simulation not implemented'})


# # Configure the SQLAlchemy part
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://simulator_user:rootshubh@localhost/distributed_systems_simulator'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Node(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     status = db.Column(db.String(80), nullable=False)
#     load = db.Column(db.Integer, nullable=False)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True)

# Runs the app in debug mode, which is helpful during development as it will reload the app for you upon changes.
# if __name__ == '__main__':
#     app.run(debug=True)