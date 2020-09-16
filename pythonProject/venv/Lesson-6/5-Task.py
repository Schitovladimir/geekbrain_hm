class Stationary():
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Start rendering")

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Start rendering with Pen")

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Start rendering with Pencil")

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Start rendering with Handle")

pen = Pen("Pen")
pencil = Pencil("Pencil")
handle = Handle("Handle")
pen.draw()
pencil.draw()
handle.draw()