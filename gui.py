import sys, os, subprocess
FILEPATH = os.path.abspath(__file__)
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from random import randint


#Create a single cell object and its attributes
class Cell:
    def __init__(self, x, y, mine_or_number, row, column):
        self.checked = False
        self.x = x
        self.y = y
        self.row = row
        self.column = column
        self.mine_or_number = mine_or_number
        self.hidden = True
        self.label = QLabel(guiGame.mainWindow)
        self.picture()
        self.label.mousePressEvent = self.mouseClick

    #Define which picture a cell will have depending on mine_or_number variable and hidden attribute
    def picture(self):
        if self.hidden:
            pixmap = QPixmap("hidden.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 9:
            pixmap = QPixmap("mina.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 8:
            pixmap = QPixmap("osem.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 7:
            pixmap = QPixmap("sedem.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 6:
            pixmap = QPixmap("sest.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 5:
            pixmap = QPixmap("pet.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 4:
            pixmap = QPixmap("stiri.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 3:
            pixmap = QPixmap("tri.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 2:
            pixmap = QPixmap("dva.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 1:
            pixmap = QPixmap("ena.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        elif not(self.hidden) and self.mine_or_number == 0:
            pixmap = QPixmap("nula.png")
            self.label.setPixmap(pixmap)
            self.label.move(self.x, self.y)

        #When mouse clicks on a single cell events occur
    def mouseClick(self, ev):
        if self.hidden == True:
            self.hidden = False #Reveals cell
            self.picture() #Give revealed picture
            self.checkNeighbours() #Checks for events on neighbour cells
            if guiGame.mainWindow.turn: #Checks if mine is hit or gives round to other player
                if self.mine_or_number == 9:
                    guiGame.player1Score += 1
                    if guiGame.player1Score > (guiGame.mineField.numberOfMines // 2):
                        #mainWindow.showDialog2()
                        print "Zmagal je", guiGame.mainWindow.player1
                        choice2 = QMessageBox.question(guiGame.mainWindow, "Game over",
                                                            "Minesweeper battle is over. " + guiGame.mainWindow.player1 + " has won!. Do you want restart the game?",
                                                            QMessageBox.No | QMessageBox.Yes)
                        if choice2 == QMessageBox.Yes:
                           try:
                               subprocess.Popen([sys.executable, FILEPATH])
                           except OSError as exception:
                               print('ERROR: could not restart aplication:')
                               print('  %s' % str(exception))
                           else:
                               qApp.quit()
                        else:
                            sys.exit()
                    guiGame.displayPlayer1Score.clear()
                    guiGame.displayPlayer1Score.setText(str(guiGame.player1Score))
                    guiGame.mainWindow.turn = True
                else:
                    guiGame.mainWindow.turn = False
                    guiGame.displayTurn.clear()
                    guiGame.displayTurn.setText("It\'s " + guiGame.mainWindow.player2 + "\'s turn")

            else:
                if self.mine_or_number == 9:
                    guiGame.player2Score += 1
                    if guiGame.player2Score > (guiGame.mineField.numberOfMines // 2):
                        #guiGame.mainWindow.showDialog2()
                        print "Zmagal je ", guiGame.mainWindow.player2
                        choice2 = QMessageBox.question(guiGame.mainWindow, "Game over",
                                                "Minesweeper battle is over. " + guiGame.mainWindow.player2 + " has won!. Do you want to restart the game?",
                                                QMessageBox.No | QMessageBox.Yes)
                        if choice2 == QMessageBox.Yes:
                           try:
                               subprocess.Popen([sys.executable, FILEPATH])
                           except OSError as exception:
                               print('ERROR: could not restart aplication:')
                               print('  %s' % str(exception))
                           else:
                               qApp.quit()
                        else:
                            sys.exit()
                    guiGame.displayPlayer2Score.clear()
                    guiGame.displayPlayer2Score.setText(str(guiGame.player2Score))
                    guiGame.mainWindow.turn = False
                else:
                    guiGame.mainWindow.turn = True
                    guiGame.displayTurn.clear()
                    guiGame.displayTurn.setText("It\'s " + guiGame.mainWindow.player1 + "\'s turn")

    def checkNeighbours(self):
        """Function will do something only if player hits empty cell,
        it will reveal all neighbour cells including all neighbour
        cells of other empty neighbour cells. It will go into
        recursive function."""

        if self.mine_or_number == 0 and self.checked == False:
            self.checked = True
            if (self.row+1 != len(field[self.row])) and (self.column-1 != -1):
                field[self.row+1][self.column-1].hidden = False
                field[self.row+1][self.column-1].picture()
                if (field[self.row+1][self.column-1].mine_or_number == 0):
                    field[self.row+1][self.column-1].checkNeighbours()

            if (self.column-1 != -1):
                field[self.row][self.column-1].hidden = False
                field[self.row][self.column-1].picture()
                if (field[self.row][self.column-1].mine_or_number == 0):
                    field[self.row][self.column-1].checkNeighbours()

            if (self.row-1 != -1) and (self.column-1 != -1):
                field[self.row-1][self.column-1].hidden = False
                field[self.row-1][self.column-1].picture()
                if (field[self.row-1][self.column-1].mine_or_number == 0):
                    field[self.row-1][self.column-1].checkNeighbours()

            if (self.row-1 != -1):
                field[self.row-1][self.column].hidden = False
                field[self.row-1][self.column].picture()
                if (field[self.row-1][self.column].mine_or_number == 0):
                    field[self.row-1][self.column].checkNeighbours()

            if (self.row-1 != -1) and (self.column+1 != len(field)):
                field[self.row-1][self.column+1].hidden = False
                field[self.row-1][self.column+1].picture()
                if (field[self.row-1][self.column+1].mine_or_number == 0):
                    field[self.row-1][self.column+1].checkNeighbours()

            if (self.column+1 != len(field)):
                field[self.row][self.column+1].hidden = False
                field[self.row][self.column+1].picture()
                if (field[self.row][self.column+1].mine_or_number == 0):
                    field[self.row][self.column+1].checkNeighbours()

            if (self.row+1 != len(field[self.row])) and (self.column+1 != len(field)):
                field[self.row+1][self.column+1].hidden = False
                field[self.row+1][self.column+1].picture()
                if (field[self.row+1][self.column+1].mine_or_number == 0):
                    field[self.row+1][self.column+1].checkNeighbours()

            if (self.row+1 != len(field[self.row])):
                field[self.row+1][self.column].hidden = False
                field[self.row+1][self.column].picture()
                if (field[self.row+1][self.column].mine_or_number == 0):
                    field[self.row+1][self.column].checkNeighbours()

#It creates arry for cells.
class MineField(list):
    def __init__(self, rows, columns):
        super(MineField, self).__init__()
        self.rows = rows
        self.columns = columns
        self.randomMines()
        global field
        field = [[0]*self.columns for x in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.columns):
                if [i, j] in self.locationOfMines:
                    field[i][j] = Cell(((i+1)*34), ((j+1)*34), 9, i, j)
                else:
                    field[i][j] = Cell(((i+1)*34), ((j+1)*34), 0, i, j)
        self.countNeighbourMines()


    def randomMines(self):
        self.numberOfMines = int((0.2 * self.rows * self.columns)+1)
        temp_numb = self.numberOfMines
        self.locationOfMines = []
        similar =  False
        while temp_numb != 0:
            similar = False
            temp_location = [randint(0, self.rows-1), randint(0, self.columns-1)]
            for i in range(len(self.locationOfMines)):
                if temp_location == self.locationOfMines[i]:
                    similar = True
            if similar == False:
                self.locationOfMines.append(temp_location)
                temp_numb -= 1

    def countNeighbourMines(self):
        mine_counter = 0
        for g in range(self.rows):
            for h in range(self.columns):

                if (g+1 != self.rows) and (h-1 != -1) and field[g+1][h-1].mine_or_number == 9:
                    mine_counter += 1
                if (h-1 != -1) and field[g][h-1].mine_or_number == 9:
                    mine_counter += 1
                if (g-1 != -1) and (h-1 != -1) and field[g-1][h-1].mine_or_number == 9:
                    mine_counter += 1
                if (g-1 != -1) and field[g-1][h].mine_or_number == 9:
                    mine_counter += 1
                if (h+1 != self.columns) and (g-1 != -1) and field[g-1][h+1].mine_or_number == 9:
                    mine_counter += 1
                if (h+1 != self.columns) and field[g][h+1].mine_or_number == 9:
                    mine_counter += 1
                if (g+1 != self.rows) and (h+1 != self.columns) and field[g+1][h+1].mine_or_number == 9:
                    mine_counter += 1
                if (g+1 != self.rows) and (field[g+1][h].mine_or_number == 9):
                    mine_counter += 1

                if field[g][h].mine_or_number != 9:
                    field[g][h].mine_or_number = mine_counter
                mine_counter = 0

class GuiGame:
    def __init__(self):
        self.player1Score = 0
        self.player2Score = 0
        self.mainWindow = MainWindow()
        self.mainWindow.player1 = guiMenu.mainWindow.player1
        self.mainWindow.player2 = guiMenu.mainWindow.player2
        self.mainWindow.width = 1000
        self.mainWindow.height = 740
        self.mainWindow.setFixedSize(self.mainWindow.width, self.mainWindow.height)
        self.imageDisplayPlayer2()
        self.imageDisplayPlayer1()
        self.imageTurn()

    def imageTurn(self):
        self.displayTurn = QLabel("It is " + self.mainWindow.player1 + "'s turn", self.mainWindow)
        self.displayTurn.setGeometry(730, 256, 250, 32)
        self.displayTurn.setFont(QFont("Times", 18, QFont.Bold))

    def imageDisplayPlayer1(self):
        self.displayPlayer1 = QLabel(self.mainWindow.player1 + " score:", self.mainWindow)
        self.displayPlayer1.setGeometry(730, 32, 250, 32)
        self.displayPlayer1.setFont(QFont("Times", 16, QFont.Bold))
        self.displayPlayer1.repaint()

        self.displayPlayer1Score = QLabel(str(self.player1Score), self.mainWindow)
        self.displayPlayer1Score.setGeometry(730, 64, 250, 32)
        self.displayPlayer1Score.setFont(QFont("Times", 14))

    def imageDisplayPlayer2(self):
        self.displayPlayer2 = QLabel(self.mainWindow.player2 + " score:", self.mainWindow)
        self.displayPlayer2.setGeometry(730, 96, 250, 32)
        self.displayPlayer2.setFont(QFont("Times", 16, QFont.Bold))

        self.displayPlayer2Score = QLabel(str(self.player2Score), self.mainWindow)
        self.displayPlayer2Score.setGeometry(730, 128, 250, 32)
        self.displayPlayer2Score.setFont(QFont("Times", 14))


class GuiMenu:
    def __init__(self):
        self.notQuit = False
        self.mainWindow = MainWindow() #Create main window as QWidget
        self.mainWindow.width = 400
        self.mainWindow.height = 300
        self.mainWindow.setFixedSize(self.mainWindow.width, self.mainWindow.height)
        self.MainMenu() #Creates main menu

    def MainMenu(self):
        #Create New game button
        self.newGame = QPushButton('New Game', self.mainWindow)
        self.newGame.resize(100, 50)
        self.newGame.move(10, 20)
        self.newGame.clicked.connect(self.NewGame)

        #Create Player 1 button and place it
        self.player1Button = QPushButton(self.mainWindow.player1, self.mainWindow)
        self.player1Button.resize(100, 50)
        self.player1Button.move(10, 80)
        self.player1Button.clicked.connect(lambda: self.EnterName(1)) #Here at event used temporal function lambda

        #Create player 2 button and place it
        self.player2Button = QPushButton(self.mainWindow.player2, self.mainWindow)
        self.player2Button.resize(100, 50)
        self.player2Button.move(10, 140)
        self.player2Button.clicked.connect(lambda: self.EnterName(2)) #Here at event used temporal function lambda

        #Create quit button and place it
        self.quitGame = QPushButton("Quit", self.mainWindow)
        self.quitGame.resize(100, 50)
        self.quitGame.move(10, 200)
        self.quitGame.clicked.connect(sys.exit)

        #Create main picture logo and place it
        self.logo = QLabel(self.mainWindow)
        pixmap = QPixmap("mina_logo.png")
        self.logo.setPixmap(pixmap)
        self.logo.move(120, 10)

    def NewGame(self):
        print("Staring a new game!!")
        self.mainWindow.hide()
        guiGame.mainWindow.show()

    def EnterName(self, playerNumber):
        if playerNumber == 1:
            text, ok = QInputDialog.getText(self.mainWindow, 'Text Input Dialog', 'Enter your name:')

            if ok:
                self.player1Button.setText(str(text))
                self.mainWindow.player1 = text
                guiGame.mainWindow.player1 = text
                guiGame.displayPlayer1.clear()
                guiGame.displayPlayer1.setText(str(guiGame.mainWindow.player1))
                guiGame.displayTurn.clear()
                guiGame.displayTurn.setText("It\'s " + guiGame.mainWindow.player1 + "\'s turn")
        else:
            text, ok = QInputDialog.getText(self.mainWindow, 'Text Input Dialog', 'Enter your name:')

            if ok:
                self.player2Button.setText(str(text))
                self.mainWindow.player2 = text
                guiGame.mainWindow.player2 = text
                guiGame.displayPlayer2.clear()
                guiGame.displayPlayer2.setText(str(guiGame.mainWindow.player2))

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.turn = True
        self.player1 = "Player 1"
        self.player2 = "Player 2"
        self.width = 0
        self.height = 0
        self.setWindowTitle("Minesweeper")
        self.setWindowIcon(QIcon('mina_logo.png'))

app = QApplication([])
guiMenu = GuiMenu()
guiGame = GuiGame()
guiGame.mineField = MineField(20, 20)
guiMenu.mainWindow.show()
app.exec_()
