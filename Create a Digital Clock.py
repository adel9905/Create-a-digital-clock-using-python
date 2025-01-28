import tkinter as tk
from time import strftime

def update_time():
    """Update the displayed time every second."""
    current_time = strftime('%I:%M:%S %p')
    label.config(text=current_time)
    label.after(200, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Configure the clock label
label = tk.Label(
    root, 
    font=('times new roman', 150), 
    background='white', 
    foreground='black'
)
label.pack(anchor='center')

# Start the clock update loop
update_time()

# Run the Tkinter main event loop
root.mainloop()