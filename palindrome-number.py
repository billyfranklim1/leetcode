def isPalindrome(x):
    if(x == 0):
        return True
    
    if(x < 0):
        return False

    reverse = 0
    num = x
    while x != 0 :
        last = x % 10
        reverse = reverse * 10 + last
        x=x//10

    return reverse == x



print(isPalindrome(121))
