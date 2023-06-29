

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QDir.addSearchPath('icon', '/icons')
        
        self.show()
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
# app = QApplication([])

# window = QWidget()

# window.show()

# app.exec()