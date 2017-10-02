#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import Adafruit_DHT
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from TestUI import Ui_Dialog

i = 0
j = 0
n = 5
final_humid = 0
final_temp = 0

class MyFirstGuiProgram(Ui_Dialog):
        def __init__(self, dialog):
                Ui_Dialog.__init__(self)
                self.setupUi(dialog)
#                value = float(self.textEdit.toPlainText())
                #print(self.value)
#                n = int(value)
                # Connect push button with a custom function (addInputTextToListbox)
                self.pushButton.clicked.connect(self.addDatatoTable)
                self.pushButton_2.clicked.connect(self.theend)

        def addDatatoTable(self):
            global i, j, n, final_humid, final_temp 
            #while i < n:
            self.tableWidget.insertRow(i)
            humidity, temperature = Adafruit_DHT.read_retry(22, 4)
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem("{0:.2f}".format(humidity)))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem("{0:.2f}".format(temperature)))
            self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(time.strftime("%H"+":"+"%M"+":"+"%S")))
            final_humid = final_humid + humidity
            final_temp = final_temp + temperature
            i = i+1
            #sys.exit()
            
            
        def theend(self):
            global i,final_humid, final_temp
            final_humid = final_humid/i
            final_temp = final_temp/i
            print("Average humidity: ",final_humid)
            print("Average temperature: ",final_temp)
            print("Over samples of: ", i)
            sys.exit()

if __name__ == '__main__':
        app = QtWidgets.QApplication(sys.argv)
        dialog = QtWidgets.QDialog()
        prog = MyFirstGuiProgram(dialog)

        dialog.show()
        sys.exit(app.exec_())


# temperature = temperature * 9/5.0 + 32
#if humidity is not None and temperature is not None:
#    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
#else:
#    print('Failed to get reading. Try again!')
#    sys.exit(1)
