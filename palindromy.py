def palindrome(string):
    return string == string[::-1]
print(palindrome('ala'))
print(palindrome('kajak'))
print(palindrome('kawa'))
print(palindrome('12321'))      