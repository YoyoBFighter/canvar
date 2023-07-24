import tkinter as tk


window = tk.Tk()
window.title("first window")
window.geometry("800x600")

canvas = tk.Canvas(window,
                   width=100
                   ,height=200,
                   bg="navy")

canvas.create_line(0,100,500,100,fill="red")

canvas.create_rectangle(0,0,100,100,fill="yellow")

canvas.create_text(50,50,text="hello",fill="black")




canvas.pack()

window.mainloop()