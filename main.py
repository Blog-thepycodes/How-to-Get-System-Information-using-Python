import platform
from datetime import datetime
import tkinter as tk
from tkinter import ttk
 
 
def get_system_information():
   """
   Retrieves and returns system information.
   """
   system_info = platform.uname()
   info_text = (
       f"System: {system_info.system}\n"
       f"Node Name: {system_info.node}\n"
       f"Release: {system_info.release}\n"
       f"Version: {system_info.version}\n"
       f"Machine: {system_info.machine}\n"
       f"Processor: {system_info.processor}"
   )
   return info_text
 
 
def show_system_information():
   """
   Displays system information in a Tkinter window.
   """
   # Create the main window
   window = tk.Tk()
   window.title("System Information - The Pycodes")
 
 
   # Create a label to display system information
   info_label = ttk.Label(window, wraplength=400, font=("Arial", 12))
   info_label.grid(row=0, column=0, padx=20, pady=20)
 
 
   # Set the label text with system information
   info_text = get_system_information()
   info_label.config(text=info_text)
 
 
   # Create a button to show the current date and time
   date_time_button = ttk.Button(window, text="Show Date and Time", command=show_date_time)
   date_time_button.grid(row=1, column=0, pady=10)
 
 
   # Run the Tkinter event loop
   window.mainloop()
 
 
def show_date_time():
   """
   Displays the current date and time in a new Tkinter window.
   """
   # Create a new window for date and time
   dt_window = tk.Toplevel()
   dt_window.title("Current Date and Time")
 
 
   # Create a label to display the current date and time
   dt_label = ttk.Label(dt_window, text=f"Current Date and Time: {datetime.now()}", font=("Arial", 12))
   dt_label.pack(padx=20, pady=20)
 
 
if __name__ == "__main__":
   # Call the function to show system information
   show_system_information()
