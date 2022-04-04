
part = 2
syntax_errors = []
total = 0
scores = []


with open('input.txt', 'r') as fin:
    '''
    fin = ["[({(<(())[]>[[{[]{<()<>>",
            "[(()[<>])]({[<{<<[]>>(",
            "{([(<{}[<>[]}>{[]{[(<()>",
            "(((({<>}<{<{<>}{[]{[]{}",
            "[[<[([]))<([[{}[[()]]]",
            "[{[{({}]{}}([{[{{{}}([]",
            "{<[[]]>}<{[{[{[]{()[[[]",
            "[<(<(<(<{}))><([]([]()",
            "<{([([[(<>()){}]>(<<{{",
            "<{([{{}}[<[[[<>{}]]]>[]]"
            ]
    '''
    for i, line in enumerate(fin):
        stack = []
        for j, char in enumerate(line):
            if char in ['(', '{', '<', '[']:
                stack.append(char)
            if char == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    syntax_errors.append(char)
                    total +=3
                    break
            elif char == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    syntax_errors.append(char)
                    total +=57
                    break
            elif char == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    syntax_errors.append(char)
                    total += 1197
                    break
            elif char == '>':
                if stack[-1] == '<':
                    stack.pop()
                else:
                    syntax_errors.append(char)
                    total += 25137
                    break
        else:
            if len(stack) !=0:
                reverse_stack = []
                completion_score = 0
                for char in reversed(stack):
                    completion_score *= 5
                    if char in [')', '}', '>', ']']: 
                        print("????",stack)
                    if char == '(':
                        completion_score +=1
                    elif char == '[':
                        completion_score +=2
                    elif char == '{':
                        completion_score +=3
                    elif char == '<':
                        completion_score +=4
            print(stack, completion_score)
            scores.append(completion_score)

if part == 2:
    print(sorted(scores)[len(scores)//2])


if part == 1:
    print(syntax_errors)
    print(total)
