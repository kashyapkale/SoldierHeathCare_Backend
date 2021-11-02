from leaderModel import *
from soldierModel import *
from ReqParser import *
from db_sql import *
from biovalModel import *
from helpModel import *
from config import *
from flask import Flask, request, jsonify, make_response
import uuid
import jwt
from werkzeug.security import generate_password_hash, check_password_hash

import datetime
from functools import wraps
from flask_restful import Api
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
#Change datbase creds in config file*************************************************************
app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = db_name
app.config['SECRET_KEY'] = 'thisissecret'

mysql = MySQL(app)

user = "Admin"
password = "ABC123"

bioval_put_args = parseBiovals()
soldier_put_args = parseSoldierInfo()
leader_put_args = parseLeaderInfo()
help_put_args = parseHelpInfo()

soldiers = varSoldiers()
biovals = varBiovals()
leaders = {
    0:{"Name" : "Samshaw","S_id" : "045","l_id":"045"},
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401

         
        data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS512"])
        print(data)
        if data['public_id'] != user:
            return jsonify({'message' : 'Token is invalid!'}), 401

        return f(*args, **kwargs)

    return decorated



@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})


    if user != auth.username:
        return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

    if auth.password == password:
        token = jwt.encode({'public_id' : user, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'],algorithm="HS512")

        return jsonify({'token' : token})

    return make_response('Could not verify', 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'})

#Soldier API Endpoints
@app.route('/soldiers')
@token_required
def getAllSoldiers():
    try:
        query = 'SELECT * FROM sinfo'
        records = getTable(mysql,query,())
        return jsonify(parseSoldierTable(records))
    except:
        return jsonify("error")

@app.route('/soldier/<string:id>',methods=['PUT','GET'])
@token_required
def getSoldier(id):
    if (request.method == 'PUT'):
        print("Entering PUT Block")
        args = soldier_put_args.parse_args()
        try:
            print("Entering Try Block")
            insertSoldierValue(mysql,args)
            return jsonify("Success")
        except:
            return jsonify("Failure,Maybe Soldier Id is alredy present in the database")
        
    if (request.method == 'GET'):
        try:
            print("Entering try")
            query = 'SELECT * FROM sinfo WHERE S_id = %s'
            records = getTable(mysql,query,(id))
            print("Post query print")
            print(records)
            row = records[0]
            obj = getSoldierJson(row)
            return jsonify(obj) 
        except:
            return jsonify("Incorrect Soldier ID")


#Bioval API Endpoints
@app.route('/health/all')
@token_required
def getAllBiovals():
    try:
        query = 'SELECT * FROM binfo'
        records = getTable(mysql,query,())
        return jsonify(parseBiovalTable(records))
    except:
        return jsonify("error")

@app.route('/health/<string:id>',methods=['PUT','GET','POST'])
@token_required
def getBioValue(id):
    if (request.method == 'POST'):
        args = bioval_put_args.parse_args()
        try:
            insertBiovalValue(mysql,args)
            return jsonify("Success")
        except:
            return jsonify("Failure")
    
    if (request.method == 'PUT'):
        args = bioval_put_args.parse_args()
        #args = reqparse.RequestParser().parse_args()
        try:
            updateBiovalValue(mysql,args)
            return jsonify("Success")
        except:
            return jsonify("Failure")
    
    if (request.method == 'GET'):
        try:
            query = 'SELECT * FROM binfo WHERE S_id = %s'
            records = getTable(mysql,query,(id))
            row = records[0]
            obj = getBiovalJson(row)
            return jsonify(obj)
        except:
            return jsonify("Incorrect Bioval ID")

#Leader Api Endpoints
@app.route('/leader/all')
@token_required
def getAllLeaders():
    try:
        query = 'SELECT * FROM linfo'
        records = getTable(mysql,query,())
        return jsonify(parseLeaderTable(records))
    except:
        return jsonify("error")

@app.route('/leader/<string:id>',methods=['PUT','GET'])
@token_required
def getLeader(id):
    if (request.method == 'PUT'):
        args = leader_put_args.parse_args()
        try:
            insertLeaderValue(mysql,args)
            return jsonify("Success")
        except:
            return jsonify("Failure,Maybe Leader Id is alredy present in the database")
    
    if (request.method == 'GET'):
        try:
            query = 'SELECT * FROM linfo WHERE L_id = %s'
            records = getTable(mysql,query,(id))
            row = records[0]
            obj = getLeaderJson(row)
            return jsonify(obj)
        except:
            return jsonify("Incorrect Soldier ID")


#Help Table Api Endpoints
@app.route('/help/all')
@token_required
def getAllHelp():
    try:
        query = 'SELECT * FROM help_info'
        records = getTable(mysql,query,())
        return jsonify(parseHelpTable(records))
    except:
        return jsonify("error")

@app.route('/help/<string:id>',methods=['PUT','GET'])
@token_required
def getHelp(id):
    if (request.method == 'PUT'):
        args = help_put_args.parse_args()
        try:
            insertHelpValue(mysql,args)
            return jsonify("Success")
        except:
            return jsonify("Failure,Maybe Help Id is alredy present in the database")
    
    if (request.method == 'GET'):
        try:
            query = 'SELECT * FROM help_info WHERE S_id = %s'
            records = getTable(mysql,query,(id))
            row = records[0]
            obj = getHelpJson(row)
            return jsonify(obj)
        except:
            return jsonify("Incorrect Soldier ID")


#api.add_resource(basicRequests,"/soldier/<int:id>")
#api.add_resource(basicRequests,"/soldier")


if __name__ == "__main__":
	app.run(debug=True)
