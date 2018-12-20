import sys
from time import sleep
import urllib.request
import json
import ast

class Thingspeak:
    def __init__(self, write_key, read_key):
        self.write_key = write_key
        self.read_key = read_key
        temp = self.read(1)
        self.id = temp['channel']['id']
        self.name = temp['channel']['name']
        self.num_field = len(temp['channel'])-8

    def write(self, field, data):
        url = "https://api.thingspeak.com/update?api_key={}&field{}={}".format(self.write_key, str(field), str(data))
        rtn = urllib.request.urlopen(url)
        return 1
    
    def read(self, _range):
        url = "https://api.thingspeak.com/channels/628897/feeds.json?api_key={}&results={}".format(self.read_key, str(_range))
        rtn = urllib.request.urlopen(url).read()
        return ast.literal_eval(str(rtn)[2:len(str(rtn))-1].replace('null',"\"\""))
    
    def get_field(self, field, result):
        url = "https://api.thingspeak.com/channels/628897/fields/{}.json?api_key={}&results={}".format(field, self.read_key, result)
        rtn = urllib.request.urlopen(url).read()
        return rtn

    def get_data(self):
        temp = self.read(1)['feeds'][0]
        del temp['entry_id']
        return temp


if __name__ == "__main__":
    testt = Thingspeak("VEMUS670D5ZP2OLN", "5LT3QPFMB8XPVWEF")
    print (testt.get_data())
  
