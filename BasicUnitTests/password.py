def validate_password(password:str)-> bool:
    if not isinstance(password,str):
        raise TypeError("Only string is allowed")
    if len(password) < 8:
        return False
    if any(password.isupper()for c in password) != True:
        if any(password.isdigit()for c in password) != True:
            return True
        else:
            return False
    else:
        return False

