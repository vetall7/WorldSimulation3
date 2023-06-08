import tkinter as tk
from Main.World import World
from Main.WorldGenerator import WorldGenerator

def get_values():
    width = int(width_entry.get())
    height = int(height_entry.get())
    world = World(height, width)
    generate = WorldGenerator(world)
    generate.Generate()
    world.DrawWorld()
    root.destroy()


root = tk.Tk()
root.title("Диалоговое окно")
root.geometry("300x150")

width_label = tk.Label(root, text="Ширина:")
width_label.pack()

width_entry = tk.Entry(root)
width_entry.pack()

height_label = tk.Label(root, text="Высота:")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

button = tk.Button(root, text="Получить значения", command=get_values)
button.pack()

root.mainloop()

