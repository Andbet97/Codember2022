

def solve(encrypted_code):    
    prayer = ''
    for encrypted_word in encrypted_code.split(' '):
        word = ''
        index = 0
        while index < len(encrypted_word):
            # Only minus ASCII (97-122)
            # If ASCII start with 9 (97-99) count 2, else (100-122), count 3
            len_ascii = 3 if encrypted_word[index] == '1' else 2
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
    
        # Secret email
        print('\nSecret Mail.')
        subject = "115111109111115 108101103105111110"
        message = "83101 113117105101110 101114101115 84101 9911111011112299111 84117 110111 109101 9911111011199101115 97 109105 84101 101115116111121 1119811510111411897110100111 84101 101115116111121 115105103117105101110100111 81117105101114101115 10611710397114 7411710110397 99111110109105103111 8697108101 8697109111115 97 10611710397114 691061019911711697 101115116101 9911110997110100111 101110 10897 11610111410910511097108 11511798109105116 116561181061045651505752561029911097108"

        print('Subject: {}\nMessage: {}'.format(solve(subject), solve(message)))
