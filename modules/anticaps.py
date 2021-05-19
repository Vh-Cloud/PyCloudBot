import re

class AntiCaps:
    
    def __init__(self, msg):
        mention = re.sub('[a-zA-Z]', '', msg)
        self.msg = msg.replace(mention, '')
    
    def analyse(self):
        caps = 0
        noCaps = 0
        
        for word in self.msg:
            if word.isupper():
                caps += 1
            
            elif word.islower():
                noCaps += 1
        
        if caps > noCaps:
            return True
        
        else:
            return False
        