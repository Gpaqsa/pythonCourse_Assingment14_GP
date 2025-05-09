import datetime
import sqlite3


class Database:
    def __init__(self, db_name="todosDb.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.__createTable()

    def __createTable(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
             tid INTEGER PRIMARY KEY AUTOINCREMENT,
             text TEXT NOT NULL,
             date TEXT
            );
            """
        )

    def getAll_data(self):
        self.cursor.execute(
            """
            SELECT tid, text, date FROM todos;
            """
        )
        dataFromDB = self.cursor.fetchall()
        # print(dataFromDB)
        todoList = []
        for todo in dataFromDB:
            tid, text, date_str = todo
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
            todoList.append(Todo(text, date=date, tid=tid))
        return todoList

    def addTodo_db(self, todo):
        self.cursor.execute("INSERT INTO todos (text, date) VALUES (?, ?)", (todo.text, str(todo.date)))
        self.connection.commit()
        print("Todo Successfully added!\n")



class Todo:
    def __init__(self, text, date=None, tid=None):
        self.tid = tid
        self.text = text
        self.date = date if date else datetime.datetime.now()

    def __str__(self):
        return f"TID: {self.tid}\nDate: {self.date.strftime('%d/%m/%Y %H:%M')}\nToDo: {self.text}\n"


class Manager:
    def __init__(self, database):
        self.database = database

    def addTodo(self):
        todo_text = input("Enter the todo text: ")
        new_todo = Todo(todo_text)
        self.database.addTodo_db(new_todo)

    def show_data(self):
        allTodos = self.database.getAll_data()
        if allTodos:
            print(f"\n{'-' * 43} Your To-Do List {'-' * 43}")
            for todo in allTodos:
                print(todo)
            print("-" * 100)
        else:
            print("\nYour todo list is empty.\n")

def main():
    dataBase = Database()
    maneger = Manager(dataBase)

    while True:
        print("Options:")
        print("1. Add Todo")
        print("2. Show Todos")
        print("3, Update Todo")
        print("4, Delete Todo")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            maneger.addTodo()
        elif choice == '2':
            maneger.show_data()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


