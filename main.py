import tkinter as tk
from Main.SimpleWorld import SimpleWorld
from Main.HexWorld import HexWorld
from Main.WorldGenerator import WorldGenerator
from tkinter import messagebox

def choose_world(width, height):
    def create_hex_world():
        window2.destroy()
        world = HexWorld(height, width)
        generate = WorldGenerator(world)
        generate.Generate()
        world.DrawWorld(generate)

    def create_simple_world():
        window2.destroy()
        world = SimpleWorld(height, width)
        generate = WorldGenerator(world)
        generate.Generate()
        world.DrawWorld(generate)

    window2 = tk.Tk()
    window2.title("Vitalii Shapovalov 196633")
    window2.geometry("300x250")
    window2.configure(bg="darkblue")

    label = tk.Label(window2, text="CHOOSE THE WORLD", font=("Helvetica", 14, "bold"), fg="white", bg="darkblue")
    label.pack(pady=10)


    button_frame = tk.Frame(window2, bg="darkblue")
    button_frame.pack(pady=10)


    button1 = tk.Button(button_frame, text="SIMPLE WORLD", command=create_simple_world, bg="blue", fg="white",
                        font=("Arial", 12, "bold"), padx=20, pady=10)
    button2 = tk.Button(button_frame, text="HEX WORLD", command=create_hex_world, bg="green", fg="white",
                        font=("Arial", 12, "bold"), padx=20, pady=10)


    button1.config(relief=tk.SOLID, bd=0)
    button1.pack(pady=10)
    button2.config(relief=tk.SOLID, bd=0)
    button2.pack(pady=10)


    window2.eval('tk::PlaceWindow . center')


    window2.mainloop()


def new_world():
    window.destroy()

    root = tk.Tk()
    root.title("Vitalii Shapovalov 196633")
    root.geometry("400x250")
    root.configure(bg="darkblue")

    frame = tk.Frame(root, bg="darkblue")
    frame.pack(padx=20, pady=20)

    width_label = tk.Label(frame, text="Width:", bg="darkblue", fg="white", font=("Arial", 15))
    width_label.pack()

    width_entry = tk.Entry(frame, font=("Arial", 16))
    width_entry.pack()

    height_label = tk.Label(frame, text="Height:", bg="darkblue", fg="white", font=("Arial", 15))
    height_label.pack()

    height_entry = tk.Entry(frame, font=("Arial", 16))
    height_entry.pack()

    button = tk.Button(frame, text="Generate World", font=("Arial", 12), bg="yellow", command=lambda: choose_world(int(width_entry.get()), int(height_entry.get())))
    button.pack(pady=30)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def saved_world():
    window.destroy()
    world = SimpleWorld(0,0)
    generate = WorldGenerator(world)
    world = generate.ReadGame()
    world.DrawWorld(generate)


window = tk.Tk()
window.title("Vitalii Shapovalov 196633")
window.geometry("300x250")
window.configure(bg="darkblue")


label = tk.Label(window, text="WORLD GAME SIMULATION", font=("Helvetica", 14, "bold"), fg="white", bg="darkblue")
label.pack(pady=10)


button_frame = tk.Frame(window, bg="darkblue")
button_frame.pack(pady=10)


button1 = tk.Button(button_frame, text="NEW GAME", command=new_world, bg="blue", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
button2 = tk.Button(button_frame, text="LOAD GAME", command=saved_world, bg="green", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)

button1.config(relief=tk.SOLID, bd=0)
button1.pack(pady=10)
button2.config(relief=tk.SOLID, bd=0)
button2.pack(pady=10)


window.eval('tk::PlaceWindow . center')

window.mainloop()
