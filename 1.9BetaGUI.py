import sys
import os
import ctypes
import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import time
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from tqdm import tqdm
except ImportError:
    print("tqdm not found, installing....")
    install('tqdm')
    from tqdm import tqdm

# Your main code follows
for i in tqdm(range(10)):
    pass
from tqdm import tqdm

# Create a loop from 0 to 50
for i in tqdm(range(8), desc="Update", unit="files"):
    time.sleep(0.7)  # Simulate work (delay of 0.1 sec)

print("[TQDM] ")

def run_as_admin():
    """Restart the script with administrator privileges."""
    if os.name != 'nt':
        # For non-Windows OS, automatic restart with admin rights
        return False
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    script = sys.argv[0]
    params = ' '.join([f'"{arg}"' for arg in sys.argv[1:]])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
        return True
    except:
        return False

if not run_as_admin():
    sys.exit()

# Functions
def create_file(directory, filename):
    try:
        filepath = os.path.join(directory, filename)
        with open(filepath, 'w') as f:
            f.write("This is a new file.")
        messagebox.showinfo("Success", f"File created at {filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create file: {e}")

def delete_file(directory, filename):
    try:
        filepath = os.path.join(directory, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            messagebox.showinfo("Success", f"File deleted: {filepath}")
        else:
            messagebox.showwarning("Warning", "File does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to delete file: {e}")

def run_task_manager():
    try:
        if os.name == 'nt':  # Windows
            subprocess.run('taskmgr', check=True)
        else:
            subprocess.run(['gnome-system-monitor'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Task Manager: {e}")

def open_device_manager():
    try:
        if os.name == 'nt':
            os.system('devmgmt.msc')
        else:
            # Device Manager is not available on Linux or other OS
            messagebox.showinfo("Info", "Device Manager is not available on this OS.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Device Manager: {e}")

def open_calculator():
    try:
        if os.name == 'nt':
            os.system('calc')
        else:
            # Attempt to open standard calculator on Linux
            subprocess.run(['gnome-calculator'], check=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open Calculator: {e}")

def search_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

def shutdown():
    try:
        if os.name == 'nt':
            os.system('shutdown /s /t 1')
        else:
            os.system('shutdown -h now')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to shut down: {e}")

def restart():
    try:
        if os.name == 'nt':
            os.system('shutdown /r /t 1')
        else:
            os.system('shutdown -r now')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to restart: {e}")

def main():
    root = tk.Tk()
    root.title("GUI MarkRuTools 1.9 Beta ")
    root.geometry("450x580") # Increased height for separators
    # Dark theme: black background, blue accents
    bg_color = "#000000"
    accent_color = "#00BFFF"
    root.configure(bg=bg_color)

    # Font style
    font_style = ("Arial", 12, "bold")
    buttons_params = {'font': font_style, 'bg': '#222222', 'fg': accent_color, 'activebackground': '#333333', 'activeforeground': accent_color}

    # Helper function to add a separator
    def add_separator(parent, color=accent_color):
        sep = tk.Frame(parent, bg=color, height=2)
        sep.pack(fill='x', pady=10, padx=20)

    # Directory and filename inputs
    dir_label = tk.Label(root, text="Directory:", bg=bg_color, fg=accent_color, font=font_style)
    dir_label.pack(pady=5)
    dir_entry = tk.Entry(root, width=50, bg="#222222", fg=accent_color, insertbackground=accent_color)
    dir_entry.pack(pady=5)

    filename_label = tk.Label(root, text="Filename:", bg=bg_color, fg=accent_color, font=font_style)
    filename_label.pack(pady=5)
    filename_entry = tk.Entry(root, width=50, bg="#222222", fg=accent_color, insertbackground=accent_color)
    filename_entry.pack(pady=5)

    # Create and delete file buttons
    create_button = tk.Button(root, text="Create File", command=lambda: create_file(dir_entry.get(), filename_entry.get()), **buttons_params)
    create_button.pack(pady=3)

    delete_button = tk.Button(root, text="Delete File", command=lambda: delete_file(dir_entry.get(), filename_entry.get()), **buttons_params)
    delete_button.pack(pady=3)

    add_separator(root) # Separator 1

    # Open Task Manager
    taskmgr_button = tk.Button(root, text="Open Task Manager", command=run_task_manager, **buttons_params)
    taskmgr_button.pack(pady=3)

    # Open Device Manager
    device_button = tk.Button(root, text="Open Device Manager", command=open_device_manager, **buttons_params)
    device_button.pack(pady=3)

    # Open Calculator
    calc_button = tk.Button(root, text="Open Calculator", command=open_calculator, **buttons_params)
    calc_button.pack(pady=3)
    
    # Новая кнопка "Info"
    info_button = tk.Button(root, text="Info", command=lambda: messagebox.showerror("MarkRuTools GUI 1.9", message="This is a test version of MarkRuTools GUI 1.9"), **buttons_params)
    info_button.pack(pady=3)

    add_separator(root) # Separator 2

    # Google Search
    search_frame = tk.Frame(root, bg=bg_color)
    search_frame.pack(pady=5)
    search_entry = tk.Entry(search_frame, width=35, bg="#222222", fg=accent_color, insertbackground=accent_color)
    search_entry.pack(side=tk.LEFT, padx=5)
    search_button = tk.Button(search_frame, text="Search Google (WEB)", command=lambda: search_google(search_entry.get()), **buttons_params)
    search_button.pack(side=tk.LEFT)

    add_separator(root) # Separator 3

    # Shutdown and Restart buttons
    shutdown_button = tk.Button(root, text="Shutdown PC", command=shutdown, **buttons_params)
    shutdown_button.pack(pady=3)
    restart_button = tk.Button(root, text="Restart PC", command=restart, **buttons_params)
    restart_button.pack(pady=3)

    root.mainloop()

if __name__ == "__main__":
    main()
