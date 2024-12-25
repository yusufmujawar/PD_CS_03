print()
print('***** Welcome to Password Complexity Checker Application *****')
print('              *** Build By Mohamed Yusuf Mujawar ***          ')
print()

def check_password_strength(password):
    # Check if password is at least 8 characters long
    length = len(password) >= 8
    # Check if password contains at least one uppercase letter
    uppercase = any(char.isupper() for char in password)
    # Check if password contains at least one lowercase letter
    lowercase = any(char.islower() for char in password)
    # Check if password contains at least one digit
    onedigit = any(char.isdigit() for char in password)
    # Check if password contains at least one special character
    specialchar = any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password)
    
    # Check if password meets all the conditions
    if length and uppercase and lowercase and onedigit and specialchar:
        return "strong"
    elif length and uppercase and lowercase and onedigit:
        return "medium"
    else:
        return "weak"

# Test the function
print(check_password_strength("Yusuf@!@#$#$^&*(8888834-34-4###!!344)"))  # Strong
print(check_password_strength("Yusu8134"))  # Medium
print(check_password_strength("Yusuf"))  # Weak



