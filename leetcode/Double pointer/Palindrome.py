def is_palindrome(str,left,right):
    while left<right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True

input_str=input('input a str\n')
if is_palindrome(input_str,0,len(input_str)-1):
    print('yes')
else:
    print('no')