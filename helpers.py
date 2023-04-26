import json

def create_user(name, password):
    with open('./database/authentication.json', 'r+') as f:
        data = json.load(f)
        val = {
            name:{
                'password':password
            }
        }
        data[name] = {"password":password}
        f.seek(0)
        json.dump(data,f, indent=4)
    print(val)

def validate_signup(name, password):
    if(len(name) > 0 and len(password)>0):
        with open('./database/authentication.json', 'r') as f:
            data = json.load(f)
        try:
            data[name]
        except:
            return(True)
        return False
    return False

def validate_login(name, password):
    if(len(name) > 0 and len(password)>0):
        with open('./database/authentication.json', 'r') as f:
            data = json.load(f)
        try:
            data[name]
        except:
            return(False)
        return True
    return False


