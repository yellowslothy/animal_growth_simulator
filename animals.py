class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.exp = 0
        self.level = 1

    def feed(self):
        self.exp += 10
        if self.exp >= self.level * 50:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.age += 1

    def status(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Level": self.level,
            "Experience": self.exp
        }
