import json
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path

def resource(name: str) -> str:
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent))
    return str(base / name)


def browse_input():
    path = filedialog.askopenfilename(filetypes=[("JSON", "*.json"), ("All files", "*.*")])
    if path:
        input_var.set(path)


def convert_and_save():
    src = input_var.get().strip()
    if not src:
        messagebox.showwarning("Missing file", "Please select an input JSON file.")
        return

    try:
        text = Path(src).read_text(encoding="utf-8")
        pretty = json.dumps(json.loads(text), indent=2, ensure_ascii=False)
    except json.JSONDecodeError as e:
        messagebox.showerror("Invalid JSON", f"{e.msg}\nLine {e.lineno}, column {e.colno}")
        return
    except OSError as e:
        messagebox.showerror("Read error", str(e))
        return

    dst = filedialog.asksaveasfilename(
        defaultextension=".json",
        initialfile=Path(src).stem + "_pretty.json",
        filetypes=[("JSON", "*.json"), ("All files", "*.*")]
    )
    if not dst:
        return

    try:
        Path(dst).write_text(pretty, encoding="utf-8")
        messagebox.showinfo("Done", f"Saved:\n{dst}")
    except OSError as e:
        messagebox.showerror("Write error", str(e))


root = tk.Tk()
root.title("Pretty JSON Converter")
root.resizable(False, False)
root.iconbitmap(resource("icon.ico"))

frame = ttk.Frame(root, padding=20)
frame.pack()

ttk.Label(frame, text="Input file").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 4))

input_var = tk.StringVar()
ttk.Entry(frame, textvariable=input_var, width=46).grid(row=1, column=0, padx=(0, 8))
ttk.Button(frame, text="Browse", command=browse_input).grid(row=1, column=1)
ttk.Button(frame, text="Convert and Save", command=convert_and_save).grid(
    row=2, column=0, columnspan=2, pady=(16, 0), sticky="ew")

root.mainloop()
