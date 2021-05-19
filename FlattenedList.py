# Python Program to Make a Flattened List from Nested List

nested_list = [1,[2,3,4],['check'],['a','b'],5,'c','himanshu']

flat_list = []

for item in nested_list:
    if type(item) == list:
        for value in item:
            flat_list.append(value)
    else:
        flat_list.append(item)

print(flat_list)
            
    
