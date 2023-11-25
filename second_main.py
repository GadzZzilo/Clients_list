import datetime
import sys

from PySide6 import QtSql, QtWidgets
from PySide6.QtCore import Qt, QModelIndex, QTimer, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor, QPainter, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QStyledItemDelegate, QComboBox, QStyleOptionViewItem, \
    QItemDelegate, QLineEdit
from ui_main import Ui_MainWindow

import sqlite3


class ComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, choices, parent=None):
        super().__init__()
        self.choices = choices

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(self.choices)
        return editor

    def setEditorData(self, editor, index):
        value = str(index.model().data(index, Qt.EditRole))
        editor.setCurrentText(value)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), Qt.EditRole)

    #################################################################
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index: QModelIndex):
        if index.column() == 1 and index.data() == "Выполнено":
            painter.save()

            # Устанавливаем цвет фона ячейки
            painter.fillRect(option.rect, QColor(0, 200, 0, 200))

            # Отображаем текст ячейки
            option.palette.setColor(QPalette.Text, Qt.white)
            # self.drawDisplay(painter, option, option.rect, index.data())

            painter.restore()
        elif index.column() == 1 and index.data() == "Исполняется":
            painter.save()

            # Устанавливаем цвет фона ячейки
            painter.fillRect(option.rect, QColor(200, 200, 0, 200))

            # Отображаем текст ячейки
            option.palette.setColor(QPalette.Text, Qt.white)
            # self.drawDisplay(painter, option, option.rect, index.data())

            painter.restore()
        else:
            # Если условие не выполняется, отображаем ячейку по умолчанию
            super().paint(painter, option, index)


class ColorDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setStyleSheet('color: white;')
        return editor


class ClientsList(QMainWindow):
    def __init__(self):
        super(ClientsList, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ######################
        self.create_connection()
        ###################

        self.connection = sqlite3.connect('clients_db.db')
        self.cursor = self.connection.cursor()

        # self.cursor.execute('SELECT * FROM clients ORDER BY Готовность, id')
        # self.data = self.cursor.fetchall()

        ################
        self.model = QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        #####################
        self.view_data()

        self.ui.pushButton.clicked.connect(self.add_new_client)
        self.ui.pushButton_2.clicked.connect(self.delete_client)

        self.ui.tableView.hideColumn(0)
        self.ui.tableView.hideColumn(5)
        # self.model.dataChanged.connect(self.update_database)
        self.model.dataChanged.connect(self.update_table_and_database)
        self.model.rowsInserted.connect(self.add_new_client_db)

        delegate_combobox = ComboBoxDelegate(["Нет лр", "Исполняется", "Выполнено"], self.ui.tableView)
        delegate_lineedit = ColorDelegate(self.ui.tableView)
        self.ui.tableView.setItemDelegateForColumn(1, delegate_combobox)
        self.ui.tableView.setItemDelegate(delegate_lineedit)

    #############3
        
    ##########33##

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('clients_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получилось открыть базу данных:(",
                                           "Нажмите, чтобы закрыть", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS clients (id integer primary key AUTOINCREMENT, Готовность VARCHAR(40), "
                   "Имя VARCHAR(60), Приведенные VARCHAR(100), Комментарий VARCHAR(160), Время_начала DATETIME)")
        return True
    def view_data(self):
        # self.model.clear()
        self.model.setHorizontalHeaderLabels(["id", "Готовность", "Имя", "Приведенные", "Комментарий", "Время_начала"])
        self.cursor.execute('SELECT * FROM clients ORDER BY Готовность, Время_начала')
        self.data = self.cursor.fetchall()

        for i_row, row_item in enumerate(self.data):
            for i_col, col_item in enumerate(row_item):
                if i_col == 0:
                    cell = QStandardItem()
                    cell.setData(col_item, Qt.DisplayRole)
                    self.model.setItem(i_row, i_col, cell)
                else:
                    cell = QStandardItem(str(col_item))
                    self.model.setItem(i_row, i_col, cell)
        #######################3

        ##########################

        print("view_data")

    def update_table_and_database(self, top_left_index, bottom_right_index):
        self.update_database(bottom_right_index)  # Обновление базы данных
        self.sort_table()

    def sort_table(self):
        self.model.sort(5, Qt.AscendingOrder)  # Сортировка по столбцу "Время_начала"
        print("sort1")
        self.model.sort(1, Qt.AscendingOrder)  # Сортировка по столбцу "Готовность"
        print("sort2")

    def add_new_client(self):
        rowPosition = self.model.rowCount()
        self.model.insertRow(rowPosition)

    def update_database(self, index):
        row = index.row()
        col = index.column()
        new_value = index.data()
        id_index = self.model.index(row, 0)
        id_value = self.model.data(id_index)
        column_name = self.model.horizontalHeaderItem(col).text()

        if col == 1 and new_value == "Исполняется":
            date = datetime.datetime.now()
            print(date)
            self.cursor.execute(
                f'UPDATE clients SET {column_name} = ?, Время_начала = ? WHERE id = ?',
                (new_value, date, id_value)
            )
        else:
            self.cursor.execute(f'UPDATE clients SET {column_name} = ? WHERE id = ?', (new_value, id_value))

        self.connection.commit()

    def add_new_client_db(self):
        self.cursor.execute("INSERT INTO clients (Готовность, Имя, Приведенные, Комментарий) VALUES ('', '', '', '')")
        self.connection.commit()

        self.cursor.execute('SELECT COUNT(*) FROM clients')
        row_count = self.cursor.fetchone()[0]
        row_index = row_count - 1

        self.cursor.execute('SELECT * FROM clients ORDER BY Готовность')
        self.data = self.cursor.fetchall()
        item = max([self.data[i][0] for i in range(len(self.data))]) if len(self.data) != 1 else 1
        cell = QStandardItem(str(item))
        self.model.setItem(row_index, 0, cell)
        # self.view_data()
        print("add")

    def delete_client(self):
        selected_index = self.ui.tableView.currentIndex()
        if not selected_index.isValid():
            return None

        row = selected_index.row()
        id_value = self.data[row][0]
        self.model.removeRow(row)

        self.cursor.execute("DELETE FROM clients WHERE ID=?", (id_value,))
        self.connection.commit()
        self.cursor.execute('SELECT * FROM clients ORDER BY Готовность')
        self.data = self.cursor.fetchall()
        print("del")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientsList()
    window.show()
    sys.exit(app.exec())
