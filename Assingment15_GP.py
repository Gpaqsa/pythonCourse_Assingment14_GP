# Todo Application
# With OPP Method
import datetime


# 1. addTodo
# 2. UpdateTodo
# 3. showTodo
# 4. deleteTodo


class Database:
    todosDB = []

    def addTodo_db(self, todo):
        self.todosDB.append(todo)

        print("Todo Successful  added! \n")

    def updateTodo_db(self, index, newTodo):
        self.todosDB[index] = newTodo
        print("Todo Update Successful")

    def deleteTodo_db(self, index):
        self.todosDB.pop(index)
        print("Todo Delete Successful")

    def get_todos(self):
        return self.todosDB


class Manager:
    def __init__(self, database):
        self.database = database

    def add_todo(self, todo):
        self.database.addTodo_db(todo)

    def show_todos(self):
        data = self.database.get_todos()

        for item in data:
            print(f"{'-' * 25}{data.index(item) + 1}{'-' * 25}")
            print(item)
            print(f"{'-' * 51}")

    def update_todo(self, index, newTodo):
        self.database.updateTodo_db(index, newTodo)

    def delete_todo(self, index):
        self.database.deleteTodo_db(index)

    def get_todos(self):
        return len(self.database.get_todos())


class Todo:
    def __init__(self, textTodo, deadline):
        self.textTodo = textTodo
        self.date = datetime.datetime.now()
        self.deadline = deadline

    def __str__(self):
        return f"Date: {self.date.strftime('%d/%m/%Y %H:%M')}\nToDo: {self.textTodo}\nDeadline: " \
               f"{self.deadline.strftime('%d/%m/%Y %H:%M')}"


def todo_checker(manager):
    while True:
        manager.show_todos()

        print("Choose ToDo N from list to replace or delete")
        todo_number = input("~  ")
        if not todo_number.isdigit():
            print("Please enter the digit!")
            continue

        todo_number = int(todo_number)
        if todo_number > len(manager.database.todosDB) or todo_number < 1:
            print(f"Please choose ToDo N between 1 - {len(manager.database.todosDB)} range!")

        todo_number -= 1
        return todo_number


def create_deadline(deadline_text):
    try:
        return datetime.datetime.strptime(deadline_text, "%d/%m/%Y %H:%M")
    except ValueError:
        raise ValueError("Invalid deadline format. Use DD/MM/YYYY HH:MM")


def menu():
    choice = None
    database = Database()
    manager = Manager(database)

    while choice != "q":
        print(f"\n{'-' * 10} Todo List Menu {'-' * 10}")
        print("a) Add Todo")
        print("u) Update Todo")
        print("d) Delete Todo")
        print("s) Show Todo")
        print("q) Quit From Project\n")

        print("Action")
        choice = input("~  ").lower()

        if choice == "a":
            print(f"\n{'#' * 3} New Todo {'#' * 3}")
            print("Enter Text --> ")
            todoText = input("~  ")
            print("Enter Deadline -->")
            deadlineText = input("~  ")
            deadline = create_deadline(deadlineText)
            todo = Todo(todoText, deadline)

            manager.add_todo(todo)
        elif choice == "u":

            if database.todosDB:

                print(f"\n{'#' * 3} Update Todo {'#' * 3}")
                index = todo_checker(manager)

                print("Enter Text --> ")
                newTodoText = input("~  ")
                print("Enter Deadline -->")
                newDeadlineText = input("~  ")
                newDeadline = create_deadline(newDeadlineText)
                newTodo = Todo(newTodoText, newDeadline)

                manager.update_todo(index, newTodo)
            else:
                print("There are no ToDo's in the database!")

        elif choice == "d":

            if database.todosDB:
                print(f"\n{'#' * 3} Delete Todo {'#' * 3}")
                index = todo_checker(manager)

                manager.delete_todo(index)
            else:
                print("There are no ToDo's in the database!")

        elif choice == "s":

            manager.show_todos()
        else:
            print("Can't manage it")


menu()
