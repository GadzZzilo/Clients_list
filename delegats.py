from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtGui import QPainter, QColor, QPalette
from PySide6.QtWidgets import QStyledItemDelegate, QComboBox, QStyleOptionViewItem, QLineEdit


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
            painter.restore()
        else:
            # Если условие не выполняется, отображаем ячейку по умолчанию
            super().paint(painter, option, index)


class ColorDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setStyleSheet('color: white;')
        return editor