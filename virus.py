import tkinter as tk
from tkinter import messagebox

def show_alert():
    messagebox.showwarning("⚠️ Warning", "Stop! Virus detected on your device!")

root = tk.Tk()
root.title("Virus Scanner")
root.geometry("220x150")
root.resizable(False, False)

btn = tk.Button(root, text="Start Virus Scan", command=show_alert, font=("Arial", 12), bg="#ff4c4c", fg="white", activebackground="#ff1a1a")
btn.pack(expand=True)

root.mainloop()
