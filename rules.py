import rule

rule.Rule(lambda entry : entry["MESSAGE"] == "Failed password" , "Failed Login Attempt", "A login attempt was made on the server and was denied")
rule.simpleRule("testtesttest", "test message", "test message triggered")
