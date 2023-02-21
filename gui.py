from PySimpleGUI import *

label = Text("Type in a to-do")
input_box = InputText()
add_button = Button("Add")


window = Window("My To-Do App", layout = [[label], [input_box, add_button]])

window.read()
print("hello")
window.close()