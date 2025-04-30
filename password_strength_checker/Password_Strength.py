import tkinter as tk
from tkinter import ttk
import re

def check_password_strength():
    password = password_entry.get()
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = sum([not length_error, not uppercase_error, not lowercase_error, not digit_error, not special_char_error])

    if score == 5:
        result_label.config(text="✔️ Strong Password", foreground="#16a34a")
    elif 3 <= score < 5:
        result_label.config(text="⚠️ Moderate Password", foreground="#eab308")
    else:
        result_label.config(text="❌ Weak Password", foreground="#dc2626")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("600x400")  # Increased size
root.configure(bg="#1e1e2f")  # Dark background
root.resizable(False, False)

# Modern Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TLabel", background="#1e1e2f", foreground="white", font=("Segoe UI", 14))
style.configure("TButton", background="#3b82f6", foreground="white", font=("Segoe UI", 12), padding=10)
style.configure("TEntry", font=("Segoe UI", 14), padding=10)

# Container Frame
frame = ttk.Frame(root, padding=50, style="TFrame")
frame.pack(expand=True)

# Widgets
ttk.Label(frame, text="🔐 Enter a password to check:", font=("Segoe UI", 16, "bold")).pack(pady=(0, 20))
password_entry = ttk.Entry(frame, width=40, show="*")
password_entry.pack(pady=10)

ttk.Button(frame, text="Check Strength", command=check_password_strength).pack(pady=20)

result_label = ttk.Label(frame, text="", font=("Segoe UI", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()
