import rule

def badLoginCheck(entry):
    if "Failed password" in entry["MESSAGE"]:
        return True
    if "Disconnected from authenticating user" and "preauth" in str(entry):
        return True
    return False

rule.Rule(badLoginCheck, "Failed Login Attempt", "A login attempt was made on the server and was denied", additionalAction=lambda : "TODO: add whois here" )
rule.simpleRule("testtesttest", "test message", "test message triggered")
#rule.Rule(lambda entry : "Disconnected from authenticating user" and "preauth" in str(entry), "Login attempt detected", "A login attempt has been recorded on the server")



