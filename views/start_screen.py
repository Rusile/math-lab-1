import threading
import time
import tkinter as tk
from tkinter import ttk
from controllers import calculations
from models.ScreenSizes import ScreenSizes
from models.Vertice import Vertice


class StartScreen:
    vertices = []
    start_x, start_y, canvas, root, repetitions = None, None, None, None, 1
    entry = None
    entry1 = None
    label1 = None
    label_result = None

    def __init__(self, screen_sizes: ScreenSizes):
        self.screen_sizes = screen_sizes

    
    def on_select(self, v):
        """Запись движения ползунка"""
        self.repetitions = v

    def run(self):
        """Запуск расчета"""
        res, err = calculations.run(self.vertices, self.repetitions, self.screen_sizes, self.root)
        self.label_result['text'] = f"Integral: {round(res, 4)}\nError: {round(float(str(err).split('(')[1].split(',')[0]), 4)}"

    def add_new(self):
        self.vertices.append(Vertice(float(self.entry.get()), float(self.entry1.get())))
        text = '     Points:\n'
        idx = 0
        for i in self.vertices:
            idx += 1
            text += f"№{idx}: x: {i.x}, y: {i.y}\n"
        self.label1['text'] = text

    def clear(self):
        self.vertices = []
        self.label1['text'] = ''


    def launch(self):
        """Отрисовка экрана"""
        self.root = tk.Tk()
        self.root.title("Rusile | Math-lab-1")
        self.root.config(cursor="pencil")
        self.root.geometry(
            f"{self.screen_sizes.screen_size_width}x{self.screen_sizes.screen_size_height}"
        )
        self.func = ttk.Label(text="Func: x^3 + y^3 + x")
        self.func.pack()
        self.label1 = ttk.Label()
        self.label1.pack()
        self.labelx = ttk.Label(text="X: ")
        self.labelx.pack()
        self.entry = tk.Entry()
        self.entry.pack()
        self.labely = ttk.Label(text="Y: ")
        self.labely.pack()
        self.entry1 = tk.Entry()
        self.entry1.pack()
        tk.Button(text="submit", command=self.add_new).pack()
        tk.Button(text="clear", command=self.clear).pack()
        scale = tk.Scale(
            self.root, from_=1, to=50, orient="horizontal", command=self.on_select
        )
        scale.pack()
        
        run_button = tk.Button(self.root, text="Run", command=self.run)
        run_button.pack()

        self.label_result = ttk.Label()
        self.label_result.pack()

        self.root.mainloop()
