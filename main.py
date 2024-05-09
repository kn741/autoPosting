import postUi,sys,saveInfo
from PyQt6 import QtWidgets

credentials = saveInfo.load_credentials()
app = QtWidgets.QApplication(sys.argv)
PlatformPoster = QtWidgets.QMainWindow()
ui = postUi.Ui_PlatformPoster()
ui.setupUi(PlatformPoster)
ui.loadAccount(credentials)
PlatformPoster.show()
sys.exit(app.exec())

