from leaderModel import *
from soldierModel import *
from ReqParser import *
from db_sql import *
from biovalModel import *
from config import *
from flask import Flask,jsonify,request
from flask_restful import Api
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/soldiers": {"origins": "*"}})

app.config['MYSQL_HOST'] = db_host
app.config['MYSQL_USER'] = db_user
app.config['MYSQL_PASSWORD'] = db_password
app.config['MYSQL_DB'] = db_name

mysql = MySQL(app)

bioval_put_args = parseBiovals()
soldier_put_args = parseSoldierInfo()
leader_put_args = parseLeaderInfo()

soldiers = varSoldiers()
biovals = varBiovals()
leaders = {
    0:{"Name" : "Samshaw","S_id" : "045","l_id":"045"},
}


#Soldier API Endpoints
@app.route('/soldiers')
def getAllSoldiers():
    try:
        query = 'SELECT * FROM sinfo'
        records = getTable(mysql,query,())
        return jsonify(parseSoldierTable(records))
    except:
        return jsonify("error")

@app.route('/soldier/<string:id>',methods=['PUT','GET'])
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
def getAllBiovals():
    try:
        query = 'SELECT * FROM binfo'
        records = getTable(mysql,query,())
        return jsonify(parseBiovalTable(records))
    except:
        return jsonify("error")

@app.route('/health/<string:id>',methods=['PUT','GET'])
def getBioValue(id):
    if (request.method == 'PUT'):
        args = bioval_put_args.parse_args()
        #args = reqparse.RequestParser().parse_args()
        try:
            insertBiovalValue(mysql,args)
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
def getAllLeaders():
    try:
        query = 'SELECT * FROM linfo'
        records = getTable(mysql,query,())
        return jsonify(parseLeaderTable(records))
    except:
        return jsonify("error")

@app.route('/leader/<string:id>',methods=['PUT','GET'])
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


#api.add_resource(basicRequests,"/soldier/<int:id>")
#api.add_resource(basicRequests,"/soldier")


if __name__ == "__main__":
	app.run(debug=True)