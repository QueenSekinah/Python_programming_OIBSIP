import tkinter as tk

bmi_records = {}

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_result_label.config(text=f"Your BMI: {bmi:.2f}")

    # Store BMI record
    user_id = user_id_entry.get()
    if user_id:
        bmi_records.setdefault(user_id, []).append(bmi)
        print(f"Recorded BMI for user {user_id}: {bmi:.2f}")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Enter weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Enter height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

user_id_label = tk.Label(root, text="Enter user ID:")
user_id_label.grid(row=3, column=0)

user_id_entry = tk.Entry(root)
user_id_entry.grid(row=3, column=1)

bmi_result_label = tk.Label(root, text="")
bmi_result_label.grid(row=4, columnspan=2)

root.mainloop()
