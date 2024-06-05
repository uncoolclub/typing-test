class Text():
    file_path = ""
    file_name = ""
    text_list = []

    def __init__(self, file_path):
        self.readText(file_path)

    def readText(self, file_path, _encoding="UTF-8"):
        self.file_path = file_path

        part = file_path.split("/")
        self.file_name = part[-1].split(".")[0]
        
        self.text_list = []
        with open(file_path, 'r', encoding=_encoding) as file:
            self.text_list.append(file.readlines())

    def getTextName(self):
        return self.text_name
    
    def getText(self):
        return self.text_list
    
    def saveText(self, _encoding = "UTF-8"):
        with open(self.file_path, 'w', encoding=_encoding) as file:
            for line in self.text_list:
                file.write(line + '\n')
