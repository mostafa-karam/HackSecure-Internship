import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading

def scan_ports():
    result_text.configure(state='normal')
    result_text.delete(1.0, tk.END)  # Clear output

    target = target_entry.get().strip()
    port_range = port_range_entry.get().strip()

    # Validate input
    if not target or not port_range:
        messagebox.showerror("Input Error", "Please enter both target and port range.")
        return

    try:
        start_port, end_port = map(int, port_range.split('-'))
        if start_port < 0 or end_port > 65535 or start_port > end_port:
            raise ValueError
    except ValueError:
        messagebox.showerror("Range Error", "Enter a valid port range (e.g., 20-80).")
        return

    def run_scan():
        scan_button.config(state='disabled')
        result_text.insert(tk.END, f"\n[+] Scanning {target} from port {start_port} to {end_port}...\n\n")
        for port in range(start_port, end_port + 1):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                try:
                    if s.connect_ex((target, port)) == 0:
                        result_text.insert(tk.END, f"[OPEN] Port {port}\n")
                        result_text.see(tk.END)
                except socket.error:
                    continue
        result_text.insert(tk.END, "\n[+] Scan Complete ✅\n")
        scan_button.config(state='normal')
        result_text.configure(state='disabled')

    threading.Thread(target=run_scan).start()

# GUI Setup
root = tk.Tk()
root.title("Modern Port Scanner")
root.geometry("700x550")
root.configure(bg="#0f172a")
root.resizable(False, False)

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#0f172a")
style.configure("TLabel", background="#0f172a", foreground="#ffffff", font=("Segoe UI", 13))
style.configure("TButton", font=("Segoe UI", 12), padding=8)
style.configure("TEntry", font=("Segoe UI", 12), padding=6)

# Frame
main_frame = ttk.Frame(root, padding=30, style="TFrame")
main_frame.pack(expand=True)

# Inputs
ttk.Label(main_frame, text="🌐 Target IP or Domain:").pack(anchor="w", pady=(0, 5))
target_entry = ttk.Entry(main_frame, width=45)
target_entry.pack(pady=(0, 15))

ttk.Label(main_frame, text="📦 Port Range (e.g., 20-1000):").pack(anchor="w", pady=(0, 5))
port_range_entry = ttk.Entry(main_frame, width=45)
port_range_entry.pack(pady=(0, 15))

scan_button = ttk.Button(main_frame, text="Start Scan", command=scan_ports)
scan_button.pack(pady=(5, 15))

# Output Box
result_text = tk.Text(main_frame, height=15, width=70, bg="#1e293b", fg="#22c55e", font=("Courier New", 11), bd=0, relief="flat")
result_text.pack(pady=10)
result_text.configure(state='disabled')

root.mainloop()
