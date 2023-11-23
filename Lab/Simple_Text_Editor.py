class CustomStack:
    def __init__(self):
        self.text = ""
        self.stack = []

    def insert(self, value):
        self.text += value
        self.stack.append(('1', value))

    def delete(self, value):
        deleted_text = self.text[-int(value):]
        self.text = self.text[:-int(value)]
        self.stack.append(('2', deleted_text))

    def get(self, value):
        print(self.text[value-1], end=" ")

    def undo(self):
        if self.stack:
            operation = self.stack.pop()
            if operation[0] == '1':
                self.text = self.text[:-len(operation[1])]
            elif operation[0] == '2':
                self.text += operation[1]


cmd = str(input())
cmd2 = cmd.split(",")

stack = CustomStack()

for i in cmd2:
    temp = i.split()
    if (temp[0]=='1'):
        stack.insert(temp[1])
    
    elif (temp[0]=='2'):
        stack.delete(temp[1])
    
    elif (temp[0]=='3'):
        stack.get(int(temp[1]))
