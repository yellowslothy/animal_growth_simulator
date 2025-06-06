class Animal:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.level = 1
        self.experience = 0
        self.is_alive = True

    def status(self):
        return {
            "Age": self.age,
            "Level": self.level,
            "Experience": self.experience,
        }

    def feed(self, fish=False):
        if not self.is_alive:
            return
        if fish:
            self.experience += 10
            if self.experience >= self.level * 50:
                self.level_up()

    def die(self):
        self.is_alive = False

    def level_up(self):
        self.level += 1
        self.experience = 0
