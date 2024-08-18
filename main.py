import tkinter as tk
from tkinter import messagebox
import pyperclip
import string
from random import choice


# Logic

def save_pw():
  website = website_input.get()
  email = email_input.get()
  password = password_input.get()
  if not website or not email or not password:
    messagebox.showinfo(title='Oops!', message='You left some fields empty')
  else:
    is_ok = messagebox.askokcancel(title='Confirm Save', message='Do you want to confirm saving these info?')
    if is_ok:
      with open('data.txt', mode='a') as file:
        file.write(f'{website} | {email} | {password}\n')
      website_input.delete(0, tk.END)
      email_input.delete(0, tk.END)
      password_input.delete(0, tk.END)

def generate_pw():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
  password = ''.join(choice(chars) for _ in range(12))
  password_input.delete(0, tk.END)
  password_input.insert(0, password)
  pyperclip.copy(password)
  messagebox.showinfo(title='Info', message='Password copied')
# 

window = tk.Tk()
window.title('MyPass')
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=200, height=200)
logo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = tk.Label(text='Website:')
website_label.grid(column=0, row=1)
website_input = tk.Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = tk.Label(text='Email:')
email_label.grid(column=0, row=2)
email_input = tk.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_label = tk.Label(text='Password:')
password_label.grid(column=0, row=3)
password_input = tk.Entry(show='*',width=21)
password_input.grid(column=1, row=3)

generate_pw = tk.Button(text='Generate Password', command=generate_pw)
generate_pw.grid(column=2, row=3, columnspan=2)

add = tk.Button(text='Add', width=36, command=save_pw)
add.grid(column=1, row=4, columnspan=2)






window.mainloop()

