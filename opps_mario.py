class Character():
    def __init__(self,name):
        self.name=name
        self.__life=3
        self.__score=0


    def kicked(self):
        self.__score +=10
        
    def punched(self):
        self.__score +=5

    def stabbed(self):
        self.__life -=1



    def displaylife(self):
        return self.__life

    def displayscore(self):
        return self.__score

    def intro(self):
        print(f" Name ---> {self.name}")
        print(f" Life ---> {self.__life}")
        print(f" Score ---> {self.__score}")

mario=Character("Mario")

mario.intro()
mario.stabbed()
mario.kicked()
mario.intro()
        
