# with the following lambdas I was able to make the to_the_power_seven() function, this works with any positive integer
square = lambda x: x**2
multiply = lambda x, y: x*y

def to_the_power_seven(x):
    return multiply(square(multiply(square(x),x)),x)


# you can insert the following four lambdas into the f variable and any positive integer into the x and y variables of apply_times_three(f,x,y) and return the correct answer
# examples include apply_times_three(multiply, 2, 1), apply_times_three(lst_ref, 3, 5), and apply_times_three(help_fun, 2, 6) 

multiply = lambda x, y: x * y
divide = lambda x, y: x // y
help_fun = lambda x, y: 'Help' + str(x) + str(y)
lst_ref = lambda x , y: x[y]

def apply_times_three(f,x,y):
    return f(x,f(x,f(x,y)))

# the purpose of writing echo_the_string(l, n) was to see if I could write the function without a for loop
def echo_the_string(l, n):
    
    def repeat(x):
        return x * n

    l2 = list(map(repeat,l))
    return l2

