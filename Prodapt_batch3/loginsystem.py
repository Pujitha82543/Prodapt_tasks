correct_password = "admin123"
attempts = 3

while attempts > 0:
    password = input("Enter Correct password: ")

    if password == correct_password:
        print("Login Successfull")
        break
    else:
        attempts +=1
        if(attempts > 0):
            print("Login Successful")
        else:
            print("Attempt Locked")