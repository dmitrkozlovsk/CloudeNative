from flask import Flask, jsonify
import json
import sqlite3

app = Flask(__name__)

@app.route("/api/v1/info")
def home_index():
    conn = sqlite3.connect('homeapp.db')
    print ('ВD connected')
    api_list = []
    cursor = conn.execute("SELECT builddtime, version,\
            methods, links FROM apirelease")
    for row in cursor:
        a_dict = {}
        a_dict['verion'] = row[0]
        a_dict['builddtime'] = row[1]
        a_dict['methods'] = row[2]
        a_dict['links'] = row[3]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'api_version': api_list}), 200

def user_list():
    conn = sqlite3.connect('homeapp.db')
    print ('ВD connected')
    api_list = []
    cursor = conn.execute("SELECT username, full_name,\
            email, password, id FROM users")
    for row in cursor:
        a_dict = {}
        a_dict['username'] = row[0]
        a_dict['full_name'] = row[1]
        a_dict['email'] = row[2]
        a_dict['password'] = row[3]
        a_dict['id'] = row[4]
        api_list.append(a_dict)
    conn.close()
    return jsonify({'user_list':api_list}), 200

@app.route("/api/v1/users")
def get_users():
    return user_list()

def list_user(user_id):
    conn = sqlite3.connect('homeapp.db')
    print ('ВD connected')
    cursor = conn.execute(f"SELECT * FROM users WHERE id={user_id}")
    data = cursor.fetchall()
    if len(data) != 0:
        data = data[0]
        user = {}
        user['username'] = data[0]
        user['full_name'] = data[1]
        user['email'] = data[2]
        user['password'] = data[3]
        user['id'] = data[4]
        conn.close()
        return jsonify(user)
 
@app.route("/api/v1/users/<int:user_id>", methods = ['GET'])
def get_user(user_id):
    return list_user(user_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
