from flask_mysqldb import MySQL

def getTable(mysql,query,parameters):
    cur = mysql.connection.cursor()
    if parameters == ():	
        cur.execute(query)
    else:
        cur.execute(query,parameters)
    records = cur.fetchall()
    return records


