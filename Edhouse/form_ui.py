# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Edhouse(object):
    def setupUi(self, Edhouse):
        if not Edhouse.objectName():
            Edhouse.setObjectName(u"Edhouse")
        Edhouse.resize(800, 600)
        self.gridLayout = QGridLayout(Edhouse)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.textArea = QPlainTextEdit(Edhouse)
        self.textArea.setObjectName(u"textArea")
        font = QFont()
        font.setPointSize(6)
        self.textArea.setFont(font)
        self.textArea.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.textArea)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.selectFile = QPushButton(Edhouse)
        self.selectFile.setObjectName(u"selectFile")
        self.selectFile.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"icon_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.selectFile.setIcon(icon)

        self.horizontalLayout.addWidget(self.selectFile)

        self.file = QLineEdit(Edhouse)
        self.file.setObjectName(u"file")

        self.horizontalLayout.addWidget(self.file)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.run = QPushButton(Edhouse)
        self.run.setObjectName(u"run")

        self.verticalLayout_4.addWidget(self.run)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Edhouse)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.summary = QLineEdit(Edhouse)
        self.summary.setObjectName(u"summary")

        self.verticalLayout.addWidget(self.summary)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(Edhouse)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.textAreaValidNumbers = QPlainTextEdit(Edhouse)
        self.textAreaValidNumbers.setObjectName(u"textAreaValidNumbers")
        self.textAreaValidNumbers.setFont(font)
        self.textAreaValidNumbers.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textAreaValidNumbers)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.retranslateUi(Edhouse)

        QMetaObject.connectSlotsByName(Edhouse)
    # setupUi

    def retranslateUi(self, Edhouse):
        Edhouse.setWindowTitle(QCoreApplication.translate("Edhouse", u"Widget", None))
#if QT_CONFIG(tooltip)
        self.selectFile.setToolTip(QCoreApplication.translate("Edhouse", u"<html><head/><body><p>Select File</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selectFile.setText("")
        self.file.setText("")
        self.file.setPlaceholderText(QCoreApplication.translate("Edhouse", u"Select file", None))
        self.run.setText(QCoreApplication.translate("Edhouse", u"RUN", None))
        self.label.setText(QCoreApplication.translate("Edhouse", u"SUM", None))
        self.label_2.setText(QCoreApplication.translate("Edhouse", u"Valid numbers", None))
    # retranslateUi

