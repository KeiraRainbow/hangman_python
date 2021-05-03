# используется шрифт Segoe Print, потому что он похож на рукописный
# все зеленое, потому что это мой любимый цвет
# я попыталась сделать все читабельным, но с текстом на кнопках все сложно
from tkinter import *
import random

root = Tk()
root.title("Виселица")
canvas = Canvas(root, width=600, height=475)
canvas.pack()


# фон в игре
def bg_game():
    y = 0
    while y < 475:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 33, fill="green", outline="dark green")
            x = x + 33
        y = y + 33


# фон при старте
def bg_start():
    y = 0
    while y < 475:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 33, fill="green", outline="dark green")
            x = x + 33
        y = y + 33


def gallow():
    canvas.create_line(10, 10, 10, 350, width=4)
    canvas.create_line(10, 10, 210, 10, width=4)
    canvas.create_line(10, 80, 60, 10, width=4)
    canvas.create_line(140, 80, 140, 10, width=4)
    canvas.create_line(10, 280, 60, 350, width=4)
    canvas.create_line(5, 350, 65, 350, width=4)


bg_start()
faq = '''Поиграем в виселицу!'''
canvas.create_text(310, 285, text=faq, fill="white", font=("Segoe Print", "20"))
# слова
words = ["автобаза", "аэродром", "академик", "ботаника", "ватружка", "вечность", "гардероб",
         "диктатор", "единорог", "единство", "живопись", "загрузка", "инцидент", "контраст", "кристалл",
         "латиница", "молодежь", "мансарда", "носитель", "обезьяна", "пристань", "редкость", "разговор",
         "сожитель", "торговля", "уважение", "фокусник", "хрусталь", "хитрость", "цыпленок", "часовщик",
         "шлагбаум", "щупальца", "эрудиция", "экономия", "юмореска", "языковед"]


# основная функция
def arr():
    bg_game()
    gallow()
    word = random.choice(words)
    el = word[1:-1]
    list = []
    for i in el:
        list.append(i)
    a0 = canvas.create_text(282, 40, text=word[0], fill="white", font=("Segoe Print", "14"))
    a1 = canvas.create_text(315, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a2 = canvas.create_text(347, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a3 = canvas.create_text(380, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a4 = canvas.create_text(412, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a5 = canvas.create_text(444, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a6 = canvas.create_text(477, 40, text="_", fill="white", font=("Segoe Print", "14"))
    a7 = canvas.create_text(510, 40, text=word[-1], fill="white", font=("Segoe Print", "14"))
    list1 = [1, 2, 3, 4, 5, 6]
    alphabet = "абвгдезжийклмнопрстуфхцчшщъыьэюя"
    error = []
    win = []

    # подсветка букв на клавиатуре, координаты отгаданных букв и выигрыш
    def a(v):
        ind_alph = alphabet.index(v)
        key = alphabet[ind_alph]

        if v in list:
            ind = list.index(v)
            b2 = list1[ind]
            list[ind] = '1'

            def kord():
                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1

            x1, y1 = kord()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=el[ind], fill="white", font=("Segoe Print", "14"))
            b[key]["bg"] = "cyan"
            if not v in list:
                b[key]["state"] = "disabled"
            if v in list:
                win.append(v)
                ind2 = list.index(v)
                b2 = list1[ind2]
                x1, y1 = kord()
                canvas.create_text(x1, y1, text=el[ind2], fill="white", font=("Segoe Print", "14"))
            if len(win) == 6:
                canvas.create_text(135, 175, text="Победа!", fill="white", font=("Segoe Print", "20"))
                for i in alphabet:
                    b[i]["state"] = "disabled"
        else:
            error.append(v)
            b[key]["bg"] = "red"
            b[key]["state"] = "disabled"

            if len(error) == 1:
                head()
            elif len(error) == 2:
                body()
            elif len(error) == 3:
                left_hand()
            elif len(error) == 4:
                right_hand()
            elif len(error) == 5:
                left_leg()
            elif len(error) == 6:
                right_leg()
                end()
            root.update()

    b = {}

    # генерация кнопок
    def gen(u, x, y):
        b[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        b[u].place(x=str(x), y=str(y))

    x = 265
    y = 110
    for i in alphabet[0:8]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 137
    for i in alphabet[8:16]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 164
    for i in alphabet[16:24]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 191
    for i in alphabet[24:32]:
        gen(i, x, y)
        x = x + 33

    # человечек
    def head():
        canvas.create_oval(110, 70, 170, 120, width=4, fill="white")
        root.update()

    def body():
        canvas.create_line(140, 120, 140, 205, width=4)
        root.update()

    def left_hand():
        canvas.create_line(140, 120, 85, 180, width=4)
        root.update()

    def right_hand():
        canvas.create_line(140, 120, 185, 180, width=4)
        root.update()

    def left_leg():
        canvas.create_line(140, 205, 85, 310, width=4)
        root.update()

    def right_leg():
        canvas.create_line(140, 205, 185, 310, width=4)
        root.update()

    # конец игры при проигрыше
    def end():
        canvas.create_text(135, 175, text="Неудача!", fill="white", font=("Segoe Print", "20"))
        for i in alphabet:
            b[i]["state"] = "disabled"


# запуск игры и обновление слова
b1 = Button(root, text="Давай..", width=10, height=1, command=lambda: arr())
b1.place(x=270, y=310)
b1["bg"] = "dark green"

root.mainloop()
