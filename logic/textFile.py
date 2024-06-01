class TextFile():
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
        f = open('./resource/text/default2.txt', 'r')
        self.text_list = f.readlines()

    def getText(self):
        return self.text_list