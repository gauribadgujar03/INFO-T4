import tkinter as tk
from tkinter import messagebox, Scrollbar, Listbox, Entry, Button, Text, END, PhotoImage, filedialog
from tkinter.simpledialog import askstring
from PIL import Image, ImageTk
import os

class ChatApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat Application")

        self.chat_history = []

        self.chat_list = Listbox(master, width=50)
        self.chat_list.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        scrollbar = Scrollbar(master, orient="vertical", command=self.chat_list.yview)
        scrollbar.grid(row=0, column=2, rowspan=3, sticky="ns")

        self.chat_list.config(yscrollcommand=scrollbar.set)

        self.entry_field = Entry(master, width=50)
        self.entry_field.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        send_button = Button(master, text="Send", command=self.send_message)
        send_button.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        attach_button = Button(master, text="Attach Image", command=self.attach_image)
        attach_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.message_area = Text(master, width=50, height=10)
        self.message_area.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

        self.message_area.config(state=tk.DISABLED)

        self.username = askstring("Username", "Please enter your username:")

        if self.username:
            self.master.title(f"Chat Application - {self.username}")

    def send_message(self):
        message = self.entry_field.get()
        if message:
            self.display_message(f"{self.username}: {message}")
            self.chat_history.append(f"{self.username}: {message}")
            self.entry_field.delete(0, END)

    def display_message(self, message):
        self.message_area.config(state=tk.NORMAL)
        self.message_area.insert(END, message + "\n")
        self.message_area.config(state=tk.DISABLED)

    def attach_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, image_path):
        # Resize the image to fit in the chat window if needed
        max_width = 300
        max_height = 200
        img = Image.open(image_path)
        img.thumbnail((max_width, max_height))

        # Display the image in the chat window
        photo = ImageTk.PhotoImage(img)
        self.chat_list.image_create(END, image=photo)

root = tk.Tk()
app = ChatApplication(root)
root.mainloop()