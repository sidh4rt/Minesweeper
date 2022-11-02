from tkinter import Button, Label
import random
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    def __init__(self, x, y, is_mine = False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
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
        )
        btn.bind('<Button-1>', self.left_click_actions ) #left click
        btn.bind('<Button-3>', self.right_click_actions ) #right click
        self.cell_btn_object = btn

    @staticmethod
    #to display the amount of cells left in the game
    #create text element in window and call it from main.py
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='#00909E',
            fg='white',
            text = f"Cells Left:{Cell.cell_count}",
            height=4,
            width=12,
            font=("",28)
        )
        Cell.cell_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()

            #if cells left count == mines count, player won
            if Cell.cell_count == settings.MINES_COUNT:
                ctypes.windll.user32.MessageBoxW(0, 'You WON! :D', 'Game Over!', 0)

        #Cancel left and right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axes(self, x, y):
        #return cell object based on value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    #to get the surrounded cell objects
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axes(self.x -1, self.y -1),
            self.get_cell_by_axes(self.x -1, self.y),
            self.get_cell_by_axes(self.x -1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y -1),
            self.get_cell_by_axes(self.x + 1, self.y -1),
            self.get_cell_by_axes(self.x + 1, self.y),
            self.get_cell_by_axes(self.x + 1, self.y + 1),
            self.get_cell_by_axes(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    #count mines in around the clicked cell
    def surrounded_cells_mines_length(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count+=1
            
        return count

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
            #replace text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text = f"Cells Left:{Cell.cell_count}")
            #if this was a mine candidate, configure bg to SystemButtonFace for safety
            self.cell_btn_object.configure(bg='SystemButtonFace')

        #mark the cell as opened (use it as last line of this method)
        self.is_opened = True

    def show_mine(self):
        # interrupt game and display message that player lost
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You clicked on a Mine :(', 'Game Over!', 0)
        sys.exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"