from functions import *
from time import *

date = strftime("%b - %d - %Y %H:%M:%S")
print("It is " + date)
todos = []
while True:
    user_action = input("Type add, show,edit or complete or exit : ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        todos = get_todos()
        todos.append(todo)

        write_todos(todos)





    elif 'show' in user_action:

        todos = get_todos()

        new_todos = []
        new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(new_todos):

            row = f"{index + 1} - {item}"
            print(row)
        print(f"Length is {index + 1}")

    elif 'exit' in user_action:
        break

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()


            new_todo = input("Enter a new to do: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todosthing = todos[number - 1].strip("\n")
            todos.pop(number - 1)

            write_todos(todos)

            message = f'Todo {todosthing} was removed from the list! '
            print(message)
        except IndexError:
            print("There is no item with that number. ")



    else:
        print("Your command is not valid!")


print("Thank you for using to do list app! Have a great day!!!")
