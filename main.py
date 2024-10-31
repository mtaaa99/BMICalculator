from tkinter import *

window =Tk()

window.title("BMI Calculator")
window.minsize(width = 250, height = 250)

label_1 = Label(text = "Enter Your Weight(kg)")
label_1.pack()

entry_1 = Entry(width = 20)
entry_1.focus()
entry_1.pack()

label_2 = Label(text = "Enter Your Height(cm)")
label_2.pack()

entry_2 = Entry(width = 20)
entry_2.pack()

result_label = Label(text="")
result_label.pack()

def calculate_bmi():
    try:
        weight = float(entry_1.get())
        height_cm = float(entry_2.get())
        height_m = height_cm / 100  # cm'yi metreye dönüştürme
        bmi = weight / (height_m ** 2)
        if bmi < 16.0:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Several Underweight")
        elif bmi > 16.0 and bmi <= 18.4:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Underweight")
        elif bmi > 18.4 and bmi <=24.9:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Normal")
        elif bmi > 24.9 and bmi <= 29.9:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Overweight")
        elif bmi > 29.9 and bmi <= 34.9:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Moderately Obese")
        elif bmi > 34.9 and bmi <= 39.9:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Severely Obese")
        elif bmi > 39.9:
            result_label.config(text = f"Your BMI is: {bmi:.2f}" + "You are Morbidly Obese")
    except ValueError:
        result_label.config(text = "Please Enter Valid Number")

button = Button(text = "Calculate")
button.config(command = calculate_bmi)
button.pack()
window.mainloop()