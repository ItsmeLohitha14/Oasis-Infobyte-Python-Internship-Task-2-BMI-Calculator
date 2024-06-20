import tkinter as tk
from tkinter import messagebox

def calculate_bmi(weight, height):
    "Calculate BMI based on weight (kg) and height (m). Formula: BMI = weight / (height * height)"
    return weight / (height * height)

def classify_bmi(bmi):
    "Classifying BMI into categories"
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Invalid input", "Weight and height must be positive numbers.")
            return

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nYou are classified as: {category}")
    
        # Provide health advice based on BMI category
        if category == "Underweight":
            messagebox.showinfo("Health Advice", "You are underweight. Consider consulting a healthcare provider.")
        elif category == "Overweight":
            messagebox.showinfo("Health Advice", "You are overweight. Consider maintaining a balanced diet and regular exercise.")
        elif category == "Obese":
            messagebox.showinfo("Health Advice", "You are obese. Consider consulting a healthcare provider for weight management.")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for weight and height.")

# main application window
root = tk.Tk()
root.title("BMI Calculator")

# Configure the main window
root.geometry("400x350")
root.configure(bg="white")

# Common font
font = ("Helvetica", 14)

# Weight label and entry
weight_label = tk.Label(root, text="Enter your weight in kilograms:", font=font, bg="white")
weight_label.pack(pady=5)

weight_entry = tk.Entry(root, font=font)
weight_entry.pack(pady=5)
weight_entry.focus_set()  # Set initial focus on weight entry

# Height label and entry
height_label = tk.Label(root, text="Enter your height in meters:", font=font, bg="white")
height_label.pack(pady=5)

height_entry = tk.Entry(root, font=font)
height_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate BMI", font=font, command=on_calculate)
calculate_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=font, bg="white")
result_label.pack(pady=10)

# Center all elements in the main window
for widget in root.winfo_children():
    widget.pack_configure(anchor="center")

root.mainloop()
