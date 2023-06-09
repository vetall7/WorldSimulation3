from Main.World import World
import tkinter as tk
from tkinter import ttk
import pygame
from pygame.locals import *
from Main.Organism import Organism
from Animals.Animal import Animal
from Main.directions import Direction
from Plants.Plant import Plant


class HexWorld(World):
    def DrawWorld(self, generate):
        CELL_SIZE = 50

        # Размеры доски
        BOARD_SIZE = (self._width, self._height)

        # Цвета клеток
        WHITE_COLOR = (255, 255, 255)
        BLACK_COLOR = (0, 0, 0)
        RED_COLOR = (255, 0, 0)
        GREEN_COLOR = (0, 255, 0)
        BLUE_COLOR = (0, 0, 255)
        YELLOW_COLOR = (255, 255, 0)

        # Инициализация Pygame
        pygame.init()

        # Создание окна
        window_width = BOARD_SIZE[0] * CELL_SIZE + self.width*CELL_SIZE/2
        window_height = BOARD_SIZE[1] * CELL_SIZE + 100  # Increased height for the text area
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Шахматная доска")

        # Создание поверхности для доски и текста
        board_surface = pygame.Surface((window_width, window_height - 100))
        text_surface = pygame.Surface((window_width, 100))

        # Очистка экрана
        board_surface.fill(WHITE_COLOR)
        text_surface.fill(WHITE_COLOR)
        move = 0
        move_y = 0
        for row in range(BOARD_SIZE[1]):
            for col in range(BOARD_SIZE[0]):
                x = col * CELL_SIZE + move
                y = row * CELL_SIZE - move_y

                # Определение цвета шестиугольника
                if isinstance(self._board[row][col], Animal):
                    color = RED_COLOR
                elif isinstance(self._board[row][col], Plant):
                    color = BLUE_COLOR
                else:
                    color = WHITE_COLOR

                # Расчет вершин шестиугольника
                points = [
                    (x + CELL_SIZE // 2, y),
                    (x + CELL_SIZE, y + CELL_SIZE // 4),
                    (x + CELL_SIZE, y + CELL_SIZE * 3 // 4),
                    (x + CELL_SIZE // 2, y + CELL_SIZE),
                    (x, y + CELL_SIZE * 3 // 4),
                    (x, y + CELL_SIZE // 4)
                ]

                # Отрисовка шестиугольника
                pygame.draw.polygon(board_surface, color, points)
                pygame.draw.polygon(board_surface, BLACK_COLOR, points, 1)
                if self._board[row][col] is not None:
                    symbol_font = pygame.font.SysFont(None, 30)
                    symbol_text = symbol_font.render(self._board[row][col].sign, True, BLACK_COLOR)
                    symbol_rect = symbol_text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                    board_surface.blit(symbol_text, symbol_rect)
            move += CELL_SIZE/2
            move_y += CELL_SIZE/4
        # Отображение текста
        font_size = 20
        font = pygame.font.SysFont(None, font_size)
        for index, comment in enumerate(self._comments):
            text_surface.blit(font.render(comment, True, BLACK_COLOR), (10, font_size * index))

        text_surface.blit(font.render("Turn number " + str(self._turn), True, BLACK_COLOR), (300, font_size))
        # Обновление экрана
        screen.blit(board_surface, (0, 0))
        screen.blit(text_surface, (0, window_height - 100))
        pygame.display.flip()
        # Ожидание нажатия клавиши
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if hasattr(event, 'key'):
                        if event.key == K_UP:
                            self._human.direction = Direction.TURN_UP
                        elif event.key == K_DOWN:
                            self._human.direction = Direction.TURN_DOWN
                        elif event.key == K_RIGHT:
                            self._human.direction = Direction.TURN_RIGHT
                        elif event.key == K_LEFT:
                            self._human.direction = Direction.TURN_LEFT
                        elif event.key == K_RETURN:
                            self._human.direction = Direction.TURN_SUPER
                        elif event.key == K_s:
                            generate.SaveGame()
                            continue
                        else:
                            self._human.direction = Direction.TURN_NONE
                        self.Turn()
                        self.DrawWorld(generate)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Левая кнопка мыши
                        mouse_pos = pygame.mouse.get_pos()  # Получить координаты мыши
                        # Проверить, попали ли координаты мыши в клетку доски
                        clicked_row = mouse_pos[1] // CELL_SIZE
                        clicked_col = mouse_pos[0] // CELL_SIZE

                        def handle_selection(event):
                            selected_item = dropdown.get()
                            window.destroy()
                            if self._board[clicked_row][clicked_col] == None:
                                org = self._NewOrganism(selected_item, clicked_col, clicked_row)
                                self.AddOrganism(org)
                                self.DrawWorld(generate)

                        # Создание главного окна
                        window = tk.Tk()
                        window.title("Выпадающий список")

                        # Создание выпадающего списка
                        dropdown = ttk.Combobox(window,
                                                values=["Antelope", "Fox", "Wolf", "Turtle", "Sheep", "Belladonna",
                                                        "Dandelion", "Grass", "Guarana", "SosmowskiHogweed"])
                        dropdown.bind("<<ComboboxSelected>>", handle_selection)
                        dropdown.current(1)
                        dropdown.pack()
                        window.eval('tk::PlaceWindow . center')

                        # Запуск главного цикла событий
                        window.mainloop()
            pygame.time.Clock().tick(30)

    def FindNeighbours(self, org, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if org.y + i >= 0 and org.y + i < self.height and org.x + j >= 0 and org.x + j < self.width and self.GetPoint(
                        org.x + j, org.y + i) is not None and isinstance(
                    self.GetPoint(org.x + j, org.y + i), Animal):
                    x.append(org.x + j)
                    y.append(org.y + i)

    def FindPoints(self, org, x, y):
        x_coo = org.x
        y_coo = org.y
        if (y_coo - 1 >= 0 and self.GetPoint(x_coo, y_coo - 1) == None):
            x.append(x_coo)
            y.append(y_coo - 1)
        if (x_coo + 1 < self.width and self.GetPoint(x_coo + 1, y_coo) == None):
            x.append(x_coo + 1)
            y.append(y_coo)
        if (y_coo + 1 < self.height and self.GetPoint(x_coo, y_coo + 1) == None):
            x.append(x_coo)
            y.append(y_coo + 1)
        if (x_coo - 1 >= 0 and self.GetPoint(x_coo - 1, y_coo) == None):
            x.append(x_coo - 1)
            y.append(y_coo)