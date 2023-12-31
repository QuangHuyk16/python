import json

# Chuỗi JSON
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Chuyển đổi chuỗi JSON thành đối tượng Python
data = json.loads(json_string)

# In dữ liệu
print(data)
