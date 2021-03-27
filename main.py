try:
	import json 
	from PyQt5 import QtWidgets as qtw
	from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QSizePolicy, QGridLayout
	import sys
except ImportError:
	print("ERROR: loading imports failed - __main__")
	exit(0)


class pyTranslator():
	def __init__(self):
		self.wordRuns = None
		self.wordsNordicTab = None
		self.dictionaryYoungerFuthark = None
		self.dictionary = None

	def input_run_words(self, wordRunss):
		#print("Use this runes to write -> ᚠ, ᚢ, ᚦ, ᚬ, ᚱ, ᚴ, ᚼ, ᚾ, ᛁ, ᛅ, ᛦ, ᛋ, ᛏ, ᛒ, ᛘ, ᛚ")
		#print("Write text : ")
		self.wordRuns = wordRunss.split()
		self.wordsNordicTab = []
		self.dictionaryYoungerFuthark = {
			ord("ᚠ") : ["f", "v"],
			ord("ᚢ") : ["u", "v", "w", "y", "o", "ø"],
			ord("ᚦ") : ["þ", "ð"],
			ord("ᚬ") : ["o", "ą", "æ"],
			ord("ᚱ") : ["r"],
			ord("ᚴ") : ["k", "g"],
			ord("ᚼ") : ["h"],
			ord("ᚾ") : ["n"],
			ord("ᛁ") : ["i", "e"],
			ord("ᛅ") : ["a", "e", "æ"],
			ord("ᛦ") : ["r"],
			ord("ᛋ") : ["s"],
			ord("ᛏ") : ["t", "d"],
			ord("ᛒ") : ["b", "p"],
			ord("ᛘ") : ["m"],
			ord("ᛚ") : ["l"]
		}

		self.dictionary = json.load(open('dictionary.json', encoding='utf-8'))

	def runs_to_nordic(self):
		#print(self.wordRuns)

		for i in range(len(self.wordRuns)):
			nordicWord = []
			for j in range(len(self.wordRuns[i])):
				nordicWord.append(self.dictionaryYoungerFuthark[ord(self.wordRuns[i][j])])
			self.wordsNordicTab.append(nordicWord)

		#print(self.wordsNordicTab)

	def translate_nordic(self):
		allWord = []
		for word in self.wordsNordicTab:
			allPosibleCombinationWord = self.stratCheckWord(word)
			#print(allPosibleCombinationWord)

			allWord.append(self.checkWordInDict(allPosibleCombinationWord, self.dictionary))
			#print(allWord)
		
		return allWord
	
	def stratCheckWord(self, word):
		lista = []
		backup = word[0]
		word.pop(0)

		if len(word) >= 1:
			for i in backup:
				self.checkWords(i, word, lista)
		else:
			for i in backup:
				lista.append(i)
		
		return lista

	def checkWords(self, prefix, word, lista):
		letter = word[0]

		if(len(word) == 1):
			for i in letter:
				lista.append(prefix+i)
		else:
			newWord = []
			for i in range(1, len(word)):
				newWord.append(word[i])

			for i in letter:
				self.checkWords(prefix+i, newWord, lista)

	def checkWordInDict(self, listOfWords, dictionary):
		englishWords = []
		for word in listOfWords:
			if word in dictionary:
				englishWords.append(dictionary[word])
		
		return englishWords


