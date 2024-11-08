from lesson_3 import UserService, User

user = UserService()

while True:
    oper = input('\n1 - add user \n2 - find user \n3 - delete user \n4 - show all \n')
    if oper == '1':
        name = input('name = ')
        email = input('email = ')
        age = int(input('age = '))

        user_service = User(name, email, age)
        user.add_user(user_service)

    elif oper == '2':
        email = input('email = ')

        find = user.find_user_by_email(email)

        print(f'Найден: {find.name}  {find.email}  {find.age}')
    
    elif oper == '3':
        email = input('email = ')
        
        user.delete_user(email)

    elif oper == '4':
        for row in user.show_all():
            name, age = row
            print(f'\nName: {name} \nAge: {age}')
        





find = user.find_user_by_email(user_service.email)
if find:
    print(f'Найден: {find.name}  {find.email}  {find.age}')

user.delete_user('nicxai12@gmail.com')