# ASCII encoded file 3
# This file uses ASCII encoding only
class ASCIIProcessor3:
    def __init__(self):
        self.ascii_chars = "Hello World"
    
    def process_ascii(self, text):
        return text.encode('ascii').decode('ascii')
