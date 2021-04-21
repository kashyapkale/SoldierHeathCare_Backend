def getBiovalJson(row):
    obj = {}
    obj["B_id"]=row[0]
    obj["S_id"]=row[1]
    obj["L_id"]=row[2]
    obj["heartrate"]=row[3]
    obj["spo2"]=row[4]
    obj["ecg"]=row[5]
    obj["temprature"]=row[6]
    return obj

def parseBiovalTable(records):
    response = {}
    for row in records:
        obj = getBiovalJson(row)
        response[row[0]] = obj
    return response

def insertBiovalValue(mysql,args):
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO binfo VALUES(%s,%s,%s,%s,%s,%s,%s)',(args["B_id"],args["S_id"],args["L_id"],str(args["heartrate"]),str(args["spo2"]),"-1",str(args["temprature"])))
    mysql.connection.commit()
    cur.close()