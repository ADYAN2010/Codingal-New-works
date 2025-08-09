import tkinter as tk

def open_new_window(event=None):  
    new_win = tk.Toplevel(root)
    new_win.title("New Window")
    new_win.geometry("300x200")
    tk.Label(new_win, text="This is a new window!", font=("Arial", 14)).pack(expand=True)

root=tk.Tk()
root.title("Main Window")
root.geometry("400x300")   

btn = tk.Button(root, text="Open New Window", command=open_new_window, font=("Arial", 12))
btn.pack(pady=50)

root.bind('<Control-n>', open_new_window)  

root.mainloop()