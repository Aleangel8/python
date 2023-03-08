class Demo:
    def __secreto(self): #los __ hace que le cambie el nombre
        print("Nadie puede saber")

    def publico(self):
        print("Todos pueden saber")

    def getSecret(self, pw):
        if(pw == "123"):
            print(self.__secreto())
        else:
            print("sin acceso")

demo = Demo()
demo.publico()
demo.getSecret("123")
demo.getSecret("234523")
#demo.__secreto()
print(dir(demo))