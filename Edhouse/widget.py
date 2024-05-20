# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Edhouse
from task import ukol
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Edhouse()
        self.ui.setupUi(self)
        self.plain_text = ""
        self.path = "mapka.txt"
        self.ui.run.clicked.connect(self.on_run)
        self.ui.selectFile.clicked.connect(self.on_select_file)
    
    def on_select_file(self):
        try:
            file, _ = QFileDialog.getOpenFileName(self, "Open file", os.getcwd())
            file_name = os.path.basename(file)
            self.ui.file.setText(file_name)
            self.path = file
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
    
    def on_run(self):
        try:
            file = self.path
            summary, mapka, myValidNumbers = ukol(file)
            self.ui.summary.setText(str(summary))
            self.textArea = ""
            max_length = max(len("".join(line)) for line in mapka)
            for line in mapka:
                self.textArea += "".join(line).ljust(max_length) + "\n"
            self.ui.textArea.setPlainText(self.textArea)
            self.ui.textAreaValidNumbers.setPlainText(str(myValidNumbers))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
