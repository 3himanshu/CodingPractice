# Python Program to Split a List Into Evenly Sized Chunks using yield

def split(lst,chunk):
    for i in range(0, len(lst), chunk):
        yield lst[i: i + chunk]

chunk_size = 2
my_lst = [1,2,3,4,5,6,7,8,9]

print(list(split(my_lst,chunk_size)))
