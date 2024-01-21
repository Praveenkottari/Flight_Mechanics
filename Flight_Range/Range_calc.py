import tkinter as tk

# Function to calculate range and endurance
def calculate_range_endurance():
    # Get input values from user
    fuel_capacity = float(fuel_capacity_entry.get())
    fuel_consumption_rate = float(fuel_consumption_rate_entry.get())
    speed = float(speed_entry.get())

    # Calculate the range and endurance
    range = fuel_capacity * speed / fuel_consumption_rate
    endurance = fuel_capacity / fuel_consumption_rate

    # Update the result labels
    range_label.config(text="Range: " + str(round(range, 2)) + " km")
    endurance_label.config(text="Endurance: " + str(round(endurance, 2)) + " hours")

# Create a new window
window = tk.Tk()
window.title("Aircraft Range and Endurance Calculator")

# Define color scheme
bg_color = "#F7F7F7"
fg_color = "#333333"
button_color = "#4CAF50"

# Set window size and background color
window.geometry("400x250")
window.config(bg=bg_color)

# Create title label
title_label = tk.Label(window, text="Aircraft Range and Endurance Calculator", font=("Helvetica", 18), bg=bg_color, fg=fg_color)
title_label.pack(pady=10)

# Create input fields
input_frame = tk.Frame(window, bg=bg_color)
input_frame.pack()

fuel_capacity_label = tk.Label(input_frame, text="Fuel Capacity (liters):", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
fuel_capacity_label.grid(row=0, column=0, padx=10, pady=10)

fuel_capacity_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=10, justify="center")
fuel_capacity_entry.grid(row=0, column=1, padx=10, pady=10)

fuel_consumption_rate_label = tk.Label(input_frame, text="Fuel Consumption Rate (liters/hour):", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
fuel_consumption_rate_label.grid(row=1, column=0, padx=10, pady=10)

fuel_consumption_rate_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=10, justify="center")
fuel_consumption_rate_entry.grid(row=1, column=1, padx=10, pady=10)

speed_label = tk.Label(input_frame, text="Speed (km/h):", font=("Helvetica", 12), bg=bg_color, fg=fg_color)
speed_label.grid(row=2, column=0, padx=10, pady=10)

speed_entry = tk.Entry(input_frame, font=("Helvetica", 12), width=10, justify="center")
speed_entry.grid(row=2, column=1, padx=10, pady=10)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", font=("Helvetica", 14), bg=button_color, fg="white", command=calculate_range_endurance)
calculate_button.pack(pady=10)

# Create result labels
result_frame = tk.Frame(window, bg=bg_color)
result_frame.pack()

range_label = tk.Label(result_frame, text="", font=("Helvetica", 14), bg=bg_color, fg=fg_color)
range_label.pack(pady=10)

endurance_label = tk.Label(result_frame, text="", font=("Helvetica", 14), bg=bg_color, fg=fg_color)
endurance_label.pack(pady=10)

# Run the main
