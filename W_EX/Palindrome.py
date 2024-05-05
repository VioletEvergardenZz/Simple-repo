def is_palindrome(str):
    left,right=0,len(str)-1
    while left<right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True

input_str=input('input a str')
if is_palindrome(input_str):
    print('yes')
else:
    print('no')