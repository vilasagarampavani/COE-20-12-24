import string
def strong_password(pas):
    if len(pas)<10 or len(pas)>15:
        return "Password must between 10 to 15 characters!"
    has_upper = any(char.isupper() for char in pas)
    has_lower = any(char.islower() for char in pas)
    has_digit = any(char.isdigit() for char in pas)
    has_special = any(char in string.punctuation for char in pas)
    if not(has_upper and has_lower and has_digit and has_special):
        return "Password must contain at least one uppercase letter, one lowercase letter,one digit and one special character"
    elif " " in pas:
        return "Password not allow white spaces"
    elif pas[-1] in ['.','@']:
        return "Password not ends with '.' or '@'"
    return "Passwrod is strong!"
pas=input("Enter a strong password:")
print(strong_password(pas))