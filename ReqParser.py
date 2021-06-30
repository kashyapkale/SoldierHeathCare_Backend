from flask_restful import reqparse



def parseBiovals():
    bioval_put_args = reqparse.RequestParser()
    bioval_put_args.add_argument("L_id", type=str, help="l_id on the video", required=True)
    bioval_put_args.add_argument("S_id", type=str, help="s_id is required", required=True)
    bioval_put_args.add_argument("B_id", type=str, help="B_id is required", required=True)
    bioval_put_args.add_argument("heartrate", type=int, help="heartrate is required", required=True)
    bioval_put_args.add_argument("temprature", type=int, help="temprature is required", required=True)
    bioval_put_args.add_argument("healthy", type=int, help="Healthy is required", required=True)
    return bioval_put_args

def parseSoldierInfo():
    soldier_put_args = reqparse.RequestParser()
    soldier_put_args.add_argument("FirstName", type=str, help="Name  is required", required=True)
    soldier_put_args.add_argument("LastName", type=str, help="Name  is required", required=True)
    soldier_put_args.add_argument("S_id", type=str, help="s_id is required", required=True)
    soldier_put_args.add_argument("age", type=int, help="s_id is required", required=True)
    soldier_put_args.add_argument("L_id", type=str, help="Likes on the video", required=True)
    return soldier_put_args

def parseLeaderInfo():
    leader_put_args = reqparse.RequestParser()
    leader_put_args.add_argument("FirstName", type=str, help="Name  is required", required=True)
    leader_put_args.add_argument("LastName", type=str, help="Name  is required", required=True)
    leader_put_args.add_argument("S_id", type=str, help="s_id is required", required=True)
    leader_put_args.add_argument("age", type=int, help="s_id is required", required=True)
    leader_put_args.add_argument("L_id", type=str, help="Likes on the video", required=True)
    return leader_put_args

def parseHelpInfo():
    help_put_args = reqparse.RequestParser()
    help_put_args.add_argument("FirstName", type=str, help="Name  is required", required=True)
    help_put_args.add_argument("LastName", type=str, help="Name  is required", required=True)
    help_put_args.add_argument("S_id", type=str, help="s_id is required", required=True)
    help_put_args.add_argument("age", type=int, help="s_id is required", required=True)
    help_put_args.add_argument("L_id", type=str, help="Likes on the video", required=True)
    return help_put_args



#____________________Unwanted Vars___________________

def varSoldiers():
    return {
    0:{"FirstName" : "Kashyap","LastName" : "Kale","age":22,"S_id" : "001","l_id":"045"},
    1:{"FirstName" : "Anuj","LastName" : "Kakade","age":21,"S_id" : "002","l_id":"045"},
    2:{"FirstName" : "Aarshee","LastName" : "Bhattacharya","age":21,"S_id" : "003","l_id":"045"},
    3:{"FirstName" : "Vaishnavi","LastName" : "Goyal","age":21,"S_id" : "004","l_id":"045"}
}

def varBiovals():
    return {
    0:{"B_id" : "000","S_id" : "001","l_id":"045","heartrate":84,"SPO2":99,"temprature":98},
    1:{"B_id" : "001","S_id" : "002","l_id":"045","heartrate":84,"SPO2":99,"temprature":98},
    2:{"B_id" : "002","S_id" : "003","l_id":"045","heartrate":84,"SPO2":99,"temprature":98},
    3:{"B_id" : "003","S_id" : "004","l_id":"045","heartrate":84,"SPO2":99,"temprature":98}
}