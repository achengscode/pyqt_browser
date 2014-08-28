""" Client_qt.py

Meant to be a more robust version of client.py
Is implemented via the pyQT framework, a python port of
the Qt UI framework.

Includes a WebKit layout engine to faciliate HTML layouts.
"""
import sys
from PyQt5 import QtWidgets, QtCore, QtWebKitWidgets
from mainwindow import Ui_MainWindow

class webwindow(QtWidgets.QMainWindow):
    """
        Class that is derived from the mainWindow.ui file
        which defines the browser window.
    """
    def __init__(self, parent=None):
        """
            Web browser constructor.
            Sets the event handlers, as well as loading the UI
            from the mainWindow.ui file.
        """
        super(webwindow, self).__init__(parent)
        self.ui = Ui_MainWindow()  # define the UI
        self.ui.setupUi(self)

        homeurl = "http://www.google.com"
        self.ui.lineEdit.setText(homeurl)  # set the homepage

        #load the home page after
        self.ui.webView.setUrl(QtCore.QUrl(homeurl))

        # tell the browser we want to handle the link clicking ourselves
        self.ui.webView.page().setLinkDelegationPolicy(QtWebKitWidgets.QWebPage.DelegateAllLinks)

        # hook up the url bar to RETURN KEYPRESS and GO button
        self.ui.pushButton.clicked.connect(self.change_page)
        self.ui.lineEdit.returnPressed.connect(self.change_page)
        self.ui.webView.linkClicked.connect(self.clicked_link)

    def change_page(self):
        """
            Change page event handler (what happens when the html page changes)
        """
        url = self.ui.lineEdit.text()
        print(url)
        self.ui.webView.setUrl(QtCore.QUrl(url))

    def clicked_link(self, url):
        """
            Overrides the original clickedlink handler
        """
        self.ui.webView.setUrl(QtCore.QUrl(url))
        self.ui.lineEdit.clear()
        self.ui.lineEdit.insert(url.toString())
        self.ui.lineEdit.home(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = webwindow()
    window.show()
    app.exec_()