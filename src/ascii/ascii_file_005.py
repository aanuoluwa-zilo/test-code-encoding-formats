# ASCII encoded file 5
# This file uses ASCII encoding only
class ASCIIProcessor5:
    def __init__(self):
        self.ascii_chars = "Hello World"
    
    def process_ascii(self, text):
        return text.encode('ascii').decode('ascii')
