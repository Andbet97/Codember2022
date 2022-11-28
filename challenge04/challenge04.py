

def solve(range_numbers):
    solutions = []
    for i in range_numbers:
        password = str(i)
        if len(password) != 5 or password.count('5') < 2:
            continue
        a, b, c, d, e = password
        if (a > b) or (b > c) or (c > d) or (d > e):
            continue
        
        solutions.append(i)

    return solutions


def tests():
    list_tests = [
        {
            'input': range(55678, 55678+1),
            'output': [55678]
        },
        {
            'input': range(12555, 12555+1),
            'output': [12555]
        },
        {
            'input': range(55555, 55555+1),
            'output': [55555]
        },
        {
            'input': range(12345, 12345+1),
            'output': []
        },
        {
            'input': range(57775, 57775+1),
            'output': []
        },
    ]

    test_result = []
    
    for test in list_tests:
        solution = solve(test['input'])
        test_result.append(solution == test['output'])
        print('Solution: {}, Expected: {}'.format(solution, test['output']))
    
    return sum(test_result) == len(list_tests)


if __name__=="__main__":
    print('Init tests')
    passed = tests()
    print('End tests\n')

    if not passed:
        print('Try again please')
    else:
        range_numbers = range(11098, 98124) # 11098-98123
        solution = solve(range_numbers)
        password = solution[55] if len(solution) > 56 else ''
        print('Solution: {}-{}'.format(len(solution), password))
