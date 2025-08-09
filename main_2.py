import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def center_window(win, width, height):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f"{width}x{height}+{x}+{y}")

def on_click():
    label.config(text="✅ Action Completed!", foreground="#27ae60")

root = tk.Tk()
root.title("Pro Vibe with Image")
center_window(root, 500, 350)
root.configure(bg="#2c3e50")

# ttk style
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 12), padding=10, background="#3498db", foreground="white")
style.map("TButton", background=[("active", "#2980b9")])

# Load and display image
image_path = "codingal.png"  # Change to your image path 	
img = Image.open(image_path)
img = img.resize((120, 120), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)

image_label = tk.Label(root, image=photo, bg="#2c3e50")
image_label.pack(pady=15)

# Title label
label = tk.Label(root, text="Welcome!", font=("Segoe UI", 16, "bold"), bg="#2c3e50", fg="white")
label.pack(pady=10)

# Buttons
btn = ttk.Button(root, text="Run Action", command=on_click)
btn.pack(pady=10)

exit_btn = ttk.Button(root, text="Exit", command=root.destroy)
exit_btn.pack(pady=5)

root.mainloop()
