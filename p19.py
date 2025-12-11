from tkinter import *

def main():
    win01 = Tk()
    win01.geometry('800x800')
    win01.title('p19')
    wcan = Canvas(win01, bg = 'white', width = 700, height = 700)
    wcan.pack()
    wcan.create_oval(93, 75, 600, 600,
                     fill = 'white', outline = 'black', width = 5)
    wcan.create_oval(200, 200, 300, 270,
                     fill = 'red', outline = 'black', width = 5)
    wcan.create_oval(400, 200, 500, 270,
                     fill = 'blue', outline = 'black', width = 5)
    wcan.create_rectangle(230, 320, 450, 340,
                     fill = 'yellow', outline = 'black', width = 5)
    wcan.create_arc(230, 500, 450, 350,
                     fill = 'green',
                    start = 180, extent = 180, outline = 'black', width = 5)

    win01.mainloop()

main()
