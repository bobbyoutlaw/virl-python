import json, sys, http.client

conn = http.client.HTTPConnection("172.16.1.25:19399")

headers = {
    'authorization': "Basic Z3Vlc3Q6Z3Vlc3Q=",
    'cache-control': "no-cache",
    'postman-token': "4a45f813-a94d-77cb-8623-f944a5ee0c34"
    }

conn.request("GET", "/simengine/rest/interfaces/automation-test1-rFAJNF", headers=headers)
strResponse = conn.getresponse()


strData = strResponse.read()
routerData = strData.decode("utf-8")
routerDict = json.loads(routerData)

routerList = list(routerDict.values())


for strTemp in routerList:
 routerString = strTemp

for strRouterName,interfaces in iter(routerString.items()):
    verifyIPAddress = interfaces['management']['ip-address']
    while verifyIPAddress != "None":
        print(strRouterName,interfaces['management']['ip-address'])
        verifyIPAddress = "None"
