import tkinter as tk
import pyjokes
root = tk.Tk()
root.title('Jokes');
root.geometry("400x200")
root.configure(bg="black")
root.title('jokes')

def joke():
     T.delete("1.0", "end")
     global joke
     joke = pyjokes.get_joke()
     T.insert(tk.END, joke)

if __name__ == '__main__':
     T = tk.Text(root)
     T.place(x=10, y=5, height=80, width=380)
     b = tk.Button(root, text="Tell me joke", fg="white", bg="blue", command=joke)
     b.place(x=150, y=100, height=40, width=100)
     root.mainloop()
