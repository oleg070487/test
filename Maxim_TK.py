import Maxim
import tkinter as tk
from tkinter import messagebox
from string import digits


def generated():
    values = [value.get() for value in lst_obj_Entry]
    from_temp_and_to_temp, number_of_numbers_generated, number_of_subranges, number_of_repeat_program = values
    from_temp = None
    to_temp = None

    check_lst = digits + ' ' + '-'
    flag = True
    if ' ' in from_temp_and_to_temp[1:-1] and all(i in check_lst for i in from_temp_and_to_temp):
        from_temp, to_temp = from_temp_and_to_temp.strip().split()
    else:
        messagebox.showinfo('Внимание', 'Нужно вводить два целых числа через пробел в первой строке!')
        flag = False
    trend_type = select_trend()

    lst_of_all_lst_generated = []
    if flag:
        try:
            for x in range(int(number_of_repeat_program)):
                lst_temp = Maxim.main(int(from_temp), int(to_temp), int(number_of_numbers_generated), trend_type,
                                      int(number_of_subranges))
                lst_of_all_lst_generated.append(lst_temp)
                flag = True
        except ValueError:
            messagebox.showerror('Ошибка', 'Вы ввели не верные данные!')
            flag = False

    result_of_zip = list(zip(*lst_of_all_lst_generated))

    if flag:
        try:
            with open('random.xls', 'w') as file:
                file.write("Случайные вещественные числа в заданном диапазоне:" + '\n\n')
                for tp in result_of_zip:
                    for el in tp:
                        el_str = str(el).replace('.', ',') + '\t'
                        file.write(f'{el_str}')
                    file.write('\n')
            messagebox.showinfo('Поздравляю', 'Данные успешно записаны!')
        except PermissionError:
            messagebox.showerror('Ошибка', 'Данные не были записаны, вы не закрыли файл!')


def clear():
    [value.delete(0, tk.END) for value in lst_obj_Entry]
    trend_var.set('no')


def select_trend():
    trend = trend_var.get()
    return trend


win = tk.Tk()
# photo = tk.PhotoImage(file='Cannabis.png')
# win.iconphoto(False, photo)
win.config(bg='#b9cef0')
win.title('Random temperature')
win.geometry('1000x500+700+200')
win.resizable(False, False)
win.minsize(1000, 500)
# win.maxsize()

lst_text_labels = ('Введите диапазон температур, два числа через пробел от меньшего к большому ',
                   'Введите требуемое количество сгенерированных чисел ',
                   'Введите число для регулирования качества тренда '
                   'в зависимости \nот количества  всех сгенерируемых чисел и '
                   'другой необходимости например число - 4 ',
                   'Введите количество датчиков',
                   'Выберите тренд:')

"""Создание меток"""
for label in lst_text_labels:
    tk.Label(win, text=label, bg='#b9cef0', font=('Arial', 13), padx=20, pady=10, justify=tk.LEFT).grid(sticky='w')

"""Создание окон ввода"""
lst_obj_Entry = []
for i in range(4):
    entry = tk.Entry(win, font=('Arial', 13))
    entry.grid(row=i, column=1)
    lst_obj_Entry.append(entry)

trend_var = tk.StringVar()
trend_var.set('no')

trend_no = tk.Radiobutton(win, bg='#b9cef0', font=('Arial', 13), padx=20, pady=5, text='Без тренда',
                          variable=trend_var, value='no', command=select_trend)
trend_no.grid(sticky='w')
trend_up = tk.Radiobutton(win, bg='#b9cef0', font=('Arial', 13), padx=20, pady=5, text='На повышение',
                          variable=trend_var, value='+', command=select_trend)
trend_up.grid(sticky='w')
trend_down = tk.Radiobutton(win, bg='#b9cef0', font=('Arial', 13), padx=20, pady=5, text='На понижение',
                            variable=trend_var, value='-', command=select_trend)
trend_down.grid(sticky='w')

"""Создание кнопок"""
btn_generated = tk.Button(win, text='Сгенерировать', activebackground='#8f8c83',
                          command=generated, padx=10, pady=10, font=('Arial', 13))
btn_generated.grid(row=8, column=0)
btn_clear = tk.Button(win, text='Сбросить', activebackground='#8f8c83',
                      command=clear, padx=10, pady=10, font=('Arial', 13))
btn_clear.grid(row=8, column=1)

win.mainloop()
