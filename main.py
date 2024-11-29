import FreeSimpleGUI as sg


# Front End
label_todo_item = sg.Text("Todo item description:", size=(20, 1))
input_box_todo = sg.InputText(tooltip="Todo item description", size=(40, 1))
button_add = sg.FilesBrowse("Add", key="add", size=(7, 1), button_color=('white', 'green'))
button_edit = sg.FolderBrowse("Edit", key="edit", size=(7, 1), button_color=('white', 'orange'))
button_delete = sg.Button("Delete", key="delete", size=(7, 1), button_color=('white', 'red'))
label_todo_list = sg.Text("Todo list items(select):", size=(20, 1))
items_todos = sg.Listbox(["item1", "item2"], size=(40, 20))

# Front End - Window Interface
title = "Todo App"
new_window = sg.Window(title=title, layout=[
    [label_todo_item],
    [input_box_todo],
    [button_add, button_edit, button_delete],
    [label_todo_list],
    [items_todos]
])

while True:
    event, values = new_window.read()
    if event == sg.WIN_CLOSED:
        break

new_window.close()
