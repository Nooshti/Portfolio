import FreeSimpleGUI as fs

label1 = fs.Text("Select files to compress:")
input1 = fs.Input()
choose_button1 = fs.FilesBrowse("Choose")

label2 = fs.Text("Select destination folder:")
input2 = fs.Input()
choose_button2 = fs.FolderBrowse("Choose")

compress_button = fs.Button("Compress")

window = fs.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

window.read()
window.close()