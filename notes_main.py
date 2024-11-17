#начни тут создавать приложение с умными заметками
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QHBoxLayout, QVBoxLayout, QGroupBox, QLineEdit, QListWidget, QTextEdit, QInputDialog
import json


""""notes = {"Добро пожаловать":{ 
    "текст":"В этом приложении можно создавать заметки с тегами...",
    "теги": ["Умные заметки", "инструкция"]
    }
}

with open("notes_data.json", "w") as file:
    json.dump(notes, file)"""




app = QApplication([])
notes_win = QWidget()
notes_win.setWindowTitle('Умные Заметки')
notes_win.resize(480,270)
zametka_add = QPushButton("Создать заметку")
zametka_del = QPushButton("Удалить заметку")
zametka_save = QPushButton("Сохранить заметку")
dobavit_for_zametka = QPushButton("Добавить к заметке")
otcrepit_from_zametka = QPushButton("Открепить от заметки")
zametka_in_tegs = QPushButton("Искать заметки по тегу")
zamitki_Spisok = QLabel("Список заметок")
tegs_spisok = QLabel("Список тегов")
tegs_line = QLineEdit()
pole2 = QListWidget()#виджет для хранения имен заметок
pole3 = QListWidget()#поле для тегов
Glav_zametka = QTextEdit()#Виджет для текста заметки


V_main = QVBoxLayout()
V_main1 = QVBoxLayout()
H_main_main = QHBoxLayout()
H_main2 = QHBoxLayout() 
H_main3 = QHBoxLayout()
H_main4 = QHBoxLayout() 
H_main5 = QHBoxLayout()
H_main6 = QHBoxLayout() 
H_main7 = QHBoxLayout()
H_main8 = QHBoxLayout() 
H_main9 = QHBoxLayout()
H_main10 = QHBoxLayout()

#размешение на красных горизанталях
H_main2.addWidget(zamitki_Spisok)
H_main3.addWidget(pole2)
H_main4.addWidget(zametka_add)
H_main4.addWidget(zametka_del)
H_main5.addWidget(zametka_save)
H_main6.addWidget(tegs_spisok)
H_main7.addWidget(pole3)
H_main8.addWidget(tegs_line)
H_main9.addWidget(dobavit_for_zametka)
H_main9.addWidget(otcrepit_from_zametka)
H_main10.addWidget(zametka_in_tegs)

#размешение горизонтальных на вертикальной линии
V_main1.addLayout(H_main2)
V_main1.addLayout(H_main3)
V_main1.addLayout(H_main4)
V_main1.addLayout(H_main5)
V_main1.addLayout(H_main6)
V_main1.addLayout(H_main7)
V_main1.addLayout(H_main8)
V_main1.addLayout(H_main9)
V_main1.addLayout(H_main10)

#насаживание шлавного поля на первую вертикальную
V_main.addWidget(Glav_zametka)


#две вертикальные оси ставим на главную горизонтальную
H_main_main.addLayout(V_main)
H_main_main.addLayout(V_main1)


notes_win.setLayout(H_main_main)

def show_note():#обработчик клика по имени заметки
    name = pole2.selectedItems()[0].text()
    Glav_zametka.setText(notes[name]["текст"])
    pole3.clear()
    pole3.addItems(notes[name]["теги"])

def add_note():
    note_name, result = QInputDialog.getText(
        notes_win, 'Добавить заметку', 'Название заметки'
    )
    if note_name != '' and result:
        notes[note_name] = { "текст":"","теги": []}
        pole2.addItem(note_name)
        pole3.addItems(notes[note_name]["теги"])
        print(notes)

def del_note():
    if pole2.selectedItems():
        name = pole2.selectedItems()[0].text()
        del notes[name]
        print(notes)
        with open("notes_data.json", 'w') as file:
            json.dump(notes, file)
        pole2.clear()
        pole3.clear()
        Glav_zametka.clear()
        pole2.addItems(notes)    

def save_note():
    if pole2.selectedItems():
        name = pole2.selectedItems()[0].text()
        notes[name]['текст'] = Glav_zametka.toPlainText()
        with open("notes_data.json", 'w') as file:
            json.dump(notes, file)
        print(notes)


def add_tag():
    if pole2.selectedItems():
        name = pole2.selectedItems()[0].text()
        teGGs = tegs_line.text()
        if not teGGs in notes[name]['теги']:
            notes[name]['теги'].append(teGGs)
            pole3.addItem(teGGs)
            tegs_line.clear()
            with open("notes_data.json", 'w') as file:
                json.dump(notes, file)
            print(notes)


def del_tag():
    if pole2.selectedItems():
        name = pole2.selectedItems()[0].text()
        teg_name = pole3.selectedItems()[0].text()
        notes[name]['теги'].remove(teg_name)
        pole3.clear()
        pole3.addItems(notes[name]['теги'])
        with open("notes_data.json", 'w') as file:
            json.dump(notes, file)
        print(notes)       

def search_tag():
    if zametka_in_tegs.text() == 'Искать заметки по тегу':
        tag = tegs_line.text()
        notes_filtered = dict()
        for note in notes:
            if tag in notes[note]['теги']:
                notes_filtered[note] = notes[note]
        zametka_in_tegs.setText('Сбросить поиск')
        pole2.clear()
        pole3.clear()
        pole2.addItems(notes_filtered) 
    elif zametka_in_tegs.text() == 'Сбросить поиск':
        zametka_in_tegs.setText('Искать заметки по тегу')
        pole2.clear()
        pole3.clear()
        tegs_line.clear()
        pole2.addItems(notes)        


with open("notes_data.json", "r") as file:
    notes = json.load(file)

pole2.addItems(notes)
zametka_add.clicked.connect(add_note)
pole2.itemClicked.connect(show_note)
zametka_del.clicked.connect(del_note)
zametka_save.clicked.connect(save_note)
dobavit_for_zametka.clicked.connect(add_tag)
otcrepit_from_zametka.clicked.connect(del_tag)
zametka_in_tegs.clicked.connect(search_tag)





notes_win.show()
app.exec_()