#!/bin/bash

USERNAME="pujitha"
PASSWORD="pujitha@123"

attempt=1

while [ $attempt -le 3 ]
do

    echo "Attempt $attempt of 3" 

     read -p "Enter Username: " user
     read -p "Enter Password: " pass
    echo

      if [ "$user" = "$USERNAME" ] && [ "$pass" = "$PASSWORD" ]; then
          echo "Login Successful"
          exit 0
      else
          echo "Invalid Username or Password"
      fi
    
      attempt=$((attempt + 1))
done 

echo "Account Locked"
