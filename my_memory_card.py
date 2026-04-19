#Общее для всех
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint

class question():
  def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    self.question =  question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3

question_list = []
question_list.append(question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
question_list.append(question('Какого цвета нет на флаге России?', 'Зелёного', 'Красный', 'Белый', 'Синий'))
question_list.append(question('Национальная хижина якут', 'Ураса', 'Иглу', 'Хата', 'Дом'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')

btn_ok = QPushButton('Ответить')
ql_question = QLabel('В каком году была основана Москва?')

# Первая часть
RadioGroupBox = QGroupBox('Варианты ответа')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

# Вторую часть
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('прав ты или нет?')
correct = QLabel('ответ будет тут') 
layout_res = QVBoxLayout()
layout_res.addWidget(result)
layout_res.addWidget(correct)

AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(ql_question)
layout_line2.addWidget(AnsGroupBox)
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(btn_ok)
AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1)
layout_card.addLayout(layout_line2)
layout_card.addLayout(layout_line3)
#Общее для всех
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
  RadioGroupBox.show()
  AnsGroupBox.hide()
  RadioGroup.setExclusive(False)
  btn_ok.setText('Ответить')
  rbtn_1.setChecked(False)
  rbtn_2.setChecked(False)
  rbtn_3.setChecked(False)
  rbtn_4.setChecked(False)
  RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: question):
  shuffle(answer)
  answer[0].setText(q.right_answer)
  answer[1].setText(q.wrong1)
  answer[2].setText(q.wrong2)
  answer[3].setText(q.wrong3)
  ql_question.setText(q.question)
  correct.setText(q.right_answer)
  show_question()

def show_correct(res):
  result.setText(res)
  show_result()

def check_answer():
  if answer[0].isChecked():
    show_correct('Правильно')
    window.score += 1
    print(f'Статистика"\n- Всего вопросов: {window.total}\n- Всего правильных ответов: {window.score}\n Рейтинг: {window.score/window.total*100}%')
  else:
    if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неверно')
        print(f'Статистика"\n- Всего вопросов: {window.total}\n- Всего правильных ответов: {window.score}\n Рейтинг: {window.score/window.total*100}%')

def next_question():
    window.total += 1

    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
  if btn_ok.text() == 'Ответить':
    check_answer()
  else:
    next_question()

window = QWidget()
window.setLayout(layout_card)
window.show()
window.total = 0
window.score = 0

btn_ok.clicked.connect(click_ok)

next_question()
window.resize(400, 300)
window.show
app.exec()
