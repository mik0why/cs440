
'''
GCD algorithm
'''
def gcd(a, b):

    i = 1
    v_min = min(a,b)
    v_max = max(a,b)

    while(i * v_min < v_max):
        i+=1

    if (v_max - v_min * i == 0):
        return v_min
     
    i-=1
    return gcd(v_max - v_min * i, v_min)


'''
Rectangles on a rubik's cube
'''
def rubiks(n):

    def fact(n):
        if n == 0: 
            return 1
        else:
            return n * fact(n-1)

    return 6 * fact(n+1) * fact(n+1) / 4      


'''
Guessing a number
'''
# def guess_unlimited(n, is_this_it):
#     # The code here is only for illustrating how is_this_it() may be used 
#     number = random.randrange(1, n)
#     guess = input("type in your guess")
#     '''guess = n/2 
#     if is_this_it(guess) == True:
#         return guess'''
#     return -1
        
def guess_unlimited(n, is_this_it):
    from random import *
    number = randrange(1, n)
    guess = input("input your number")
    
    while(is_this_it(guess)!=True):
        guess = input("incorrect, input your number again")
        
    return guess
    

'''
Guessing a number where you can only make two guesses that are larger
'''
def guess_limited(n, is_this_smaller):
    from random import *
    number = randrange(1, n)
    guess = input("input your number")
    fail_count = 0

    while(is_this_smaller(n/2) == False){
        fail_count=+1
        n=/2

    }

	counter = 0 #keeping track of how many 'Fails'
    return -1
        
'''
Guessing a number, bonus problem
'''
def guess_limited_plus(n, is_this_smaller):
    return -1
        

