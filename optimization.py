def bf_optimize(code: str):
    new_code = ''
    index = 0
    while index < len(code):
        character = code[index]
        if character in '+-':
            num_plus = 0
            while True:
                if index >= len(code):
                    break
                character = code[index]
                if character not in '+-':
                    break
                if character == '+':
                    num_plus += 1
                else:
                    num_plus -= 1
                index += 1
            if num_plus != 0:
                if num_plus < 0:
                    for i in range((num_plus**2)**0.5):
                        new_code += '-'
                else:
                    for i in range(num_plus):
                        new_code += '+'
        else:
            new_code += character
            index += 1
    new_code = new_code.replace('**', '*')

    return new_code

def c_optimize(c_code: str):
    lines = c_code.split('\n')
    index = 0

    new_lines = []

    while index < len(lines):
        part = lines[index]
        if part in ['memory[cursor]++;', 'memory[cursor]--;', 'SUBTRACT_CURSOR();', 'ADD_CURSOR();']:
            n = -1
            part2 = part
            while True:
                part2 = lines[index]
                if part2 != part:
                    break
                index += 1
                n += 1

            if part == 'memory[cursor]++;':
                new_lines.append('memory[cursor]+=' + str(n+1) + ';')
            elif part == 'memory[cursor]--;':
                new_lines.append('memory[cursor]-=' + str(n+2) + ';')
            elif part in ['ADD_CURSOR();', 'SUBTRACT_CURSOR();']:
                new_lines.append(f'for(int i=0;i<{n+1};i++)')
                new_lines.append(part)
        elif part in ['ADD_CURSOR();', 'SUBTRACT_CURSOR();']:
            n = 1
            part2 = part
            while True:
                n += 1
        else:
            new_lines.append(part)
            index += 1
    
    c_code = '\n'.join(new_lines)

    #c_code = c_code.replace('memory[cursor]++;\nmemory[cursor]++;', 'memory[cursor]+=2;')
    #c_code = c_code.replace('memory[cursor]--;\nmemory[cursor]--;', 'memory[cursor]-=2;')
    return c_code
