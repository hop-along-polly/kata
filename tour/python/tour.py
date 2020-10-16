import time


if __name__ == '__main__':
    print("""
        __________          __  .__                    ___________                  
        \______   \___.__._/  |_|  |__   ____   ____   \__    ___/___  __ _________ 
        |     ___<   |  |\   __\  |  \ /  _ \ /    \    |    | /  _ \|  |  \_  __  \\
        |    |    \___  | |  | |   Y  (  <_> )   |  \   |    |(  <_> )  |  /|  | \/
        |____|    / ____| |__| |___|  /\____/|___|  /   |____| \____/|____/ |__|   
                  \/                \/            \/                            
    """)
    print('Welcome to the Python tour! This aims to teach you enough Python that you can complete any of the other Kata provided.')
    time.sleep(5)

    print("""A couple of quick notes before we get started.
      - Press ctrl + c to exit out of the program.
      - Backticks (`) are used to add emphasis.
      - Anything enclosed by triple backticks (```) should be read as code.
      - When you see `?:` it means awaiting input.
    """)

    time.sleep(10)
    student = input("Please type your name and then press enter. \n?: ")
    time.sleep(0.5)
    print(f'Hello {student}')


    # Fundamentals
    time.sleep(1)
    print() # always give a new line
    print('Lets cover the fundamentals of Python.')
    time.sleep(1.5)
    print("""Python is an interpreted, dynamically typed, object oriented programming langauge.
The plain english explanation of those terms are:

    Interpreted:       The compiling of code is delayed until that block of code is needed allowing for execution of the code
                       and compiling of the code to occur in tandem. Languages like C++ and Java compile all of the source
                       code before execution can start.


    Dymanically Typed: When a value is stored in the program it's data type is determined at the time it is saved, rather
                       than being predefined by the programmer.


    Object Oriented:   Heirarchical structures called "classes" are used to organize code. Object Oriented or OO languages
                       are the most popular types of programming languages.
    """)
    input('Press enter to continue on to code comments. \n:? ')

    # Comments
    print("""\n
###############################
#       Code Comments         #
###############################

Our first scenic view on this tour is Code Comments.

Code Comments more commonly called, comments, are a mechanism for developers to provide documentation about their code.
Most often they are used to explain what code is doing, or why code was written the way it was.

Comments are ignored by the interpreter so anything in a code comment is not executed.

Python treats any line starting with `#` as a comment.

Example
```
# This is a comment. The line below is actual code, but it is commented out.
# print('Hello student')
print('Hello World!') # This line of code will execute and print Hello World to your screen.
```
    """)
    # TODO It would be cool if this could be abstractd to a quiz object or somethin.
    input('Press enter to continue. \n:? ')
    answer = input('What character appears at the beginning of a line indicating that line is a comment? \n?: ')
    if answer == '#':
        print('Correct!')
    else:
        print("Incorrect. A `#` indicates that line is a code comment.")

    time.sleep(1)
    answer = input("""
Given this block of code what would be printed to your screen?
# print('A')
print('B')
    """)
    if answer == 'B':
        print('Correct!')
    elif answer == "'B'":
        print("90% Correct. The value actually printed is B, the opening and closing ' represent B is a string. Which is a great transition to our next stop...")
    else:
        print("Incorrect. Only B is printed. The '#' before print('A') means that print command will not be executed.")
    # TODO Maybe figure out a way to allow users to retry the quiz.

    # Data Types
    time.sleep(2.5)
    print("""\n
###############################
#        Data Types           #
###############################

Data Types, usually shortened to types, describes the data being stored. Given a specific data type you can infer properties
of that type.

For example 10 is an integer. The Python data type for integers is `int`. Since you can add, subtract, multiply, and divide
integers you know you can add, subtract, multiply, and divide int's in Python.

The data types this tour covers are:
    - int (Integers)
    - float (Floating point numbers i.e. 10.0)
    - bool (Boolean logic values True/False)
    - str (Strings of characters i.e. `This is a string` while `a` is a character)
    - list (Lists of int, str, bool etc.)
    - dict (dictionaries key/value stores mapping a key to a int, str, or bool value)

    Each of these types will be covered in more detail starting with ints.
    """)
    #int
    time.sleep(2.5)
    print("The first data type we are going to cover are integers. Python uses the abbreviated 'int' to represent this data type.")
    print("As implied by the name this is used to ")
    ## str
    time.sleep(2.5)
    print("The first data type we are going to cover are 'strings'. Python uses the abreviated 'str' to represent this data type.")
    print("strings are used for anything ")
