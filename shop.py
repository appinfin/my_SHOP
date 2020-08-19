from tkinter import *

def select_fruits(e):
    """Ф-ция выбора фрукта в зависимости от нажатой кнопки"""
    fruit = e.widget.winfo_name()
    print('this str:', fruit)
    select_fruits = {'!button': 'яблок',
                     '!button2': 'апельсинов',
                     '!button3': 'груш'
                     }
    select_price_fruits = {'!button': 70,
                           '!button2': 160,
                           '!button3': 100
                           }
    choice_fruit = select_fruits[fruit]
    price_fruit = select_price_fruits[fruit]
    toplevel_set_weight(price_fruit, choice_fruit)
    
def toplevel_set_weight(price_fruit, choice_fruit):
    """Окно ввода кол-ва фруктов"""
    top_win = Toplevel(root)
    top_win.title("my SHOP")
    w = top_win.winfo_screenwidth()  # ширина экрана
    h = top_win.winfo_screenheight()  # высота экрана
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 210  # смещение от середины
    h = h - 100
    top_win.geometry(f'420x200+{w}+{h}')
    top_win.resizable(False, False)
    top_win.grab_set()
    top_win.focus_set()
    #IMG
    img_top_win = PhotoImage(file = "seller.png")
    #WIDGETS
    label_img_seller = Label(top_win, image = img_top_win)\
                       .grid(row = 0, column = 0, padx = 10, pady = 10)
                       
    label_top_win = LabelFrame(top_win, text = 'Сколько, Вам, взвесить?', font = 'Arial 12 bold')
    label_top_win.grid(row = 0, column = 1)
    # ввод кол-ва фруктов
    ent = Entry(label_top_win, width = 6)
    ent.grid(row = 0, column = 0, padx = 10)
    ent.insert = (0, "2")
    
    label_weight = Label(label_top_win, text = 'КГ', font = 'Arial 12 bold').grid(row = 0, column = 1)
    
    but_ok = Button(label_top_win, text = 'Оплатить',\
                    command = lambda: result(price_fruit, ent.get(), choice_fruit, top_win))
    
    but_ok.grid(row = 0, column = 2, padx = 10, ipadx = 40)
    
    mainloop()

def result(price_fruit, ent_get, choice_fruit, top_win):
    """Ф-ция расчёта суммы"""
    if float(ent_get) <= 100.0: #не более 100 кг.
        top_win.destroy()
        round_weigth = round(float(ent_get),3)
        total = price_fruit * round_weigth
        label_basket['text'] = f'В корзине {round_weigth} кг {choice_fruit}\nна сумму {total} руб.'
    else:
        top_win.destroy()
        total = price_fruit * 100
        label_basket['text'] = f'В корзине 100 кг {choice_fruit}\nна сумму {total} руб.'    

root = Tk()
root.title("my SHOP")
w = root.winfo_screenwidth()  # ширина экрана
h = root.winfo_screenheight()  # высота экрана
w = w // 2  # середина экрана
h = h // 2
w = w - 210  # смещение от середины
h = h - 100
root.geometry(f'420x200+{w}+{h}')
##root.geometry(f'420x200+400+20')
root.resizable(False, False)
#IMG
img = PhotoImage(file = "1.png")
img_2 = PhotoImage(file = "2.png")
img_3 = PhotoImage(file = "3.png")
#LABELs images
label = Label(image = img, width = 140).grid(row = 1, column = 0)
label_2 = Label(image = img_2, width = 140).grid(row = 1, column = 1)
label_3 = Label(image = img_3, width = 140).grid(row = 1, column = 2)
#LABEL apples
top_label = Label(text = 'Яблоки (Apples)\nЦена: 70 руб/кг.',\
                  font = 'Arial 10').grid(row = 0, column = 0, pady = 10)
#LABEL oranges
top_label_2 = Label(text = 'Апельсины (Oranges)\nЦена: 160 руб\кг.',\
                    font = 'Arial 10').grid(row = 0, column = 1)
#LABEL pears
top_label_3 = Label(text = 'Груши (Pears)\nЦена: 100 руб\кг.',\
                    font = 'Arial 10').grid(row = 0, column = 2)
#LABEL basket
label_basket = Label(text = 'В корзине 0 кг фруктов\nна сумму 0 руб.',\
                     font = 'Arial 12 bold', justify = LEFT)
label_basket.grid(row = 3, column = 0, columnspan = 3, sticky = 'w', ipadx = 10, ipady = 10)
##BUTTON 1
btn = Button(root, text = 'Купить')
btn.bind('<Button-1>', select_fruits)
btn.bind('<Return>', select_fruits)
btn.grid(row = 2, column = 0)
##BUTTON 2
btn_2 = Button(root, text = 'Купить')
btn_2.bind('<Button-1>', select_fruits)
btn_2.bind('<Return>', select_fruits)
btn_2.grid(row = 2, column = 1)
##BUTTON 3
btn_3 = Button(root, text = 'Купить')
btn_3.bind('<Button-1>', select_fruits)
btn_3.bind('<Return>', select_fruits)
btn_3.grid(row = 2, column = 2)

root.mainloop()
