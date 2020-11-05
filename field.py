import random

class FIELD():
    # init field and properties
    def __init__(self):
        self.x, self.y = self.set_field()
        self.num_shop, self.num_jobchange = self.set_events()

        self.init_field(self.x, self.y, self.num_shop, self.num_jobchange)

    # set field size
    def set_field(self):
        x = int(input('input x'))
        y = int(input('input y'))
        return x, y

    # set any event num
    def set_events(self):
        num_shop = 4
        num_jobchange = 2
        return num_shop, num_jobchange

    def init_field(self, x, y, num_shop, num_jobchange):
        field = [["Normal" for i in range(x)] for j in range(y)]
        print(field)
        cnt = 0
        while cnt < num_shop:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field[randX][randY] == "Normal":
                field[randX][randY] = "Shop"
                cnt += 1
        print(field)
        cnt = 0
        while cnt < num_jobchange:
            randX = random.randrange(0, x-1)
            randY = random.randrange(0, y-1)
            if field[randX][randY] == "Normal":
                field[randX][randY] = "JobChange"
                cnt += 1
        print(field)
    # run some events on field
    # add any more events
    def event1():
        pass

f = FIELD()
