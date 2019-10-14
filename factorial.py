# Function which returns factorial of a number

def fact(N):
    f = 1
    for value in range(1, N+1):
        f *= value
    return f

# Function which checks given string is palindrome or not

def ispalindrome(S):
    if(S == S[::-1]):
        return True
    else:
        return False