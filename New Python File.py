# def my_function():
#     #creates an exception
#     word = 'word'
#     val = ' '
#     for i in range(0,100):
#         val += word[i:i+1]
#     return val

def my_function(a, b):
    # creates an unbound local error
    try:
        c = a + b + c
    except UnboundLocalError:
        c = a + b
    return c


def calc_square_root(n):
    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt

    answer = sqrt(n)
    return answer
    print("Module not found")

def sqrt(n):
    if type(n) is str:
        raise TypeError("Cannot send a string")
    if n < 2:
       raise ValueError("You cannot send a negative number"
                        "to this function")
       
    x = n
    y = 1
    
    e = 0.00001
    while (x - y > e):
        x = (x+y)/2
        y = n/x
    return x


def main():
    x = 4
    try:
        answer = sqrt(4)
    except TypeError:
        new_x = int(x)
        answer = sqrt(new_x)
    except ValueError:
        print("You must send a positive number")
        answer = ''
    print(my_function(3, 2))


if __name__ == "__main__":
    main()
