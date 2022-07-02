from sympy import symbols, Eq, solve, sympify
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk


def EulerMethod():
    x,y = symbols('x y')
    #Getting information from text boxes in the GUI
    slope = sympify(slope_input.get())
    x0 = float(x_input.get())
    y0 = float(y_input.get())
    xf= float(xf_input.get())
    number_of_steps = int(n_input.get())

    length_of_partitions = ((xf - x0)/(number_of_steps))
    x_values = [x0]
    y_values = [y0]
    n = 0
    y_approx = y0
    while n != number_of_steps:
        #Incrementing y by the slope at (x,y) * the length of each partition
        y_approx += length_of_partitions * (slope.evalf(subs = {x:(x0 + (n)*length_of_partitions),y:y_approx}))
        x_values.append(x0 + (n+1)*length_of_partitions)
        y_values.append(y_approx)
        n+= 1

    #Updating UI display the results
    tk.Label(root,
    text='Final Approximation : y({}) = {}'.format(xf,y_values[-1]),
    bg='#F0F8FF',
    font=('arial', 12, 'normal'),
    ).place(x=16, y=166)

    #Creating the graph with the data points from euler's method
    plt.plot(x_values,y_values)
    plt.title('Approximate Solution to  dy/dx = {}'.format(slope_input.get()))
    plt.show()


#----------------[ USER INTERFACE STUFF ]--------------------------#
root = tk.Tk()
# --Main window--
root.geometry('383x200')
root.configure(background='#F0F8FF')
root.title('Euler\'s Method Calculator')

#--GUI labels--
load = Image.open('PennStat.png')
render = ImageTk.PhotoImage(load)
logo = tk.Label(image=render)
logo.image = render
logo.place(x=305,y = 17)



tk.Label(root, text='dy/dx = ', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=7)

tk.Label(root, text='Initial x value:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=27)

tk.Label(root, text='Initial y value:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=47)

tk.Label(root, text='Approximate to x =', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=67)

tk.Label(root, text='Number of steps:', bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=20, y=87)

# the text boxes--
slope_input=tk.Entry(root)
slope_input.place(x=80, y=7, width = 210)


x_input=tk.Entry(root)
x_input.place(x=120, y=27)

y_input=tk.Entry(root)
y_input.place(x=120, y=47)

xf_input=tk.Entry(root)
xf_input.place(x=160, y=67)

n_input=tk.Entry(root)
n_input.place(x=160, y=87)

# Creates button which when pressed, calls EulersMethod()
#  (with strings in text entries in the window as the parameters )
tk.Button(root,
    text='Graph Approximate Solution', 
    bg='#C1CDCD',
    font=('arial', 15, 'bold'),
    command = EulerMethod,
).place(x=10, y=117)

root.mainloop()
