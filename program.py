"""
    Create a simple python program consisting of;
    1. Data Types
    2. Data Structure
    3. Functions

"""

# Registration Form 
print("Welcome to Smoky Tech")
print('Sign Up Form')

def signup(name, email, username, age, password):
    name=input("Name\n")
    username=input("Username\n")
    email=input("Email Address\n")
    try:
        age=int(input("Age\n"))
        
    except ValueError:
        print("Your inpiut must be an Integer")
    password=input("Password(mini. length of 8)\n")
    
    #print(name, username, email, age, password)
    
    print(f'{name}, you are welcome to Smoky Tech. Your username is {username}. Click the link in your email to verify your account.')
    
signup(name=any, username=any, email=any, age=any, password=any)

# A dictionary containing names and age
data={"user": ['Luke', 'James', 'Marvelous',],
      "age": ['17', '22', '25']}
#print(data)

print(data.get("user",) [0])
print(data.get("age",) [0])
print(data.get("user",) [1])
print(data.get("age",) [1])
print(data.get("user",) [2])
print(data.get("age",) [2])