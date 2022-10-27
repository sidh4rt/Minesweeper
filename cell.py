from tkinter import Button

class Cell:
    def __init__(self, is_Mine=False) :
        self.is_Mine = is_Mine
        self.cell_btn_object = None

    def create_btn_object (self, location) :
        btn = Button (
            location,
            text='TEXT'
        )
        btn.bind('<Button-1>', self.left_click_actions ) #left click
        btn.bind('<Button-3>', self.right_click_actions ) #right click
        self.cell_btn_object = btn
        
    def left_click_actions(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")