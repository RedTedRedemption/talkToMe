class Rule:
    rules = []
    def __init__(self, triggerText, subject, message):
        Rule.rules.append(self)
        self.triggerText = triggerText
        self.subject = subject
        self.message = message

    def test(self, logEntry):
        print("testing %s" % logEntry)

        try:
            logEntry.index(self.triggerText)
        except ValueError:
            print("not found")
            return False
        else:
            print("found")
            return True 

        return False

def getRules():
    return rules
