# Digital Clock Using Tkinter

This project is a simple **Digital Clock** created using Python's `Tkinter` library. The clock displays the current time in a **12-hour format (HH:MM:SS AM/PM)** and updates every 200 milliseconds.

---

## How It Works

1. **Importing Required Modules**
   - `tkinter` is used to create the graphical user interface (GUI).
   - `strftime` from the `time` module is used to format the current time into a readable string.

2. **Defining the `update_time` Function**
   - This function retrieves the current time using `strftime('%I:%M:%S %p')`:
     - `%I`: Displays the hour in 12-hour format.
     - `%M`: Displays minutes.
     - `%S`: Displays seconds.
     - `%p`: Displays `AM` or `PM`.
   - The retrieved time is set as the text for the clock `label` using `label.config(text=current_time)`.
   - `label.after(200, update_time)` ensures the function is called again every 200 milliseconds, creating a continuous update loop.

3. **Creating the Main Window**
   - `tk.Tk()` initializes the main application window, and `root.title("Digital Clock")` sets the title of the window.

4. **Configuring the Clock Label**
   - A `Label` widget is created to display the time:
     - `font=('times new roman', 150)`: Sets the font to **Times New Roman** with a font size of 150.
     - `background='white'`: Sets the background color of the label to white.
     - `foreground='black'`: Sets the text color to black.
   - `label.pack(anchor='center')` centers the label in the application window.

5. **Starting the Clock**
   - The `update_time` function is called initially to set the time and start the update loop.

6. **Running the Application**
   - `root.mainloop()` starts the Tkinter event loop, keeping the application window open until it is manually closed.

---

## Requirements

- **Python 3.x**: Tkinter is included with Python by default. No additional libraries are required.

---

## How to Run

1. Copy the code into a file named `digital_clock.py`.
2. Open a terminal or command prompt.
3. Run the script using:
   ```bash
   python3 digital_clock.py
