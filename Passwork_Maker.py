import random
Symbol = 'QWERTYUIOPASDFGHJKLZXCVBNMqwerty()uiopasdfghjklzxcvbnm123456789!@#$%^&*'
print('''
______________
Password Maker
______________''')
Chars_Password = int(input('How many passwords do you need?'))
Chars_Count = int(input('How many characters in your password?'))
print('This is Your Password :')
for i in range(0,Chars_Password,1) : 
    password = ''
    for r in range(0,Chars_Count,1):
        password += random.choice(Symbol)
    print(password)