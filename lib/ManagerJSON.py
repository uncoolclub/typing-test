import json
import os 

class ManagerJSON:
    file_path = ""
    data = {}
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            self.createJSON(file_path)
        else:
            self.readJSON(file_path)

    def readJSON(self, file_path, _encoding = "UTF-8"):
        self.file_path = file_path
        with open(self.file_path, 'rw', encoding=_encoding) as file:
            self.data = json.load(file)
         
    def createJSON(self, file_path, _encoding = "UTF-8"):
        self.file_path = file_path
        with open(file_path, 'w', encoding=_encoding) as file:
            json.dump({}, file, indent=4)
    
    def appendJSON(self, Info):
        self.data.append(Info)
        self.saveJSON()

    def saveJSON(self, _encoding = "UTF-8"):
        with open(self.file_path, 'w', encoding=_encoding) as file:
            json.dump(self.data, file, indent=4)
    
    
    def setData(self, key, value):
        self.data[key] = value

    def getData(self, key):
        return self.data[key]