import os

def get_number_file(path):
    file_list=os.listdir(path)
    return len(file_list)


# path='./static/Detect/'
# number=get_number_file(path)
# print("number:",number)