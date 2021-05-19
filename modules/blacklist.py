from unicodedata import normalize

class Blacklist:
    
    def __init__(self, message):
        self.content = normalize('NFKD' ,message.content.lower()).encode('ASCII', 'ignore').decode('ASCII')
        self.message = message
        
        #Get words from blacklist.txt
        file = open("./blacklist/blacklist.txt", 'r')    
        self.words = file.read().strip().lower().split(', ')
        file.close()
    
    def verify(self):
        swearWords = 0
        
        #Verify words 
        for word in self.words:
            if self.content.find(word) != -1:
                swearWords += 1
        
        return swearWords
                
