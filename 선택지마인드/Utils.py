import json

json_data = None

with open('./resource/story.json', 'r', encoding='utf8') as data:
    json_data = json.loads(data.read())

def getFirst(root, index):
    arr = ["", "", "", ""]
    text = str(json_data[root][index]['question'])
    
    if len(text) <= 55:
        arr.insert(0, text[:len(text)])
    elif len(text) > 55:
        string = text[((len(text) // 2)):(len(text))]
        location = string.index(' ')
        arr.insert(0, text[:(len(text) // 2)])
        arr.insert(1, string[:location] + string[location + 1:])
    return arr

def getFirstLen(root):
    return len(json_data[root]) - 1

def getChoice(root, index):
    arr = ["", ""]
    text = json_data[root][index]['choice']
    arr.insert(0, text[0])
    arr.insert(1, text[1])

    return arr

def isFinish(root, index):
    if str(json_data[root][index]['question'][1]) == 'finish':
        return True
    else:
        return False


                                      
    

