import tkinter as TreeApp
import pyautogui

root= TreeApp.Tk()

canvas1 = TreeApp.Canvas(root, width = 1080, height = 720)
canvas1.pack()

def tree():  
    label1 = TreeApp.Label(root, text= 'Tree command is executed! \n Please close this application.\n THANK YOU!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    pyautogui.hotkey('win','r')
    pyautogui.write('tree')
    pyautogui.press('enter')
    
button1 = TreeApp.Button(text='Execute Tree',command=tree, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
