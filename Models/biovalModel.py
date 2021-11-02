def getBiovalJson(row):
    obj = {}
    obj["B_id"]=row[0]
    obj["S_id"]=row[1]
    obj["L_id"]=row[2]
    obj["heartrate"]=row[3]
    obj["ecg"]=row[4]
    obj["temprature"]=row[5]
    obj["healthy"]=row[6]
    return obj

def parseBiovalTable(records):
    response = []
    for row in records:
        obj = getBiovalJson(row)
        response.append(obj)
    return response

def insertBiovalValue(mysql,args):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO binfo VALUES(%s,%s,%s,%s,%s,%s,%s)',(args["B_id"],args["S_id"],args["L_id"],str(args["heartrate"]),"-1",str(args["temprature"]),str(args["healthy"])))
    mysql.connection.commit()
    cur.close()

def updateBiovalValue(mysql,args):
    cur = mysql.connection.cursor()
    #UPDATE tablename SET col1 = 'val1', col2 = 'val2' WHERE id = id_value
    print("Executing Query")
    #query = 'UPDATE binfo SET heartrate = %s,temprature=%s,healthy=%s WHERE B_id = "%s";'

    res = cur.execute('UPDATE binfo SET heartrate = %s,temprature=%s,healthy=%s WHERE B_id = %s;',(int(args["heartrate"]),int(args["temprature"]),int(args["healthy"]),str(args["B_id"])))
    print(res)
    print("Query Executed")
    mysql.connection.commit()   
    cur.close()
     
