import json

def authentication(user,password):
    with open('db.json') as db:
        data = json.load(db)
        result = False
        userFound = False
        i = 0
        while (userFound == False and i < len(data)):
            if (user == data[i]['user']):
                userFound = True
                if (password == data[i]['password']):
                    result = True
            i = i + 1
        return result