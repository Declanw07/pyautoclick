# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(531, 193)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 511, 131))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.window_label = QLabel(self.gridLayoutWidget)
        self.window_label.setObjectName(u"window_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.window_label)

        self.window_combobox = QComboBox(self.gridLayoutWidget)
        self.window_combobox.setObjectName(u"window_combobox")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.window_combobox)

        self.click_button_label = QLabel(self.gridLayoutWidget)
        self.click_button_label.setObjectName(u"click_button_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.click_button_label)

        self.click_button_combobox = QComboBox(self.gridLayoutWidget)
        self.click_button_combobox.setObjectName(u"click_button_combobox")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.click_button_combobox)

        self.click_delay_label = QLabel(self.gridLayoutWidget)
        self.click_delay_label.setObjectName(u"click_delay_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.click_delay_label)

        self.click_delay_spinbox = QSpinBox(self.gridLayoutWidget)
        self.click_delay_spinbox.setObjectName(u"click_delay_spinbox")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.click_delay_spinbox)

        self.hold_click_label = QLabel(self.gridLayoutWidget)
        self.hold_click_label.setObjectName(u"hold_click_label")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.hold_click_label)

        self.hold_click_checkbox = QCheckBox(self.gridLayoutWidget)
        self.hold_click_checkbox.setObjectName(u"hold_click_checkbox")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.hold_click_checkbox)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 2)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 531, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PyAutoClicker", None))
        self.window_label.setText(QCoreApplication.translate("MainWindow", u"Window", None))
        self.click_button_label.setText(QCoreApplication.translate("MainWindow", u"Click Button", None))
        self.click_delay_label.setText(QCoreApplication.translate("MainWindow", u"Click Delay", None))
        self.hold_click_label.setText(QCoreApplication.translate("MainWindow", u"Hold Click", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

