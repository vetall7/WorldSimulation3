from abc import ABC, abstractmethod
import tkinter as tk
import pygame

from Main.Organism import Organism
from Animals.Animal import Animal
from Plants.Plant import Plant

# Rest of the code...

class World():
    def __init__(self, height, width):
        self._height = height
        self._width = width
        self._turn = 0
        self._organisms = []
        self._comments = []
        self._board = [[None] * width for _ in range(height)]
        self._human = None
        self._CellNeighboursCounter = None
        self._cellSize = 50

    @property
    def turn(self):
        return self._turn

    @turn.setter
    def turn(self, value):
        self._turn = value

    @property
    def human(self):
        return self._human

    @human.setter
    def human(self, value):
        self._human = value

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def CellNeighboursCounter(self):
        return self._CellNeighboursCounter

    def get_org_counter(self):
        return len(self._organisms)

    @property
    def organisms(self):
        return self._organisms
    def __SetPoint(self, x, y, organism):
        self._board[organism.y][organism.x] = organism
    def AddOrganism(self, organism):
        self._organisms.append(organism)
        self.__SetPoint(organism.x, organism.y, organism)
    def DrawWorld(self):
            # Размеры клетки
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
            window_size = (BOARD_SIZE[0] * CELL_SIZE, BOARD_SIZE[1] * CELL_SIZE)
            screen = pygame.display.set_mode(window_size)
            pygame.display.set_caption("Шахматная доска")

            # Очистка экрана
            screen.fill(WHITE_COLOR)

            # Отрисовка клеток доски
            for row in range(BOARD_SIZE[1]):
                for col in range(BOARD_SIZE[0]):
                    x = col * CELL_SIZE
                    y = row * CELL_SIZE
                    # Определение цвета клетки
                    if isinstance(self._board[row][col], Animal):
                        color = RED_COLOR
                    elif isinstance(self._board[row][col], Plant):
                        color = BLUE_COLOR
                    else:
                        color = WHITE_COLOR

                    # Отрисовка клетки
                    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
                    if self._board[row][col] != None:
                        symbol_font = pygame.font.SysFont(None, 30)
                        symbol_text = symbol_font.render(self._board[row][col].sign, True,
                                                         BLACK_COLOR)  # Замените "Символ" на нужный символ
                        symbol_rect = symbol_text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                        screen.blit(symbol_text, symbol_rect)

            # Обновление экрана
            pygame.display.flip()

            # Ожидание нажатия клавиши
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    elif event.type == pygame.KEYDOWN:
                        return

                pygame.time.Clock().tick(30)
    def GetPoint(self, x, y):
        return self._board[y][x]

    def FindPoints(self, org, x, y):
        x_coo = org.x
        y_coo = org.y
        if (y_coo-1 >= 0 and self.GetPoint(x_coo, y_coo-1) == None):
            x.append(x_coo)
            y.append(y_coo-1)
        if (x_coo + 1 < self.width and self.GetPoint(x_coo+1, y_coo) == None):
            x.append(x_coo + 1)
            y.append(y_coo)
        if (y_coo + 1 < self.height and self.GetPoint(x_coo, y_coo + 1) == None):
            x.append(x_coo)
            y.append(y_coo + 1)
        if (x_coo-1 >= 0 and self.GetPoint(x_coo-1, y_coo) == None):
            x.append(x_coo-1)
            y.append(y_coo)
