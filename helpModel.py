def getHelpJson(row):
    obj = {}
    obj["FirstName"]=row[1]
    obj["LastName"]=row[2]
    obj["S_id"]=row[0]
    obj["age"]=row[3]
    obj["L_id"]=row[4]
    obj["Help"]=row[5]
    return obj

def parseHelpTable(records):
    response = []
    for row in records:
        obj = getHelpJson(row)
        response.append(obj)
    return response

def insertHelpValue(mysql,args):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO help_info VALUES(%s,%s,%s,%s,%s)',(args["FirstName"],args["LastName"],args["S_id"],str(args["age"]),args["L_id"],"In Progress"))
    mysql.connection.commit()
    cur.close()