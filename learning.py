# ToDo:
#1 -  parse cases (new method generated
#2 -  plot
## Everything Starts here
build = "1.0"
print ("Everything Starts here")
print ("Build "+ build)

from PyQt5 import QtWidgets, uic
import sys
from urllib.request import Request, urlopen

class Ui(QtWidgets.QMainWindow):


    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('d1.ui', self) # Load the .ui file
        self.fetch.clicked.connect(self.getCountry)
        self.show() # Show the GUI
        webpg= self.lineEdit.text()
        data = self.getHTMLData(webpg)
        print ("--------\n")
        # print(data)
        self.getCountries(data)

    def getCountries(self, data):
        out = data.split(b'\n')
        listOfCountries = []
        for x in out:
            if (x.find(b'a class="mt_a" href="country/') != -1):
                end = x.find(b'</a>')
                start = x.find(b'/">')+3
                substring = x[start:end].decode('utf-8')

                listOfCountries.append(str(substring))
                self.comboBox.setStyleSheet("QComboBox { combobox-popup: 0; }");
                self.comboBox.clear()
                self.comboBox.addItems(listOfCountries)
       
        
    def getHTMLData (self,URL):
        print("This is the reference webpage! --" + URL + "--")
        req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        data = urlopen(req).read()
        return data
    
    def getCountry(self):
        print("click you fuckface!")
        content = self.comboBox.currentText()
        print(" This is it "+ content)
        webpg= "https://www.worldometers.info/coronavirus/country/"+content+"/"
        data = self.getHTMLData(webpg)
        #print(data)
        self.parseData(data)
   
    def parseData(self,data):
        print("Entered parsing data!")
        out = data.split(b'\n')
        listOfCases = []
        listOfDates = []
        count =1 
        for x in out:
            
            #dates only 1 time
            
            if ((x.find(b'categories: ["Feb 15, 2020","Feb 16, 2020","Feb 17, 2020"') != -1) & (count>0)):
                count=0
                print(x)    
                end = x.find(b'[')
                start = x.find(b']')+3
                substring = x[start:end].decode('utf-8')
                print(substring)

                
       
        
    def getCases (self,data):
        out = data.split(b'\n')
        dates = []
        series = []
        for x in out:
            if (x.find(b'a class="mt_a" href="country/') != -1):
                end = x.find(b'</a>')
                start = x.find(b'/">')+3
                substring = x[start:end].decode('utf-8')

                listOfCountries.append(str(substring))
                self.comboBox.setStyleSheet("QComboBox { combobox-popup: 0; }");
                self.comboBox.clear()
                self.comboBox.addItems(listOfCountries)
        
app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application