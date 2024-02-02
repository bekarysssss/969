class StringMethods:

    def getString(self):
        self.input_string = input("Input: ")

    def printString(self):
        print("Output:", self.input_string.upper())

string = StringMethods()
string.getString()
string.printString()