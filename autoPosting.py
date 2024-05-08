import postUi,sys
from PyQt6 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
PlatformPoster = QtWidgets.QMainWindow()
ui = postUi.Ui_PlatformPoster()
ui.setupUi(PlatformPoster)
PlatformPoster.show()
sys.exit(app.exec())

