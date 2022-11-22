import json


def solve(list_colors):
    zebra = [list_colors[0]]
    counter = 0
    last_color = None

    for color in list_colors:
        if len(zebra) == 1 and zebra[0] == color:
            continue
        if len(zebra) < 2 or zebra[-2] == color:
            zebra.append(color)
            continue

        counter, last_color = [len(zebra), zebra[-1]] if len(zebra) >= counter else [counter, last_color]
        zebra = [zebra[-1], color]
    
    counter, last_color = [len(zebra), zebra[-1]] if len(zebra) >= counter else [counter, last_color]
    
    return '{}@{}'.format(counter, last_color)


def tests():
    list_tests = [
        {
            'input': ["red", "blue", "red", "blue", "green"],
            'output': [4, "blue"]
        },
        {
            'input': ["green", "red", "blue", "gray"],
            'output': [2, "gray"]
        },
        {
            'input': ["blue", "blue", "blue", "blue"],
            'output': [1, "blue"]
        },
        {
            'input': ["red", "green", "red", "green", "red", "green"],
            'output': [6, "green"],
        },
        {
            'input': ["blue", "red", "blue", "red", "gray"],
            'output': [4, "red"]
        },
        {
            'input': ["red", "red", "blue", "red", "red", "red", "green"],
            'output': [3, "red"],
        },
        {
            'input': ["red", "blue", "red", "green", "red", "green", "red", "green"],
            'output': [6, "green"],
        },
    ]

    test_result = []
    
    for test in list_tests:
        solution = solve(test['input'])
        expected = '{}@{}'.format(test['output'][0], test['output'][1])
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
        text_list_colors = ''
        with open("colors.txt", "r") as content:
            text_list_colors = content.read()
        
        list_colors = json.loads(text_list_colors)
        print('Solution: {}'.format(solve(list_colors)))
