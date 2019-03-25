class Rule:
    rules = []
    def __init__(self, trigger, subject, message, additionalAction=None):
        Rule.rules.append(self)
        self.trigger = trigger
        self.subject = subject
        self.message = message
        self.additionalAction = None 

    def test(self, logEntry):
        return self.trigger(logEntry)

class simpleRule:
    def __init__(self, triggerText, subject, message):
        Rule(lambda entry : entry["MESSAGE"] == triggerText, subject, message)

def getRules():
    return rules