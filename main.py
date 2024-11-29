import FreeSimpleGUI as sg
import sqlite3

# Fetch todos from SQL lite
query = 'SELECT task FROM todos ' \
        'WHERE completed=0 ' \
        'ORDER BY id ASC'
params = []
conn = sqlite3.connect(r'C:\Users\AndreyNizhnik\OneDrive - AFG INDIA HOLDINGS PTE. LTD\Personal\COURCES\Python3\Section09\todo.db')
c = conn.cursor()
c.execute(query, params)
todos_fetched = c.fetchall()
todos = [item[0] for item in todos_fetched]
conn.close()

# Frontend
label_todo_item = sg.Text("Todo item description:", size=(20, 1))
input_box_todo = sg.InputText(tooltip="Todo item description", size=(40, 1), key="task_description")
button_add = sg.Button("Add", key="add", size=(7, 1), button_color=('white', 'green'))
button_edit = sg.Button("Edit", key="edit", size=(7, 1), button_color=('white', 'orange'))
button_delete = sg.Button("Delete", key="delete", size=(7, 1), button_color=('white', 'red'))
button_clear = sg.Button("Clear", key="clear", size=(7, 1), button_color=('white', 'gray'))
label_todo_list = sg.Text("Todo list items (select):", size=(20, 1))
items_todos = sg.Listbox(todos, size=(40, 20), key="task_item_from_list")

# Frontend - Window Interface
title = "Todo App"
new_window = sg.Window(title=title,
                       layout=[
                           [label_todo_item],
                           [input_box_todo],
                           [button_add, button_edit, button_delete, button_clear],
                           [label_todo_list],
                           [items_todos]])

while True:
    event, values = new_window.read()
    match event:
        case "add":
            print(event)
            print(values)
            new_window['task_description'].update(value="")
        case "edit":
            print(event)
            print(values)
            new_window['task_description'].update(value="")
        case "delete":
            print(event)
            print(values)
            new_window['task_description'].update(value="")
        case "clear":
            print(event)
            print(values)
            new_window['task_description'].update(value="")
        case sg.WIN_CLOSED:
            break

new_window.close()
