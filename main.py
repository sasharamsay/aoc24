from tkinter import *
from day1 import *

window = Tk()
window.geometry('230x185')
window.title('Advent of Code 2024')
day_var = StringVar(window)
part_var = StringVar(window)
answer_var = StringVar(window)
test_var = IntVar(window)


def configure(win):
    day_label = Label(win, text='Day:', padx=10, pady=10)
    day_input = Entry(win, textvariable=day_var, width=10)
    part_label = Label(win, text='Part:', padx=10, pady=10)
    part_input = Entry(win, textvariable=part_var, width=10)
    test = Checkbutton(win, text='Use test input', variable=test_var, pady=10)
    button = Button(win, text='Submit', command=submit)
    answer = Label(win, textvariable=answer_var, pady=10)

    day_label.grid(row=0, column=0)
    day_input.grid(row=0, column=1)
    part_label.grid(row=1, column=0)
    part_input.grid(row=1, column=1)
    test.grid(row=2, column=1)
    button.grid(row=3, column=1)
    answer.grid(row=4, column=1)

    win.focus_force()
    day_input.focus()
    win.mainloop()


def submit():
    answer_var.set('Thinking...')
    run(int(day_var.get()), int(part_var.get()), test_var.get())


def run(day, part, test):
    file_type = 'test' if test == 1 else 'in'
    filename = 'input/' + file_type + str(day) + '.txt'

    day_map = {
        1: (day_1, day_1_part_2)
    }

    answer_var.set(str(day_map[day][part-1](filename)))


if __name__ == '__main__':
    configure(window)
