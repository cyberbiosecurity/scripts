import tkinter as tk
import keyboard
import pyperclip
import time
import threading

# List of items to choose from
ITEMS = [
    "✔ Done",
    "⚠ Warning",
    "❌ Error",
    "⏱ Time",
    "? Unknown",
    "→ Next",
    "← Prev",
    "★ Important"
]

def insert_selected(text):
    pyperclip.copy(text)
    time.sleep(0.05)
    keyboard.press_and_release("ctrl+v")

import tkinter as tk
import os
import time

def show_popup():
    def on_select(event=None):
        try:
            selected = listbox.get(listbox.curselection())
            root.destroy()
            insert_selected(selected)
        except Exception as e:
            print(f"Selection error: {e}")

    def on_quit(event=None):
        print("Exiting the app.")
        os._exit(0)

    root = tk.Tk()
    root.title("Insert Symbol")
    root.attributes("-topmost", True)
    root.geometry("+500+300")
    root.resizable(False, False)

    listbox = tk.Listbox(root, font=("Consolas", 14), width=30, height=len(ITEMS) + 1)
    
    # ⏱ Insert current time as first item
    listbox.insert(tk.END, f"[{time.ctime()[11:16]}]")

    # 📋 Insert the rest of the items
    for item in ITEMS:
        listbox.insert(tk.END, item)
    listbox.pack()

    # ❌ Quit App button
    btn_quit = tk.Button(root, text="❌ Quit App (Ctrl+Q)", command=on_quit)
    btn_quit.pack(pady=5)

    # 🧠 Focus and grab control after UI is ready
    root.after(100, lambda: listbox.focus_force())
    root.after(100, lambda: root.grab_set())
    root.after(100, lambda: listbox.selection_set(0))

    # 🔗 Bindings
    listbox.bind("<Return>", on_select)
    listbox.bind("<Double-Button-1>", on_select)
    listbox.bind("<Escape>", lambda e: root.destroy())  # Just closes popup
    root.bind("<Control-q>", on_quit)

    root.mainloop()


def hotkey_thread():
    keyboard.add_hotkey("ctrl+f1", lambda: threading.Thread(target=show_popup).start())
    #keyboard.wait("esc")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    print("Press Ctrl+F1 to insert symbol. Ctrl+Q in popup- to exit.")
    hotkey_thread()
