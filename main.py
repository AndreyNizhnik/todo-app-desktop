import FreeSimpleGUI as sg
import sqlite3
from datetime import datetime, timedelta

DTB_LOCATION = r'C:\Users\AndreyNizhnik\OneDrive - AFG INDIA HOLDINGS PTE. LTD\Personal' \
               r'\COURCES\Python3\Section09\todo.db'


# Fetch todos from SQL lite
def fetch_dtb():
    query = 'SELECT task FROM todos ' \
            'WHERE completed=0 ' \
            'ORDER BY id ASC'
    params = []
    conn = sqlite3.connect(DTB_LOCATION)
    c = conn.cursor()
    c.execute(query, params)
    todos_fetched = c.fetchall()
    todos = [item[0] for item in todos_fetched]
    conn.close()
    return todos


# Get date for new task - 2 weeks from current
today = datetime.today()
date_2_weeks_from_today = today + timedelta(weeks=2)
formatted_date = date_2_weeks_from_today.strftime('%Y-%m-%d')

# Frontend elements
label_todo_item = sg.Text("Todo item description:", size=(20, 1))
input_box_todo = sg.InputText(tooltip="Todo item description", size=(40, 1), key="task_description")
button_add = sg.Button("Add", key="add", size=(7, 1), button_color=('white', 'green'))
button_edit = sg.Button("Edit", key="edit", size=(7, 1), button_color=('white', 'orange'))
button_delete = sg.Button("Delete", key="delete", size=(7, 1), button_color=('white', 'red'))
button_clear = sg.Button("Clear", key="clear", size=(7, 1), button_color=('white', 'gray'))
label_todo_list = sg.Text("Todo list items (select):", size=(20, 1))
items_todos = sg.Listbox(fetch_dtb(), size=(40, 20), key="task_item_from_list", enable_events=True)

# Frontend - Window Interface
title = "Todo App"
new_window = sg.Window(title=title,
                       layout=[
                           [label_todo_item],
                           [input_box_todo],
                           [button_add, button_edit, button_delete, button_clear],
                           [label_todo_list],
                           [items_todos]])

# Main backend loop
while True:
    event, values = new_window.read()
    match event:
        case "add":
            task = values['task_description'].capitalize()
            responsible = "Unassigned"
            deadline = formatted_date
            project = "Other"
            if task:
                conn = sqlite3.connect(DTB_LOCATION)
                c = conn.cursor()
                c.execute('INSERT INTO todos (task, responsible, deadline, project) VALUES (?, ?, ?, ?)',
                          (task, responsible, deadline, project))
                conn.commit()
                conn.close()
                new_window['task_description'].update(value="")
                new_window['task_item_from_list'].update(values=fetch_dtb())
            else:
                sg.popup(f"Enter task description and try again!")
        case "edit":
            task = values['task_description'].capitalize()
            old_task = values["task_item_from_list"][0]
            if task:
                conn = sqlite3.connect(DTB_LOCATION)
                c = conn.cursor()
                c.execute('UPDATE todos SET task = ? WHERE task = ?', (task, old_task))
                conn.commit()
                conn.close()
                new_window['task_description'].update(value="")
                new_window['task_item_from_list'].update(values=fetch_dtb())
            else:
                sg.popup(f"Select task and try again!")
        case "delete":
            task = values["task_item_from_list"][0]
            if task:
                conn = sqlite3.connect(DTB_LOCATION)
                c = conn.cursor()
                c.execute('DELETE FROM todos WHERE task = ?', (task,))
                conn.commit()
                conn.close()
                new_window['task_description'].update(value="")
                new_window['task_item_from_list'].update(values=fetch_dtb())
            else:
                sg.popup(f"Select task and try again!")
        case "clear":
            new_window['task_description'].update(value="")
            new_window['task_item_from_list'].update(values=fetch_dtb())
        case "task_item_from_list":
            new_window['task_description'].update(value=values["task_item_from_list"][0])
        case sg.WIN_CLOSED:
            break

new_window.close()
