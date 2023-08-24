import tkinter as tk
from tkinter import messagebox
import csv

def calculate_contributions_and_tax(monthly_hours):
    monthly_rate = 200.00
    sss_rate = 0.045
    philhealth_rate = 0.045
    pagibig_rate = 0.02
    withholding_tax_rate = 0.20
    max_sss_contribution = 900.00
    withholding_tax_threshold = 20833.00
    
    monthly_rate = monthly_rate * monthly_hours
    sss_contribution = min(monthly_rate * sss_rate, max_sss_contribution)
    philhealth_contribution = (monthly_rate * philhealth_rate) / 2
    pagibig_contribution = monthly_rate * pagibig_rate
    withholding_tax = 0 if monthly_rate <= withholding_tax_threshold else (monthly_rate - withholding_tax_threshold) * withholding_tax_rate
    
    net_salary = monthly_rate - (sss_contribution + philhealth_contribution + pagibig_contribution + withholding_tax)
    
    return monthly_rate, sss_contribution, philhealth_contribution, pagibig_contribution, withholding_tax, net_salary

def calculate_and_display():
    employee_name = name_entry.get()
    monthly_hours = float(hours_entry.get())
    
    monthly_rate, sss_contribution, philhealth_contribution, pagibig_contribution, withholding_tax, net_salary = calculate_contributions_and_tax(monthly_hours)
    
    result_text = (
        f"Employee Name: {employee_name}\n"
        f"Monthly Rate: {monthly_rate}\n"
        f"SSS Contribution: {sss_contribution}\n"
        f"Philhealth Contribution: {philhealth_contribution}\n"
        f"Pag-IBIG Contribution: {pagibig_contribution}\n"
        f"Withholding Tax: {withholding_tax}\n"
        f"Net Salary: {net_salary}"
    )
    
    result_label.config(text=result_text)
    
    # Save results in a CSV file
    with open("employee_salary.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Employee Name", "Monthly Rate", "SSS Contribution", "Philhealth Contribution", "Pag-IBIG Contribution", "Withholding Tax", "Net Salary"])
        writer.writerow([employee_name, monthly_rate, sss_contribution, philhealth_contribution, pagibig_contribution, withholding_tax, net_salary])
    
    messagebox.showinfo("Saved", "Results saved to employee_salary.csv")

# Create the main window
root = tk.Tk()
root.title("Employee Salary Calculator")

# Create and arrange GUI elements
name_label = tk.Label(root, text="Employee Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

hours_label = tk.Label(root, text="Monthly Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_and_display)
calculate_button.pack()

result_label = tk.Label(root, text="", wraplength=400)
result_label.pack()

# Start the GUI event loop
root.mainloop()
