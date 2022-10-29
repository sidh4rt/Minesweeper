from tkinter import Button
import random
import settings

class Cell:
    all = []
    def __init__(self, x, y, is_Mine=False) :
        self.is_Mine = is_Mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #append the object to Cell.all
        Cell.all.append(self)

    def create_btn_object (self, location) :
        btn = Button (
            location,
            height=4,
            width=12,
            text = f"({self.x}, {self.y})"
        )
        btn.bind('<Button-1>', self.left_click_actions ) #left click
        btn.bind('<Button-3>', self.right_click_actions ) #right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_Mine:
            self.show_Mine()
        else:
            self.show_cell()

    def get_cell_by_axes(self,x,y):
        #return cell object based on value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    def show_cell(self):
        surrounded_cells = [
            self.get_cell_by_axes(self.x -1, self.y -1),
            self.get_cell_by_axes(self.x -1, self.y),
            self.get_cell_by_axes(self.x -1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y -1),
            self.get_cell_by_axes(self.x + 1, self.y -1),
            self.get_cell_by_axes(self.x + 1, self.y),
            self.get_cell_by_axes(self.x + 1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y + 1)
        ]
        print (surrounded_cells)

    def show_Mine(self):
        # interrupt game and display message that player lost
        self.cell_btn_object.configure(bg='red')

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_Mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"