list_of_dics = [{"key": 10}, {"key1": 10}, {"key2": 10}]
print(list(list_of_dics[2].keys())[0])

for index in range(len(list_of_dics)):
    if list(list_of_dics[index].keys())[0] == "key2":
        print("YAAAY")


for item in list_of_dics:
    a = list(item.keys())[0]
    print(a)

print(list_of_dics[1]["key1"])