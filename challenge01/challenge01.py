

def separe_data(list_data):
    list_keys = []
    list_values = []

    for data in list_data:
        key, value = data.split(':')
        list_keys.append(key)
        list_values.append(value)

    return list_keys, list_values


def solve():
    users_data = []
    users_valid = 0
    user_name = ''

    user_keys = ["usr","eme","psw","age","loc","fll"]

    with open("users.txt", "r") as inputs:
        user = ""
        for line in inputs:
            if line == "\n":
                users_data.append(user)
                user = ""
                continue
            user += line.replace("\n", " ")
    
    for row in users_data:
        list_data = row.split(' ')[:-1] # because last character are " "
        list_keys, list_values = separe_data(list_data)
        valid_user = len(user_keys) == sum([e in list_keys for e in user_keys])
        if valid_user:
            users_valid += 1
            user_name = list_values[list_keys.index('usr')]
    
    print("{}{}".format(users_valid, user_name))        

 
if __name__=="__main__":
    solve()
