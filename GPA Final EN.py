# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:21:27 2024

@author: ElaMolavi
"""
import tkinter as tk
from tkinter import messagebox


# Create the main window
root = tk.Tk()
root.title("GPA_Calculator")

# Create the label for the welcome message

welcome_label = tk.Label(root, text="******   Welcome to 'GPA_Calculator'   ******" ,font=("Helvetica", 18))

# Create the label for the END

END_label = tk.Label(root, text="* Ela.molavi@gmail.com *" ,font=("Helvetica", 10))

 #Define a function to calculate GPA with the removal of a single course
def calculate_gpa():
    try:
        score = float(score_entry.get())
        total_units = float(total_units_entry.get())
        if score < 0 or total_units <= 0:
            raise ValueError
        gpa = score / total_units
        gpa_label.config(text=f"current GPA: {round(gpa, 2)}")
    except ValueError:
        messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")
def calculate_emtiazekol():
     try:
         score = float(score_entry.get())
         grade = float(grade_entry.get())
         credit_hour = float(credit_hour_entry.get())
         if score < 0 or grade <= 0:
             raise ValueError
         emtiazekol= score - (grade*credit_hour)
         emtiazekol_label.config(text=f"The total score after removing the lesson is this: {round(emtiazekol, 2)}")
     except ValueError:
         messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")
def calculate_vahedekol():
      try:
          credit_hour = float(credit_hour_entry.get())
          total_units = float(total_units_entry.get())
          if total_units < 0 or credit_hour <= 0:
              raise ValueError
          vahedekol= total_units - credit_hour
          vahedekol_label.config(text=f"The total unit after removing the lesson: {round(vahedekol, 2)}")
          
      except ValueError:
          messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")
def calculate_final_GPA_Removed():
    try:
        score = float(score_entry.get())
        grade = float(grade_entry.get())
        total_units = float(total_units_entry.get())
        credit_hour = float(credit_hour_entry.get())
        vahedekol = total_units - credit_hour
        emtiazekol = score - (grade*credit_hour)
        if emtiazekol < 0 or vahedekol <= 0:
            raise ValueError
        final_GPA_Removed = emtiazekol / vahedekol
        final_GPA_Removed_label.config(text=f"GPA after removing the course: {round(final_GPA_Removed, 2)}")
        
    except ValueError:
        messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")
def calculate_emtiazekol2():
     try:
         score = float(score_entry.get())
         grade = float(grade_entry.get())
         credit_hour = float(credit_hour_entry.get())
         credit_hour2 = float(credit_hour2_entry.get())
         grade2 = float(grade2_entry.get())
         if score < 0 or grade <= 0:
             raise ValueError
         emtiazekol2= (score -(credit_hour * grade))+(credit_hour2 * grade2)
         emtiazekol2_label.config(text=f"Total score after removing and adding lessons: {round(emtiazekol2, 2)}")
     except ValueError:
         messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")
def calculate_vahedekol2():
      try:
          
          total_units = float(total_units_entry.get())
          credit_hour = float(credit_hour_entry.get())
          credit_hour2 = float(credit_hour2_entry.get())
          
          if total_units < 0 or credit_hour <= 0:
              raise ValueError
          vahedekol2= (total_units - credit_hour) + +credit_hour2
          vahedekol2_label.config(text=f"Total unit after removing and adding lessons: {round(vahedekol2, 2)}")
          
      except ValueError:
          messagebox.showerror("Error", "The input is invalid. Please enter a positive number.")                   
         
def calculate_final_GPA_Plus():
     try:
         score = float(score_entry.get())
         total_units = float(total_units_entry.get())
         credit_hour = float(credit_hour_entry.get())
         credit_hour2 = float(credit_hour2_entry.get())
         grade = float(grade_entry.get())
         grade2 = float(grade2_entry.get())
         emtiazekol2 = (score -(credit_hour * grade))+(credit_hour2 * grade2)
         vahedekol2 = (total_units - credit_hour) + +credit_hour2
         
         if emtiazekol2 < 0 or vahedekol2 <= 0:
             raise ValueError
         final_GPA_Plus = emtiazekol2 / vahedekol2
         final_GPA_Plus_label.config(text=f"GPA after adding and removing lessons: {round(final_GPA_Plus, 2)}")
         
     except ValueError:
         messagebox.showerror("Error", "The input is invalid. Please enter a positive number.") 
         
         
         
         
score_label = tk.Label(root, text="Please enter the total points received based on the units awarded:")
score_entry = tk.Entry(root)

total_units_label = tk.Label(root, text="Please enter the number of total course units (pass units + fail units) taken:")
total_units_entry = tk.Entry(root) 

credit_hour_label = tk.Label(root, text="Please enter the number of lessons you want to delete, if you don't want to delete a lesson, enter 0: ")
credit_hour_entry = tk.Entry(root)
      
grade_label = tk.Label(root, text="Please enter the grade of the lesson you want to delete, if you don't want to delete the lesson, enter 0: ")
grade_entry = tk.Entry(root)

credit_hour2_label = tk.Label(root, text="Please enter the number of credits you intend to take to improve your GPA: ")
credit_hour2_entry = tk.Entry(root)
      
grade2_label = tk.Label(root, text="Please enter the grade that you think would improve your GPA if you received it: ")
grade2_entry = tk.Entry(root)

# calculation buttons
gpa_label = tk.Label(root, text="",font=("Helvetica", 13))

emtiazekol_label = tk.Label(root, text="",font=("Helvetica", 13))

vahedekol_label = tk.Label(root, text="",font=("Helvetica", 13))


emtiazekol2_label = tk.Label(root, text="",font=("Helvetica", 13))


vahedekol2_label = tk.Label(root, text="",font=("Helvetica", 13))


final_GPA_Removed_label = tk.Label(root, text="",font=("Helvetica", 13))


final_GPA_Plus_label = tk.Label(root, text="",font=("Helvetica", 13))


calculate1_button = tk.Button(root, text="Current GPA", command=calculate_gpa)


calculate2_button = tk.Button(root, text="Total score after removing lessons", command=calculate_emtiazekol)


calculate3_button = tk.Button(root, text="The total unit after removing the lesson", command=calculate_vahedekol)


calculate4_button = tk.Button(root, text="GPA after removing lessons", command=calculate_final_GPA_Removed)


calculate5_button = tk.Button(root, text="Total score after removing and adding lessons", command=calculate_emtiazekol2)


calculate6_button = tk.Button(root, text="Total unit after removing and adding lessons", command=calculate_vahedekol2)


calculate7_button = tk.Button(root, text="GPA after adding and removing lessons", command=calculate_final_GPA_Plus)

            
# Define the input reset function
def reset_entries():
    score_entry.delete(0, tk.END)
    total_units_entry.delete(0, tk.END)
    gpa_label.config(text="")
    
    credit_hour_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    
    credit_hour2_entry.delete(0, tk.END)
    grade2_entry.delete(0, tk.END)
    vahedekol_label.config(text="")
    emtiazekol_label.config(text="")
    vahedekol2_label.config(text="")
    emtiazekol2_label.config(text="")
    final_GPA_Removed_label.config(text="")
    final_GPA_Plus_label.config(text="")
    
reset_button = tk.Button(root, text="Reset", command=reset_entries)
reset_button.grid()   

#Placing widgets with grid layout
welcome_label.grid(row=0, column=0, padx=10, pady=10)
score_label.grid(row=1, column=0, padx=10, pady=10)
score_entry.grid(row=1, column=1, padx=10, pady=10)
total_units_label.grid(row=2, column=0, padx=10, pady=10)
total_units_entry.grid(row=2, column=1, padx=10, pady=10)
credit_hour_label.grid(row=3, column=0, padx=10, pady=10)
credit_hour_entry.grid(row=3, column=1, padx=10, pady=10)
grade_label.grid(row=4, column=0, padx=10, pady=10)
grade_entry.grid(row=4, column=1, padx=10, pady=10)
credit_hour2_label.grid(row=5, column=0, padx=10, pady=10)
credit_hour2_entry.grid(row=5, column=1, padx=10, pady=10)
grade2_label.grid(row=6, column=0, padx=10, pady=10)
grade2_entry.grid(row=6, column=1, padx=10, pady=10)
calculate1_button.grid(row=0, column=2, padx=10, pady=10)
reset_button.grid(row=0, column=1, padx=10, pady=10)
calculate2_button.grid(row=1, column=2, padx=10, pady=10)
calculate3_button.grid(row=2, column=2, padx=10, pady=10)
calculate4_button.grid(row=3, column=2, padx=10, pady=10)
calculate5_button.grid(row=4, column=2, padx=10, pady=10)
calculate6_button.grid(row=5, column=2, padx=10, pady=10)
calculate7_button.grid(row=6, column=2, padx=10, pady=10)
gpa_label.grid(row=8, column=1, padx=10, pady=10)
emtiazekol_label.grid(row=9, column=0, padx=10, pady=10)
vahedekol_label.grid(row=9, column=1, padx=10, pady=10)
emtiazekol2_label.grid(row=10, column=0, padx=10, pady=10)
vahedekol2_label.grid(row=10, column=1, padx=10, pady=10)
final_GPA_Removed_label.grid(row=9, column=2, padx=10, pady=10)
final_GPA_Plus_label.grid(row=10, column=2, padx=10, pady=10)
END_label.grid(row=11, column=2, padx=10, pady=10)


# Running the main loop
root.mainloop()
