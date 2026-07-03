from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample users
users = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22}
]

# Home Page
@app.route('/')
def home():
    return "Welcome to the Flask REST API!"

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET one user
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    for user in users:
        if user["id"] == id:
            return jsonify(user)
    return jsonify({"message": "User not found"}), 404

# POST new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "age": data["age"]
    }

    users.append(new_user)

    return jsonify(new_user), 201

# PUT update user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    for user in users:
        if user["id"] == id:
            user["name"] = data["name"]
            user["age"] = data["age"]
            return jsonify(user)

    return jsonify({"message": "User not found"}), 404

# DELETE user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return jsonify({"message": "User deleted successfully"})

    return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)