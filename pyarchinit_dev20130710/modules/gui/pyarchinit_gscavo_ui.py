# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_gscavo_ui.ui'
#
# Created: Sat Jul 13 11:55:46 2013
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialogiornalediscavo(object):
    def setupUi(self, Dialogiornalediscavo):
        Dialogiornalediscavo.setObjectName("Dialogiornalediscavo")
        Dialogiornalediscavo.resize(700, 591)
        Dialogiornalediscavo.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/iconSite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialogiornalediscavo.setWindowIcon(icon)
        self.gridLayout_9 = QtGui.QGridLayout(Dialogiornalediscavo)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_29 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(Dialogiornalediscavo)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_first_rec = QtGui.QPushButton(Dialogiornalediscavo)
        self.pushButton_first_rec.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/5_leftArrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName("pushButton_first_rec")
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 0, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(Dialogiornalediscavo)
        self.pushButton_prev_rec.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/4_leftArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon2)
        self.pushButton_prev_rec.setObjectName("pushButton_prev_rec")
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 1, 1, 2)
        self.pushButton_next_rec = QtGui.QPushButton(Dialogiornalediscavo)
        self.pushButton_next_rec.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/6_rightArrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon3)
        self.pushButton_next_rec.setObjectName("pushButton_next_rec")
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 4, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(Dialogiornalediscavo)
        self.pushButton_last_rec.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/7_rightArrows.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon4)
        self.pushButton_last_rec.setObjectName("pushButton_last_rec")
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 5, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/newrec.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon5)
        self.pushButton_new_rec.setObjectName("pushButton_new_rec")
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 6, 1, 1)
        self.pushButton_save = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/b_save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon6)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 0, 7, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon7)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.gridLayout.addWidget(self.pushButton_delete, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(70, 30, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/new_search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon8)
        self.pushButton_new_search.setObjectName("pushButton_new_search")
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 4, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon9)
        self.pushButton_search_go.setObjectName("pushButton_search_go")
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 5, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/images/sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon10)
        self.pushButton_sort.setObjectName("pushButton_sort")
        self.gridLayout.addWidget(self.pushButton_sort, 1, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/images/view_all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon11)
        self.pushButton_view_all.setObjectName("pushButton_view_all")
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 7, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(60, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(Dialogiornalediscavo)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_42 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_43 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName("label_43")
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(Dialogiornalediscavo)
        self.label_status.setMinimumSize(QtCore.QSize(50, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText("")
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName("label_status")
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(Dialogiornalediscavo)
        self.label_sort.setMinimumSize(QtCore.QSize(40, 0))
        self.label_sort.setSizeIncrement(QtCore.QSize(40, 0))
        self.label_sort.setBaseSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText("")
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName("label_sort")
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName("label_34")
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_27 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName("label_rec_corrente")
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName("label_rec_tot")
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line_8 = QtGui.QFrame(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout.addWidget(self.line_8)
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBox_sito = QtGui.QComboBox(Dialogiornalediscavo)
        self.comboBox_sito.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setFrame(False)
        self.comboBox_sito.setObjectName("comboBox_sito")
        self.comboBox_sito.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_sito, 0, 0, 3, 6)
        self.label = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 4, 0, 1, 1)
        self.label_8 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 7, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Dialogiornalediscavo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 7, 0, 1, 1)
        self.lineEdit_area = QtGui.QLineEdit(Dialogiornalediscavo)
        self.lineEdit_area.setObjectName("lineEdit_area")
        self.gridLayout_7.addWidget(self.lineEdit_area, 5, 0, 1, 1)
        self.lineEdit_quadrato = QtGui.QLineEdit(Dialogiornalediscavo)
        self.lineEdit_quadrato.setObjectName("lineEdit_quadrato")
        self.gridLayout_7.addWidget(self.lineEdit_quadrato, 5, 3, 1, 1)
        self.label_2 = QtGui.QLabel(Dialogiornalediscavo)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 7, 3, 1, 1)
        self.lineEdit_us = QtGui.QLineEdit(Dialogiornalediscavo)
        self.lineEdit_us.setAutoFillBackground(False)
        self.lineEdit_us.setMaxLength(32776)
        self.lineEdit_us.setObjectName("lineEdit_us")
        self.gridLayout_7.addWidget(self.lineEdit_us, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 5, 2, 1, 1)
        self.calendar = QtGui.QPushButton(Dialogiornalediscavo)
        self.calendar.setObjectName("calendar")
        self.gridLayout_7.addWidget(self.calendar, 5, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.giornalescavo = QtGui.QTextBrowser(Dialogiornalediscavo)
        self.giornalescavo.setFrameShape(QtGui.QFrame.WinPanel)
        self.giornalescavo.setFrameShadow(QtGui.QFrame.Plain)
        self.giornalescavo.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.giornalescavo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.giornalescavo.setObjectName("giornalescavo")
        self.gridLayout_8.addWidget(self.giornalescavo, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_8)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.label_8.setBuddy(self.lineEdit_us)
        self.label_7.setBuddy(self.lineEdit_area)
        self.label_2.setBuddy(self.lineEdit_quadrato)

        self.retranslateUi(Dialogiornalediscavo)
        QtCore.QMetaObject.connectSlotsByName(Dialogiornalediscavo)

    def retranslateUi(self, Dialogiornalediscavo):
        Dialogiornalediscavo.setWindowTitle(QtGui.QApplication.translate("Dialogiornalediscavo", "pyArchInit Gestione Scavi - Archeozoologia Quantificazioni", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Reload DB", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("Dialogiornalediscavo", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("Dialogiornalediscavo", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Sito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "US", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.calendar.setText(QtGui.QApplication.translate("Dialogiornalediscavo", "Calendar", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialogiornalediscavo = QtGui.QDialog()
    ui = Ui_Dialogiornalediscavo()
    ui.setupUi(Dialogiornalediscavo)
    Dialogiornalediscavo.show()
    sys.exit(app.exec_())

