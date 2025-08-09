import tkinter as tk
from tkinter import ttk

# Function to center window on screen
def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 6) - (width // 6)
    y = (screen_height // 6) - (height // 6)
    win.geometry(f"{width}x{height}+{x}+{y}")

# Function when button is clicked
def on_click():
    label.config(text="✅ Action Completed!", foreground="#27ae60")

# Main window
root = tk.Tk()
root.title("Pro Vibe Window")
center_window(root, 600, 500)
root.configure(bg="#2c3e50")

# Use ttk theme for modern look
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=10, background="#3498db", foreground="white")
style.map("TButton", background=[("active", "#2980b9")])

# Title label
label = tk.Label(root, text="Welcome!", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white")
label.pack(pady=30)

# Action button
btn = ttk.Button(root, text="Run Action", command=on_click)
btn.pack(pady=10)

# Exit button
exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=5)

# Run
root.mainloop()