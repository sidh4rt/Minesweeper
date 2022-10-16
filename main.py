from email import utils
from tkinter import *
from turtle import left
import settings
import utils

root = Tk()
#override settings of window
root.configure(bg="#52616B")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg = 'red', #change to black or something
    width = settings.WIDTH,
    height = utils.height_perc(25)
)

top_frame.place(x=0, y=0)

left_frame = Frame (
    root,
    bg = 'blue', #change to something else
    width = utils.width_perc(25),
    height = utils.height_perc(75)
)
left_frame.place(x=0, y=utils.height_perc(25))

center_frame = Frame (
    root,
    bg='green', #change later to something
    width=utils.width_perc(75),
    height=utils.height_perc(75)
)
center_frame.place(x=utils.width_perc(25), y=utils.height_perc(25))
#run the window
root.mainloop()