# Fir check kariye ki user ka password sakht hai ya nahi. Ek sakht password ko yeh sab rule follow karne chaiye:

      

password=input("Enter the password :")
# a=(len(password))

if (len(password))>=6 and (len(password))<=16:
    print(len(password))
    if "$" in password:
        if "2" or "8" in password:
            if "A"or "Z" in password: 
                print("Strong password")


