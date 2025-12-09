from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 

window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r") as input_file:
    text = input_file.read()
    txt.edit.insert(END, text)
    input_file.close()
    window.title(f"Codingal's Text editor - {filepath}")

def save_file():
    """Open a file for editing."""
    filepath = asksaveasfilename(defaulttension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as input_file:
              
    text = txt.edit.insert(END, text)
    output_file.write(text)
    window.title(f"Codingal's Text editor - {filepath}")
txt_edit = Text(window)
fr_buttons = Frame(window, relif=RAISED, bd=2)
btn_open = Button(fr_buttons, text = "Open", comand = open_file)
btn_save = Button(fr_buttons, text = "Save Ass...", comand = save_file)

btn_open.grid(row=0, column=0, sticky = "ew", padx=5, pady=5)
btn_save.grid(row=0, column=0, sticky = "ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky = "ns")
txt_edit.grid(row=0, column=1, sticky = "nsew")

window.mainloop()