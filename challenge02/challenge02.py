

def solve(encrypted_code):    
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

    return prayer


def tests():
    list_tests = [
        {
            'input': "109105100117",
            'output': 'midu'
        },
        {
            'input': "9911110010110998101114",
            'output': 'codember'
        },
        {
            'input': "9911110010110998101114 109105100117",
            'output': 'codember midu'
        },
        {
            'input': "11210897121 116101116114105115",
            'output': 'play tetris'
        }
    ]

    test_result = []
    
    for test in list_tests:
        solution = solve(test['input'])
        expected = test['output']
        test_result.append(solution == expected)
        print('Solution: {}, Expected: {}'.format(solution, expected))
    
    return sum(test_result) == len(list_tests)


if __name__=="__main__":
    print('Init tests')
    passed = tests()
    print('End tests\n')

    if not passed:
        print('Try again please')
    else:
        encrypted_code = ''
        with open("encrypted.txt", "r") as content:
            encrypted_code = content.read()
        print('Solution: {}'.format(solve(encrypted_code[:-1])))
