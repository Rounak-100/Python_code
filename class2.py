class person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print(f"Hi, I am {self.name}")

john=person("Rounak Koner")
print(john.name)
john.talk()
bob=person("Bob Smith")
bob.talk()
