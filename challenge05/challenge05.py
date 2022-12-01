import math
import json


def solve(keys_list):
    while len(keys_list) > 1:
        num_kills = math.ceil(len(keys_list)/2)
        index = 0 # Start to 0 index
        while num_kills > 0:
            neighbor = (index+1) % len(keys_list)
            keys_list.remove(keys_list[neighbor]) # Remove right neighbor
            index += 1
            num_kills -= 1

    return keys_list[0]


def tests():
    list_tests = [
        {
            'input': list(range(0, 10)),
            'output': 4
        },
    ]

    test_result = []
    
    for test in list_tests:
        solution = solve(test['input'])
        test_result.append(solution == test['output'])
        print('Solution: {}, Expected: {}'.format(solution, test['output']))
    
    return sum(test_result) == len(list_tests)


if __name__=='__main__':
    print('Init tests')
    passed = tests()
    print('End tests\n')

    if not passed:
        print('Try again please')
    else:
        users_dict = None
        with open('mecenas.json', 'r') as content:
            users_dict = json.loads(content.read())
        
        solution = solve(list(range(len(users_dict))))
        print('Solution: {}-{}'.format(users_dict[solution], solution))
