from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
#override settings of window
root.configure(bg="#394867")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = '#14274E', #change to black or something
    width = settings.WIDTH,
    height = utils.height_perc(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='#14274E',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)
game_title.place(x=utils.width_perc(25), y=0)

left_frame = Frame (
    root,
    bg = '#00909E', #change to something else
    width = utils.width_perc(25),
    height = utils.height_perc(75)
)
left_frame.place(x=0, y=utils.height_perc(25))

center_frame = Frame (
    root,
    bg='#F0F5F9', #change later to something
    width=utils.width_perc(75),
    height=utils.height_perc(75)
)
center_frame.place(x=utils.width_perc(25), y=utils.height_perc(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

#run the window
root.mainloop()