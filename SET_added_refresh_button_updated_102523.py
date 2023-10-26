import tkinter as tk
import random
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Set")

# Set the background color
root.configure(bg="light blue")

# Specify the directory containing the images
image_dir = "C:\\Users\\Ryan Fernald\\Documents\\SpyderProjects\\SET\\cards"

# Get a list of all image files in the directory
image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

# Create a 3x4 grid of buttons with gaps and borders
buttons = []
for row in range(3):
    for col in range(4):
        # Choose a random image file
        image_file = random.choice(image_files)
        # Load the image
        image = Image.open(os.path.join(image_dir, image_file))
        # Resize the image
        image = image.resize((200, 150), Image.LANCZOS)
        # Convert it to a format Tkinter can use
        img = ImageTk.PhotoImage(image)
        button = tk.Button(root, image=img, width=200, height=150, bd=13, relief="groove")
        # Keep a reference of the image and its filename
        button.image = img
        button.image_name = image_file
        button.grid(row=row, column=col, padx=5, pady=5)
        buttons.append(button)

# Add extra rows and columns that take up remaining space
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

# Define a function to handle button clicks
def button_click(button):
    if button["relief"] == "sunken":
        button.config(relief="groove")
    else:
        button.config(relief="sunken")
    if sum(button["relief"] == "sunken" for button in buttons) == 3:
        image_names = [os.path.splitext(button.image_name)[0] for button in buttons if button["relief"] == "sunken"]
        print(f"Image names: {image_names}")
        for button in buttons:
            if button["relief"] == "sunken":
                # Choose a random image file
                image_file = random.choice(image_files)
                # Load the image
                image = Image.open(os.path.join(image_dir, image_file))
                # Resize the image
                image = image.resize((200, 150), Image.LANCZOS)
                # Convert it to a format Tkinter can use
                img = ImageTk.PhotoImage(image)
                # Update the button's image and keep a reference of the image and its filename
                button.config(image=img, relief="groove")
                button.image = img
                button.image_name = image_file

# Bind the button click function to each button
for button in buttons:
    button.config(command=lambda b=button: button_click(b))

# Define a function to refresh all images on buttons
def refresh_images():
    for button in buttons:
        # Choose a random image file
        image_file = random.choice(image_files)
        # Load the image
        image = Image.open(os.path.join(image_dir, image_file))
        # Resize the image
        image = image.resize((200, 150), Image.LANCZOS)
        # Convert it to a format Tkinter can use
        img = ImageTk.PhotoImage(image)
        # Update the button's image and keep a reference of the image and its filename
        button.config(image=img)
        button.image = img
        button.image_name = image_file

# Load an icon for the refresh button from a specific file location.
refresh_icon_image_path = "C:\\Users\\Ryan Fernald\\Documents\\SpyderProjects\\SET\\other\\refresh.png"
refresh_icon_image = Image.open(refresh_icon_image_path)
refresh_icon_image_resized = refresh_icon_image.resize((200, 150), Image.LANCZOS)
refresh_icon_img = ImageTk.PhotoImage(refresh_icon_image_resized)

# Add a refresh button to the right of your grid of buttons.
refresh_button = tk.Button(root, command=refresh_images,
                           height=150, width=200,
                           compound=tk.TOP,
                           relief="groove",
                           bd=13,
                           repeatdelay=1000,
                           repeatinterval=100,
                           takefocus=True,
                           image=refresh_icon_img)
refresh_button.image = refresh_icon_img
refresh_button.grid(row=2, column=5)

root.mainloop()