class pyGui(qtw.QWidget):
	def __init__(self): 
		super().__init__()

		self.text = ""
		self.translate = pyTranslator()

		self.setWindowTitle("Runs Translator") #Ustawia tytuł okna
		self.setLayout(qtw.QVBoxLayout())
		self.keypad()

		self.show()
	
	def keypad(self):
		conteiner = qtw.QWidget()
		conteiner.setLayout(qtw.QGridLayout())

		#Buttons
		self.input_text =  qtw.QLineEdit()
		self.output_text = qtw.QLineEdit()
		btn_result = qtw.QPushButton('Translate', clicked = self.func_result)
		btn_clear = qtw.QPushButton('Clear', clicked = self.func_clear)
		btn_1 = qtw.QPushButton('ᚠ', clicked = lambda:self.run_press('ᚠ'))
		btn_2 = qtw.QPushButton('ᚢ', clicked = lambda:self.run_press('ᚢ'))
		btn_3 = qtw.QPushButton('ᚦ', clicked = lambda:self.run_press('ᚦ'))
		btn_4 = qtw.QPushButton('ᚬ', clicked = lambda:self.run_press('ᚬ'))
		btn_5 = qtw.QPushButton('ᚱ', clicked = lambda:self.run_press('ᚱ'))
		btn_6 = qtw.QPushButton('ᚴ', clicked = lambda:self.run_press('ᚴ'))
		btn_7 = qtw.QPushButton('ᚼ', clicked = lambda:self.run_press('ᚼ'))
		btn_8 = qtw.QPushButton('ᚾ', clicked = lambda:self.run_press('ᚾ'))
		btn_9 = qtw.QPushButton('ᛁ', clicked = lambda:self.run_press('ᛁ'))
		btn_10 = qtw.QPushButton('ᛅ', clicked = lambda:self.run_press('ᛅ'))
		btn_11 = qtw.QPushButton('ᛦ', clicked = lambda:self.run_press('ᛦ'))
		btn_12 = qtw.QPushButton('ᛋ', clicked = lambda:self.run_press('ᛋ'))
		btn_13 = qtw.QPushButton('ᛏ', clicked = lambda:self.run_press('ᛏ'))
		btn_14 = qtw.QPushButton('ᛒ', clicked = lambda:self.run_press('ᛒ'))
		btn_15 = qtw.QPushButton('ᛘ', clicked = lambda:self.run_press('ᛘ'))
		btn_16 = qtw.QPushButton('ᛚ', clicked = lambda:self.run_press('ᛚ'))
		btn_space = qtw.QPushButton('Space', clicked = lambda:self.run_press(' '))

		#Add to layout
		conteiner.layout().addWidget(self.input_text, 0, 0, 1, 4)
		conteiner.layout().addWidget(self.output_text, 1, 0, 1, 4)
		conteiner.layout().addWidget(btn_result, 2, 0, 1, 2)
		conteiner.layout().addWidget(btn_clear, 2, 2, 1, 2)
		conteiner.layout().addWidget(btn_1, 3, 0)
		conteiner.layout().addWidget(btn_2, 3, 1)
		conteiner.layout().addWidget(btn_3, 3, 2)
		conteiner.layout().addWidget(btn_4, 3, 3)
		conteiner.layout().addWidget(btn_5, 4, 0)
		conteiner.layout().addWidget(btn_6, 4, 1)
		conteiner.layout().addWidget(btn_7, 4, 2)
		conteiner.layout().addWidget(btn_8, 4, 3)
		conteiner.layout().addWidget(btn_9, 5, 0)
		conteiner.layout().addWidget(btn_10, 5, 1)
		conteiner.layout().addWidget(btn_11, 5, 2)
		conteiner.layout().addWidget(btn_12, 5, 3)
		conteiner.layout().addWidget(btn_13, 6, 0)
		conteiner.layout().addWidget(btn_14, 6, 1)
		conteiner.layout().addWidget(btn_15, 6, 2)
		conteiner.layout().addWidget(btn_16, 6, 3)
		conteiner.layout().addWidget(btn_space, 7, 0, 1, 4)
		self.layout().addWidget(conteiner)

		#Resaizning
		self.input_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.output_text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_clear.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_10.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_11.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_12.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_13.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_14.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_15.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_16.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		btn_space.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

	def func_clear(self):
		self.text = ""
		self.input_text.clear()
		self.output_text.clear()

	def run_press(self, run):
		self.text += run
		self.input_text.setText(self.text)

	def func_result(self):
		runs = self.text
		print("Program Strarted ...") 
		self.translate.input_run_words(runs)
		self.translate.runs_to_nordic()
		output = self.translate.translate_nordic()
		print(output)
		self.output_text.setText(str(output))


App = QApplication(sys.argv)
window = pyGui() 
App.setStyle(qtw.QStyleFactory.create('Fusion'))
App.exec_()