# NESTED DICTIONARY
dic1={"class":{"student":{"name":"xyz","marks":{"python":100,"web":90}}}}
A=(dic1["class"]["student"]["marks"]["python"])
print(A)
B=(dic1["class"]["student"]["marks"]["web"])
print(B)

# by get method
up=dic1.get("class",{}).get("student",{}).get("marks",{}).get("web")
print(up)