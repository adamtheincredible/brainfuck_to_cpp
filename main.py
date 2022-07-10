from constants import *
from optimization import *

class interpreter:
    cursor: int = 0
    code = BODY

    def __init__(self, have_body: bool = True):
        if not have_body:
            self.code = ''
        self.have_body = have_body

    def interpret(self, code: str):
        # Before analyzing the code, it is optimized
        code = bf_optimize(code)

        index = 0
        while index < len(code):
            character = code[index]
            print(character)
            if character == '>':
                self.code += "ADD_CURSOR();\n"
            elif character == '<':
                self.code += "SUBTRACT_CURSOR();\n"
            elif character == '+':
                self.code += "memory[cursor]++;\n"
            elif character == '-':
                self.code += "memory[cursor]--;\n"
            elif character == '*':
                self.code += "memory[cursor]=0;\n"
            elif character == '.':
                self.code += "std::cout<<(char)memory[cursor];\n"
            elif character == ',':
                self.code += "std::cin>>memory[cursor];\n"
            elif character == '_':
                self.code += "std::cout<<std::endl;\n"
            elif character == '[':
                index += 1
                new_code = ''
                while character != ']':
                    # If we run into an error at this stage, it means that
                    # even though we've reached the end of the code, the
                    # loop has never been closed (thus, the error message).
                    try:
                        character = code[index]
                    except IndexError:
                        print("Error: Forgot to close the loop.")
                        return

                    # Current version does not support nested loops, so
                    # they are not allowed
                    if character == '[':
                        print("Error: Nested loops are not supported.")
                        return

                    elif character == ']':
                        break
                    new_code += character
                    index += 1

                # After extracting the code from the loop, we check to
                # see if the formatting is correct ([<range> <code>])
                splitted_code = new_code.split(' ')
                if len(splitted_code) != 2:
                    print("Error: Badly formatted loop.")
                    return
                
                # The range must be either i (short for infinite) or a
                # positive number.
                try:
                    code_range = int(splitted_code[0])
                    if code_range <= 0:
                        print("Error: The loop range must be greater than zero.")
                        return
                except:
                    if splitted_code != 'i':
                        print("Error: The loop does not contain a correct integer(range).")
                        return
                    else:
                        code_range = None
                
                # Checks to see what kind of loop we're dealing with,
                # and generates code accordingly.
                added = ''
                if code_range:
                    added += f'for (int i=0;i<{code_range};i++)\n'
                else:
                    added += 'while(true)\n'
                
                # Calls another interpreter to interpret the inner code
                # of the loop, and then adds the resulting c++ code to
                # its own code
                intprt2 = interpreter(False)
                intprt2.interpret(splitted_code[1])
                added += '{\n' + intprt2.code + '}\n'

                # If the resulting code is just a loop that does nothing,
                # the optimizer automatically does not include it. Of course,
                # you're more than welcome to create an infinite loop that
                # does nothing. The optimizer only removes useless for loops.
                if added.endswith('{\n}\n') and code_range != None:
                    self.code += added

            index += 1
        if self.have_body:
            self.code += '}'
        
        # Sends the resulting c++ code to a final optimizer
        # before storing it.
        self.code = c_optimize(self.code)
