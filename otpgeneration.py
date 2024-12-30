import secrets

otp =''.join([str(secrets.randbelow(10)) for num in range(6)] )     

print(otp)
