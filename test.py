import json
with open('./database/users.json', 'r') as f:
    data = json.load(f)

cu = "Yash Giri"


def getTodos(d):
    return d['todos']

def getTodoAuthor(d):
    return(d["author"])

def getTodoCreated(d):
    return(d["created"])

def getTodoList(d):
    return(d["list"])

def addItemToList(index, value)

for x in range(0, len(data)):
    if(data[x]["name"]== cu):
        l = getTodos(data[x])
        for x in l:
            print(getTodoList(x))