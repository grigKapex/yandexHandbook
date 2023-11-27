class Programmer:

    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.time = 0
        self.alltime = 0
        self.salary = 0
        self.post_office = {'Junior': 10, 'Middle': 15, 'Senior': 20}
        self.risecount = 0

    def work(self, time):
        self.alltime += time
        self.time = time
        key = self.post
        salary = (self.post_office[key] + self.risecount) * self.time
        self.salary += salary

    def rise(self):
        match self.post:
            case 'Junior':
                self.post = 'Middle'
            case 'Middle':
                self.post = 'Senior'
            case _:
                self.risecount += 1

    def info(self):
        return self.name + ' ' + str(self.alltime) + 'ч. ' + str(self.salary) + 'тгр.'