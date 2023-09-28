import PyQt5.QtWidgets as qw
import PyQt5.QtCore as qc
import os
import sys

class FileTree(qw.QWidget):
    def __init__(self, path):
        super().__init__()
        #Настройка окна
        self.setWindowTitle('FileTree')
        self.setGeometry(300, 300, 300, 300)
        #Файлы
        self.model=qw.QFileSystemModel()
        self.model.setRootPath(path)
        self.model.setFilter(qc.QDir.Hidden|qc.QDir.AllEntries|qc.QDir.NoDotAndDotDot)
        #Виджет древа
        self.tree=qw.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(path))
        #Виджет поиска
        self.search=qw.QLineEdit()
        self.search.setPlaceholderText('Поиск...')
        self.search.textChanged.connect(self.on_search)
        #Добавление виджетов
        place = qw.QVBoxLayout()
        place.addWidget(self.search)
        place.addWidget(self.tree)
        self.setLayout(place)

    def on_search(self):
        #Сортировка по имени
        filter=[self.search.text()+'*']
        self.model.setNameFilters(filter)
        self.model.setNameFilterDisables(False)

if __name__ == "__main__":
    app = qw.QApplication(sys.argv)
    path=os.path.expanduser('~')
    window = FileTree(path)
    window.show()
    sys.exit(app.exec_())

