def bf_optimize(code: str):
    code = code.replace('+-', '')
    code = code.replace('-+', '')
    code = code.replace('**', '*')

    return code

def c_optimize(c_code: str):
    c_code = c_code.replace('memory[cursor]++;\nmemory[cursor]++;', 'memory[cursor]+=2;')
    c_code = c_code.replace('memory[cursor]--;\nmemory[cursor]--;', 'memory[cursor]-=2;')
    return c_code
