import tkinter as tk

root = tk.Tk()
root.title("Set")

# Set the background color
root.configure(bg="light blue")

# Create a 3x4 grid of buttons with gaps and borders
buttons = []
for row in range(3):
    for col in range(4):
        button = tk.Button(root, text="", width=20, height=10, bd=2, relief="groove")
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons.append(button)

# Define a function to handle button clicks
def button_click(button):
    if button["relief"] == "sunken":
        button.config(relief="groove")
    else:
        button.config(relief="sunken")
    if sum(button["relief"] == "sunken" for button in buttons) == 3:
        data = [[button.grid_info()["row"], button.grid_info()["column"]] for button in buttons if button["relief"] == "sunken"]
        print(f"Button locations: {data}")
        for button in buttons:
            button.config(relief="groove")

# Bind the button click function to each button
for button in buttons:
    button.config(command=lambda b=button: button_click(b))

root.mainloop()
