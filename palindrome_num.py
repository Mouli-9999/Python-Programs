def palindrome():
    string = input("Enter the value:")
    if(string[::-1] == string):
        print(string, "is plaindrome")
    else:
        print(string,"is not palindrome")
palindrome()