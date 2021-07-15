import json #import library
#str_ = '{"home": {"player":{"username": "tester","age": 21,"winningNumbers": [21,47,55]}}}'

str_ = str(input()) #input for json, test
dict_ = json.loads(str_) #json to dict

class Model: #main model
    class home:
        class player:
            def __init__(self, username, age, winningNumbers):
                self.username = username
                self.age = age
                self.winningNumbers = winningNumbers

Model.home.player(dict_['home']['player']['username'], dict_['home']['player']['age'], dict_['home']['player']['winningNumbers']) #dict to model

#json > dict > model