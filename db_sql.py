from flask_mysqldb import MySQL

def getTable(mysql,query,parameters):
    print("Entering getTable")
    cur = mysql.connection.cursor()
    if parameters == ():
        print("Entering Empty Parameter")	
        cur.execute(query)
        print("Exiting Empty Parameter")
    else:
        print("Entering Non-Empty Parameter")
        print(cur.execute(query,parameters))
        #cur.execute(query,parameters)
        print("Exiting Non-Empty Parameter")
        
    records = cur.fetchall()
    return records


