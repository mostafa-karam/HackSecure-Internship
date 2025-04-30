import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from cryptography.fernet import Fernet
import os

def select_file():
    file_path = filedialog.askopenfilename(title="Select Text File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

def generate_key():
    key = Fernet.generate_key()
    key_entry.delete(0, tk.END)
    key_entry.insert(0, key.decode())
    messagebox.showinfo("Key Generated", "A new encryption key has been generated.")

def encrypt_file():
    path = file_entry.get()
    key = key_entry.get()
    if not os.path.exists(path):
        messagebox.showerror("File Error", "Selected file does not exist.")
        return
    if not key:
        messagebox.showerror("Key Error", "Please enter a valid encryption key.")
        return
    try:
        with open(path, "rb") as f:
            data = f.read()
        fernet = Fernet(key.encode())
        encrypted = fernet.encrypt(data)

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Encrypted File")
        if save_path:
            with open(save_path, "wb") as f:
                f.write(encrypted)
            messagebox.showinfo("Success", "File encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def decrypt_file():
    path = file_entry.get()
    key = key_entry.get()
    if not os.path.exists(path):
        messagebox.showerror("File Error", "Selected file does not exist.")
        return
    if not key:
        messagebox.showerror("Key Error", "Please enter a valid encryption key.")
        return
    try:
        with open(path, "rb") as f:
            data = f.read()
        fernet = Fernet(key.encode())
        decrypted = fernet.decrypt(data)

        save_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Decrypted File")
        if save_path:
            with open(save_path, "wb") as f:
                f.write(decrypted)
            messagebox.showinfo("Success", "File decrypted successfully!")
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# --- GUI Setup ---
root = tk.Tk()
root.title("Modern File Encryption Tool")
root.geometry("700x400")
root.configure(bg="#0f172a")
root.resizable(False, False)

# Style
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#0f172a")
style.configure("TLabel", background="#0f172a", foreground="white", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 12), padding=8)
style.configure("TEntry", font=("Segoe UI", 12), padding=6)

# Layout
frame = ttk.Frame(root, padding=30)
frame.pack(expand=True)

# File Selector
ttk.Label(frame, text="📄 File to Encrypt/Decrypt:").grid(row=0, column=0, sticky="w", pady=(0,5))
file_entry = ttk.Entry(frame, width=50)
file_entry.grid(row=1, column=0, pady=(0, 10), sticky="ew")
ttk.Button(frame, text="Browse", command=select_file).grid(row=1, column=1, padx=(10, 0))

# Key Field
ttk.Label(frame, text="🔑 Encryption Key:").grid(row=2, column=0, sticky="w", pady=(10, 5))
key_entry = ttk.Entry(frame, width=50)
key_entry.grid(row=3, column=0, pady=(0, 10), sticky="ew")
ttk.Button(frame, text="Generate Key", command=generate_key).grid(row=3, column=1, padx=(10, 0))

# Action Buttons
ttk.Button(frame, text="Encrypt File", command=encrypt_file).grid(row=4, column=0, pady=(20, 10), sticky="ew")
ttk.Button(frame, text="Decrypt File", command=decrypt_file).grid(row=5, column=0, pady=(0, 10), sticky="ew")

root.mainloop()
