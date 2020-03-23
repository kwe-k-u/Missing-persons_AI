import requests
r = requests.get("https://sellercenter-api.jumia.com.gh/?Action=GetProducts&Filter=all&Format=JSON&Timestamp=2020-02-24T08%3A40%3A16%2B00%3A00&UserID=kwekuaacquaye%40gmail.com&Version=1.0&Signature=a7f869f7321f4cffd3b90687797eeba58e61a57cbcec80baa247467a427ed123")
import json
r = json.loads(r.text)
import pprint
a = pprint.pprint(r)
print(a)


 #dic =json.dumps(dic_var)