import tkinter as tk
from tkinter import scrolledtext

def save_notes():
    notes_content = text_area.get("1.0", tk.END)
    with open("build_notes.md", "w") as f:
        f.write(notes_content)
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Paste Build Notes")

# Create a label
label = tk.Label(root, text="Please paste your build notes below and click Save.", padx=10, pady=10)
label.pack()

# Create a scrolled text area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
text_area.pack(padx=10, pady=10)

# Create a save button
save_button = tk.Button(root, text="Save and Close", command=save_notes)
save_button.pack(pady=10)

# Bring the window to the front
root.lift()
root.attributes('-topmost',True)
root.after_idle(root.attributes,'-topmost',False)

# Start the GUI event loop
root.mainloop()