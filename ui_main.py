# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QMainWindow,
                               QPushButton, QSizePolicy, QTableView, QVBoxLayout,
                               QWidget, QTableWidgetItem, QComboBox)
import icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(759, 562)
        MainWindow.setStyleSheet(u"background-color: rgb(49, 49, 49);\n"
"font: 9pt \"Noto Serif\";\n"
"")
        MainWindow.setIconSize(QSize(28, 28))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 240px;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/newPrefix/plus-large-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"width: 240px;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 60);\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/delete-2-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButton_2)

#         self.pushButton_3 = QPushButton(self.centralwidget)
#         self.pushButton_3.setObjectName(u"pushButton_3")
#         self.pushButton_3.setStyleSheet(u"QPushButton {\n"
# "color: white;\n"
# "background-color: rgba(255, 255, 255, 30);\n"
# "border: 1px solid rgba(255, 255, 255, 40);\n"
# "border-radius: 7px;\n"
# "width: 240px;\n"
# "height: 50px;\n"
# "font-size: 14pt;\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "background-color: rgba(255, 255, 255, 40);\n"
# "}\n"
# "QPushButton:pressed {\n"
# "background-color: rgba(255, 255, 255, 60);\n"
# "\n"
# "}\n"
# "")
#         icon2 = QIcon()
#         icon2.addFile(u":/newPrefix/edit-content-svgrepo-com.svg", QSize(), QIcon.Normal, QIcon.Off)
        # self.pushButton_3.setIcon(icon2)
        # self.pushButton_3.setIconSize(QSize(30, 30))

        # self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout_2")
        self.tableView = QTableView(self.centralwidget)

        self.tableView.setObjectName(u"tableView")
        self.tableView.verticalHeader().setMinimumSectionSize(50)
        self.tableView.setStyleSheet(u"QTableView {\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QTableView::section {\n"
"border: none;\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"color: rgba(210, 210, 210, 210);\n"
"background-color: rgb(49, 49, 49);\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"\n"
"QTableView::item:selected:active {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.header = self.tableView.horizontalHeader()
        self.header.setStyleSheet("QHeaderView::section {\n"
"border: none;\n"
"background-color: rgb(70, 70, 70);\n"
"color: white;\n"
"height: 50px;\n"
"font-size: 12pt;\n"
"}")
        self.tableView.setAlternatingRowColors(False)
        self.tableView.setShowGrid(True)
        self.tableView.verticalHeader().hide()
        self.tableView.horizontalHeader().setDefaultSectionSize(135)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # Разрешаем растягивать последний столбец для заполнения доступного пространства
        # self.tableView.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.tableView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0441\u043e\u0432\u044b\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        # self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

