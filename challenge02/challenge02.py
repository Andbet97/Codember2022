

def solve():
    encrypted_code = ''
    with open("encrypted.txt", "r") as content:
        encrypted_code = content.read()
    
    prayer = ''
    for encrypted_word in encrypted_code.split(' '):
        word = ''
        index = 0
        while index < len(encrypted_word):
            # Only minus ASCII (97-122)
            # If ASCII start with 9 (97-99) count 2, else (100-122), count 3
            len_ascii = 2 if encrypted_word[index] == '9' else 3
            word += chr(int(encrypted_word[index:index+len_ascii]))
            index += len_ascii
        prayer += "{} ".format(word)
    prayer = prayer[:-1] # Because last character are " "

    print(prayer)


if __name__=="__main__":
    solve()
