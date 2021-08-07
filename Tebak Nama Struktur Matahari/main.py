import turtle
import pandas

screen = turtle.Screen()
screen.title("Tebak Bagian/Struktur Matahari")
image = 'matahari.gif'
screen.addshape(image)
turtle.shape(image)

tertebak = []
data = pandas.read_csv('struktur.csv')
struktur = data.struktur.to_list()

while len(tertebak) < 8:
    jawaban = screen.textinput(title=f"{len(tertebak)}/8 Ditebak",
                               prompt="Ketik Nama Struktur Mataharinya!").title()

    if jawaban in struktur:
        tertebak.append(jawaban)
        teks = turtle.Turtle()
        teks.hideturtle()
        teks.penup()
        struktur_data = data[data.struktur == jawaban]
        teks.goto(int(struktur_data.x), int(struktur_data.y))
        teks.write(jawaban)

    if jawaban == "Keluar":
        missing_answer = []
        for i in struktur:
            if i not in tertebak:
                missing_answer.append(i)
        new_data = pandas.DataFrame(missing_answer).to_csv('StrukturMatahari.csv')
        break