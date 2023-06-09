import tkinter as tk
from Main.SimpleWorld import SimpleWorld
from Main.HexWorld import HexWorld
from Main.WorldGenerator import WorldGenerator
from tkinter import messagebox

def new_world():
    window.destroy()
    def create_world():
        width = int(width_entry.get())
        height = int(height_entry.get())
        root.destroy()
        world = HexWorld(height, width)
        generate = WorldGenerator(world)
        generate.Generate()
        world.DrawWorld(generate)
        root.destroy()

    root = tk.Tk()
    root.title("Диалоговое окно")
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

    button = tk.Button(frame, text="Generate World", font=("Arial", 12), bg = "yellow", command=create_world)
    button.pack(pady=30)

    root.eval('tk::PlaceWindow . center')
    root.mainloop()


def saved_world():
    window.destroy()
    world = SimpleWorld(0,0)
    generate = WorldGenerator(world)
    world = generate.ReadGame()
    world.DrawWorld(generate)

# Создание главного окна
window = tk.Tk()
window.title("Диалоговое окно")
window.geometry("300x250")  # Размер окна
window.configure(bg="darkblue")  # Цвет фона окна

# Создание надписи с жирным шрифтом, измененным цветом текста и фона
label = tk.Label(window, text="WORLD GAME SIMULATION", font=("Helvetica", 14, "bold"), fg="white", bg="darkblue")
label.pack(pady=10)  # Размещение надписи с отступом

# Создание контейнера для кнопок
button_frame = tk.Frame(window, bg="darkblue")
button_frame.pack(pady=10)  # Отступ между контейнером и надписью

# Создание кнопок с овальной формой, увеличенными размерами и отступом
button1 = tk.Button(button_frame, text="NEW GAME", command=new_world, bg="blue", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)
button2 = tk.Button(button_frame, text="LOAD GAME", command=saved_world, bg="green", fg="white", font=("Arial", 12, "bold"), padx=20, pady=10)

# Применение овальной формы кнопок
button1.config(relief=tk.SOLID, bd=0)  # Убираем границу кнопки
button1.pack(pady=10)  # Отступ между кнопками
button2.config(relief=tk.SOLID, bd=0)
button2.pack(pady=10)

# Центрирование окна на экране
window.eval('tk::PlaceWindow . center')

# Запуск главного цикла обработки событий
window.mainloop()
