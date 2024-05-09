import postUi,sys,saveInfo
from PyQt6 import QtWidgets
app = QtWidgets.QApplication(sys.argv)
PlatformPoster = QtWidgets.QMainWindow()
ui = postUi.Ui_PlatformPoster()
ui.setupUi(PlatformPoster)
credentials = saveInfo.load_credentials()
ui.loadAccount(credentials)
PlatformPoster.show()
sys.exit(app.exec())

