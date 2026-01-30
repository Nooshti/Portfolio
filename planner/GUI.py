import functions
import FreeSimpleGUI as fs

label = fs.Text("Type in a to-do")
input_box = fs.InputText(tooltip="Enter todo:", key="todo")
add_button = fs.Button("Add")
# layout expects a list
# if u want to put input_box below label then put both in separate brackets



window = fs.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read() # method which returns something
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case fs.WINDOW_CLOSED:
            break

window.close()