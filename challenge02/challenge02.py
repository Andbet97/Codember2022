

def solve():
    encrypted_code = ''
    with open("encrypted.txt", "r") as content:
        encrypted_code = content.read()
    
    oration = ''
    for encrypted_word in encrypted_code.split(' '):
        word = ''
        index = 0
        while index < len(encrypted_word):
            len_ascii = 2 if encrypted_word[index] == '9' else 3
            word += chr(int(encrypted_word[index:index+len_ascii]))
            index += len_ascii
        oration += "{} ".format(word)
    oration = oration[:-1] # because last character are " "

    print(oration)


if __name__=="__main__":
    solve()
