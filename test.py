import requests

BASE = "http://127.0.0.1:5000/"


data = [{"likes":10,'name':'tim','views':100000},
        {"likes":43,'name':'how ring','views':10030200},
        {"likes":123,'name':'joe','views':1000040}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())
