#!/usr/bin/python3
# defining a decorator
def hello_decorator(func):

    # inner1 is a Wrapper function in
    # which the argument is called

    # inner function can access the outer local
    # functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        # calling the actual function now
        # inside the wrapper function.
        func()

        print("This is after function execution")

    return inner1


# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")

# defining a function, to be called inside wrapper
def new_function_to_be_used():
    print("This is new  function !!")


# passing 'function_to_be_used' inside the
# decorator to control its behavior
for i in range(5):
    if i^2 == 0:
        continue
    print(i)


print('some infotmation  for git')
