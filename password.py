#password strenth checker

import re

#password strength conditions:
#min 8 chars,difit, 1 Uppercase, lowercase, special char

def check_password_strength(password):
    if len(password)<8:
        return "Weak: password must be at least 8 characters"
    
    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit"
    
    if not any(char.isupper() for char in password):
        return "Weak: password must contain upper character"
    
    if not any(char.islower() for char in password):
        return "Weak: password must contain lower character"
    
    if not re.search(r'[~!@#$%^&*()_+<>?{}||]', password):
        return "Medium: password must contain a special character"
    
    return "Strong: Your password is secured!"

def password_checker():
    print("Welcome to the password strength checker")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")

        if password.lower()== 'exit':
            print("Thank you for using this tool")
            break

        result = check_password_strength(password)
        print(result)

#execute the password checker tool

if __name__=="__main__":
    password_checker()
    
