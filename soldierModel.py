def getSoldierJson(row):
    obj = {}
    obj["S_id"]=row[0]
    obj["FirstName"]=row[1]
    obj["LastName"]=row[2]
    obj["age"]=row[3]
    obj["L_id"]=row[4]
    return obj

def parseSoldierTable(records):
    response = {}
    for row in records:
        obj = getSoldierJson(row)
        response[row[0]] = obj
    return response

def insertSoldierValue(mysql,args):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO sinfo VALUES(%s,%s,%s,%s,%s)',(args["S_id"],args["FirstName"],args["LastName"],str(args["age"]),args["L_id"]))
    mysql.connection.commit()
    cur.close()