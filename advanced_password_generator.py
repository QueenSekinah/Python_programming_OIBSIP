import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    # Determine character set based on user selection
    characters = ''
    if include_letters.get():
        characters += string.ascii_letters
    if include_numbers.get():
        characters += string.digits
    if include_symbols.get():
        characters += string.punctuation

    # Check if at least one character set is selected
    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Copy password to clipboard
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    # Display password
    password_display.config(text=password)

root = tk.Tk()
root.title("Password Generator")

# Password Length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Character Set Options
include_letters = tk.BooleanVar()
letters_checkbox = tk.Checkbutton(root, text="Include Letters", variable=include_letters)
letters_checkbox.grid(row=1, column=0)

include_numbers = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers)
numbers_checkbox.grid(row=1, column=1)

include_symbols = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=include_symbols)
symbols_checkbox.grid(row=1, column=2)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=3)

# Display Generated Password
password_display_label = tk.Label(root, text="Generated Password:")
password_display_label.grid(row=3, column=0)
password_display = tk.Label(root, text="", font=("Arial", 12))
password_display.grid(row=3, column=1, columnspan=2)

root.mainloop()