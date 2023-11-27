from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTableView, QHeaderView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск в таблице")
        self.setGeometry(100, 100, 800, 400)

        # Создание виджета и вертикального компоновщика
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        # Создание поля ввода для поиска
        self.search_input = QLineEdit()
        self.search_input.textChanged.connect(self.highlight_rows)
        layout.addWidget(self.search_input)

        # Создание таблицы и модели данных
        self.table = QTableView()
        self.model = QStandardItemModel(self)

        # Установка модели данных для таблицы
        self.table.setModel(self.model)

        # Установка заголовков столбцов
        self.model.setHorizontalHeaderLabels(["Столбец 1", "Столбец 2", "Столбец 3"])

        # Вставка данных в модель
        self.insert_data()

        # Настройка параметров таблицы
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Добавление таблицы в компоновщик
        layout.addWidget(self.table)

        # Установка компоновщика для основного окна
        self.setCentralWidget(widget)

    def insert_data(self):
        # Вставка данных в модель
        for i in range(10):  # Пример для 10 строк
            row = []
            for j in range(3):  # Пример для 3 столбцов
                item = QStandardItem(f"Значение {i}-{j}")
                row.append(item)
            self.model.appendRow(row)

    def highlight_rows(self):
        search_text = self.search_input.text()

        # Очищение выделения всех строк
        for row in range(self.model.rowCount()):
            self.table.setRowHidden(row, False)

        # Поиск и подсветка строк, удовлетворяющих критерию поиска
        if search_text:
            for row in range(self.model.rowCount()):
                for column in range(self.model.columnCount()):
                    item = self.model.item(row, column)
                    if search_text.lower() in item.text().lower():
                        self.table.setRowHidden(row, False)
                        break
                    else:
                        self.table.setRowHidden(row, True)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()