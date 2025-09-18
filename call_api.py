import requests


# res = requests.get("http://localhost:6688/")
# print(res.status_code, res.json())

# res = requests.get("http://localhost:6688/hello/Giang")
# print(res.status_code, res.json())


url1 = "http://localhost:6688/hello"
payload1 = {"name":"Duong Giang"}


url2 = "http://localhost:6688/get"
payload2 = {
    "name":"Giang", 
    "age": 22, 
    "country": "Việt Nam",
            }

#res = requests.post(url2, json=payload2)
#print(res.status_code, res.json())

url3 = "http://localhost:6688/items/"
payload3 = {
    "name": "GẠO",
    "description": "Gạo ST25 xuất khẩu nhiều nước",
    "price":26.500,
    "tax":2.600
}

res = requests.post(url3, json=payload3)

print(res.status_code, res.json())