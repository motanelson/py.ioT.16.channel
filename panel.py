import tkinter as tk
import os

WIN_W = 800
WIN_H = 600
CELLS_PER_ROW = 4
CELLS_PER_COL = 4
CELL_SIZE = 50
GAP = 10

# estados iniciais (todos 0)
states = [0] * (CELLS_PER_ROW * CELLS_PER_COL)

class GridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Janela Amarela")
        self.root.geometry(f"{WIN_W}x{WIN_H}")
        self.root.configure(bg="yellow")

        self.canvas = tk.Canvas(root, width=WIN_W, height=WIN_H, bg="yellow", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.cells = []
        self.draw_grid()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_grid(self):
        grid_w = CELLS_PER_ROW * CELL_SIZE + (CELLS_PER_ROW - 1) * GAP
        grid_h = CELLS_PER_COL * CELL_SIZE + (CELLS_PER_COL - 1) * GAP
        start_x = (WIN_W - grid_w) // 2
        start_y = (WIN_H - grid_h) // 2

        self.cells.clear()
        self.canvas.delete("all")

        for r in range(CELLS_PER_COL):
            for c in range(CELLS_PER_ROW):
                idx = r * CELLS_PER_ROW + c
                x1 = start_x + c * (CELL_SIZE + GAP)
                y1 = start_y + r * (CELL_SIZE + GAP)
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                color = "black" if states[idx] else "white"
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                self.cells.append(rect)

    def on_click(self, event):
        for idx, rect in enumerate(self.cells):
            coords = self.canvas.coords(rect)
            if coords[0] <= event.x <= coords[2] and coords[1] <= event.y <= coords[3]:
                # alterna estado
                states[idx] = 1 - states[idx]
                new_color = "black" if states[idx] else "white"
                self.canvas.itemconfig(rect, fill=new_color)

                # chama comando
                cmd = f"command{idx+1} {states[idx]}"
                os.system(cmd)
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = GridApp(root)
    root.mainloop()
