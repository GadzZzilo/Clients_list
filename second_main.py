import datetime
import sys

from PySide6 import QtSql, QtWidgets
from PySide6.QtCore import Qt, QStringListModel, QSortFilterProxyModel
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QListView

from delegats import ComboBoxDelegate, ColorDelegate
from ui_add_client_window import Ui_Dialog
from ui_main import Ui_MainWindow

import sqlite3


class NameFilterModel(QSortFilterProxyModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.filter_string = ""

    def setFilterString(self, text):
        self.filter_string = text
        self.invalidateFilter()

    def filterAcceptsRow(self, source_row, source_parent):
        if not self.filter_string:
            return True
        name = self.sourceModel().data(self.sourceModel().index(source_row), Qt.DisplayRole)
        return name.startswith(self.filter_string)


class ClientsList(QMainWindow):
    def __init__(self):
        super(ClientsList, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.create_connection()

        self.connection = sqlite3.connect('clients_db.db')
        self.cursor = self.connection.cursor()

        self.model = QStandardItemModel()
        self.ui.tableView.setModel(self.model)
        self.view_data()

        self.ui.pushButton.clicked.connect(self.open_new_window)
        self.ui.pushButton_2.clicked.connect(self.delete_client)

        # self.ui.tableView.hideColumn(0)
        # self.ui.tableView.hideColumn(5)

        self.model.dataChanged.connect(self.update_table_and_database)
        self.model.rowsInserted.connect(self.add_new_client_db)

        delegate_combobox = ComboBoxDelegate(["Нет лр", "Исполняется", "Выполнено"], self.ui.tableView)
        delegate_lineedit = ColorDelegate(self.ui.tableView)
        self.ui.tableView.setItemDelegateForColumn(1, delegate_combobox)
        self.ui.tableView.setItemDelegate(delegate_lineedit)

    def open_new_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)

        self.cursor.execute('SELECT Имя FROM clients ORDER BY Имя')
        names = [name[0] for name in self.cursor.fetchall()]

        filter_model = NameFilterModel()
        filter_model.setSourceModel(QStringListModel(names))

        search_line = self.ui_window.search_line
        search_line.textChanged.connect(filter_model.setFilterString)

        list_view = self.ui_window.listView
        list_view.setModel(filter_model)
        list_view.setEditTriggers(QListView.NoEditTriggers)
        list_view.clicked.connect(lambda index: search_line.setText(index.data()))

        self.new_window.show()

        self.ui_window.pushButton.clicked.connect(self.add_new_client)

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('clients_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Не получилось открыть базу данных:(",
                                           "Нажмите, чтобы закрыть", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS clients (id integer primary key AUTOINCREMENT, Готовность VARCHAR(40), "
                   "Имя VARCHAR(60), Приведенные VARCHAR(100), Пригласитель VARCHAR(100), Комментарий VARCHAR(160), Время_начала DATETIME)")
        return True

    def get_data(self):
        self.cursor.execute('SELECT * FROM clients ORDER BY Готовность, Время_начала')
        self.data = self.cursor.fetchall()

    def view_data(self):
        self.model.setHorizontalHeaderLabels(["id", "Готовность", "Имя", "Приведенные", "Пригласитель", "Комментарий", "Время_начала"])
        self.get_data()

        for i_row, row_item in enumerate(self.data):
            for i_col, col_item in enumerate(row_item):
                if i_col == 0:
                    cell = QStandardItem()
                    cell.setData(col_item, Qt.DisplayRole)
                    self.model.setItem(i_row, i_col, cell)
                else:
                    cell = QStandardItem(str(col_item))
                    self.model.setItem(i_row, i_col, cell)

    def update_table_and_database(self, top_left_index, bottom_right_index):
        self.update_database(bottom_right_index)  # Обновление базы данных
        self.sort_table()

    def sort_table(self):
        self.model.sort(6, Qt.AscendingOrder)  # Сортировка по столбцу "Время_начала"
        self.model.sort(1, Qt.AscendingOrder)  # Сортировка по столбцу "Готовность"

    def add_new_client(self):
        name = self.ui_window.lineEdit.text()
        status = "Нет лр"
        comment = self.ui_window.textEdit.toPlainText()
        inviter = self.ui_window.search_line.text()
        row_position = self.model.rowCount()

        if inviter != "":
            for i_row, row_item in enumerate(self.data):
                if inviter == row_item[2]:
                    old_cell = self.model.item(i_row, 3)
                    new_cell = QStandardItem()
                    new_cell.setData(f"{old_cell.text()}, {name}" if old_cell is not None else str(name), Qt.DisplayRole)
                    self.model.setItem(i_row, 3, new_cell)
                    break

        self.model.insertRow(row_position)

        for item, col in zip([status, name, comment, inviter], [1, 2, 5, 4]):
            cell = QStandardItem(str(item))
            self.model.setItem(row_position, col, cell)

        self.new_window.close()
        self.get_data()
        
    def update_database(self, index):
        row = index.row()
        col = index.column()
        new_value = index.data()
        id_index = self.model.index(row, 0)
        id_value = self.model.data(id_index)
        column_name = self.model.horizontalHeaderItem(col).text()

        if col == 1 and new_value == "Исполняется":
            date = datetime.datetime.now()
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

        self.get_data()
        item = self.cursor.execute('SELECT MAX(id) FROM clients')
        result = self.cursor.fetchone()[0] if item is not None else 1
        cell = QStandardItem(str(result))
        self.model.setItem(row_index, 0, cell)

    def delete_client(self):
        selected_index = self.ui.tableView.currentIndex()

        if not selected_index.isValid():
            return None

        row = selected_index.row()
        id_value = self.data[row][0]
        self.model.removeRow(row)

        self.cursor.execute("DELETE FROM clients WHERE ID=?", (id_value,))
        self.connection.commit()
        self.get_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClientsList()
    window.show()
    sys.exit(app.exec())
