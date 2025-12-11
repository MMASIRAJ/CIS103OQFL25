from tkinter import *

def lbl(winmain):
    lbl01 = Label(winmain, text = 'Temperature Converstion', font = ('Times New Roman', 20),
                  fg = 'red')
    lbl01.place(x = 200, y = 0)
    lbl02 = Label(winmain, text = 'Kelvin: ', font = ('Times New Roma', 20), fg = 'blue')
    lbl02.place(x = 1, y = 100)
    lbl03 = Label(winmain, text = 'Celcius: ', font = ('Times New Roma', 20), fg = 'blue')
    lbl03.place(x = 1, y = 150)
    lbl04 = Label(winmain, text = 'Fahrenheit: ', font = ('Times New Roma', 20), fg = 'blue')
    lbl04.place(x = 1, y = 200)

def k(winmain):
    txtbox_01 = Entry(winmain, font = ('Times New Roman', 20), fg = 'purple')
    txtbox_01.place(x = 200, y = 100)
    return txtbox_01


def txtbox(winmain):
    celsius = Entry(winmain, font = ('Times New Roman', 20), fg = 'purple')
    celsius.place(x = 200, y = 150)
    return celsius
def txtbox02(winmain):
    f = Entry(winmain, font = ('Times New Roman', 20), fg = 'purple')
    f.place(x = 200, y = 200)
    return f

def clr(k,txtbox,txtbox02):
    k.delete(0,'end')
    txtbox.delete(0,'end')
    txtbox02.delete(0,'end')

def cal(kelvin_entry, celsius_entry, fah_entry):
    try:
        kelvin = float(kelvin_entry.get())
        if kelvin < 0:
            fah_entry.delete(0, END)
            fah_entry.insert(0, "Invalid")
            celsius_entry.delete(0, END)
            celsius_entry.insert(0, "Invalid")
        else:
            celcius = kelvin - 273.15
            f = (9/5)*(kelvin - 273)+32
            fah_entry.delete(0, END)
            fah_entry.insert(0, str(round(f, 2)))
            celsius_entry.delete(0, END)
            celsius_entry.insert(0, str(round(celcius, 2)))
    except ValueError:
        fah_entry.delete(0, END)
        fah_entry.insert(0, "Error")
        celsius_entry.delete(0, END)
        celsius_entry.insert(0, "Error")

def btn(winmain, kelvin_entry, celsius_entry, fah_entry):
    btn01 = Button(winmain, font = ('Times New Roman', 20), text = 'Cal', fg = 'purple',
                   command = lambda:cal(kelvin_entry, celsius_entry, fah_entry))
    btn01.place(x = 200, y = 250)
    btn02 = Button(winmain, font = ('Times New Roman', 20), text = 'DELETE', fg = 'purple',
                   command = lambda:clr( kelvin_entry, celsius_entry, fah_entry))
    btn02.place(x = 300, y = 250)
    

def main():
    winmain = Tk()
    winmain.title('Temperature')
    winmain.geometry('500x500')
    lbl(winmain)
    kelvin_entry = k(winmain)
    celsius_entry = txtbox(winmain)
    fah_entry = txtbox02(winmain)
    
    btn(winmain, kelvin_entry, celsius_entry, fah_entry)
    

    winmain.mainloop()

main()
