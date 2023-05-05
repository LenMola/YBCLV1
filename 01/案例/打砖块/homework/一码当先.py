class Phone():
    def __init__(self,name,color,memory):
        self.name = name
        self.color = color
        self.memory = memory
phone = Phone('iPhone','黑色','128G')
print(phone.memory+phone.color+'的'+phone.name+'售价为6000元')



