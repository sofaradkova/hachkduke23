
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'PennyPro'
app.config['MONGO_URI'] = 'mongodb+srv://admin:password12321@cluster0.ssegjcs.mongodb.net/'
app.config['SECRET_KEY'] = 'secretkey'

mongo = PyMongo(app)

@app.route('/')
def _index():
    return render_template('index.html')

@app.route('/api/data/findUser/<username>')
def _findUser(username):
    user = mongo.db.users.find_one({'username':username})
    if user:
        return jsonify({'result':True})
    else:
        return jsonify({'result':False})
    
@app.route('/api/data/addUser/<username>/<password>', methods=['POST'])
def _addUser(username,password):
    user = mongo.db.users.find_one({'username':username})
    if user:
        return jsonify({'result':False})
    else:
        mongo.db.users.insert({'username':username,'password':password})
        return jsonify({'result':True})

@app.route('/dashboard')
def _dashboard():    
    return render_template('dashboard.html')



    

        
        
def main():
   app.run(debug=True,port=8000)
main()