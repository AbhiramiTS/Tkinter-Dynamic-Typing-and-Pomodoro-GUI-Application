import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Mile to Kilometer Converter")

# Set padding for the window
window.config(padx=50, pady=50)


# Function to convert miles to kilometers
def miles_to_km():
    miles = miles_input.get()
    # Convert miles to kilometers using the conversion factor 1 mile = 1.609 kilometers
    km = int(miles) * 1.609
    # Update the result label with the calculated kilometers
    km_result_label.config(text=km)


# Create and place the label for input miles
miles_label = tk.Label(text="Miles : ")
miles_label.grid(column=1, row=0)

# Create and place the input entry for miles
miles_input = tk.Entry(width=10)
miles_input.grid(column=2, row=0)

# Create and place the label for displaying converted kilometers
km_label = tk.Label(text="Kilometers : ")
km_label.grid(column=1, row=1)

# Create and place the label to display the result (initially set to 0)
km_result_label = tk.Label(text="0")
km_result_label.grid(column=2, row=1)

# Create and place the button to trigger the conversion
calc_button = tk.Button(text="Convert", command=miles_to_km)
calc_button.grid(column=2, row=2)

# Start the Tkinter event loop
window.mainloop()
