# brainfuck_to_cpp
This is a minimal code designed to convert my standard brainfuck into c++ code. The code is written purely in python, without any additional libraries, and all the versions will follow that trend as well.

## Adam's Simplified Brainfuck
ASB is, as the name suggests, a simplified version of brainfuck designed by me (no wonder it's shit). The code is designed to be easier to write and work with (as if anyone's gonna really use this crap)

### Features of ASB
* Ranged loops
* Basic optimization
* Automatic error handling
* Verbose
* Easier to understand

### Problems
* Unable to handle nested loops (for now)
* Written in python (that in and on itself is enough to make anyone puke)

### Examples
* Get four letters from the user

`[4 ,>]`

* Get four letters from the user and print them (and a newline character ( _ )):

`[4 ,>][4 <][4 .>]_`
