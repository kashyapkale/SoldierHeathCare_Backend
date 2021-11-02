def getLeaderJson(row):
    obj = {}
    obj["L_id"]=row[0]
    obj["FirstName"]=row[1]
    obj["LastName"]=row[2]
    obj["age"]=row[3]
    obj["S_id"]=row[4]
    return obj
                             
def parseLeaderTable(records):
    response = []
    for row in records:
        obj = getLeaderJson(row)
        response.append(obj)
    return response

def insertLeaderValue(mysql,args):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO linfo VALUES(%s,%s,%s,%s,%s)',(args["L_id"],args["FirstName"],args["LastName"],str(args["age"]),args["S_id"]))
    mysql.connection.commit()
    cur.close()
