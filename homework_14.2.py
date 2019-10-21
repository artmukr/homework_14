# Implement 2 classes, the first one is Boss and the second one is Worker
# Worker has a property 'boss' which value must be an instance of Boss
# You can reassign this value, but you should check whether the new value
# is Boss. Each Boss has a list of his own workers. You should implement
# a method which allows you to add workers to a Boss. You're not allowed
# to add instances of Boss class to workers list!
# You can refactor the existing code.
# id_ - is just a random unique integer


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)

    def remove_worker(self, worker):
        self.workers.remove(worker)

    def __repr__(self):
        return f"{self.name} is a boss of {self.workers}"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.add_worker(self)

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, worker):
        if not isinstance(worker, Worker):
            self._boss.remove_worker(self)
            worker.add_worker(self)

    def __repr__(self):
        return f'{self.name} is worker'


b1 = Boss(456, "Tom", "Google")
b2 = Boss(658, "Doom", "S.F.P.D.")
w1 = Worker(125, "Dexter", "Google", b1)
w2 = Worker(658, "Lemmy", "S.F.P.D.", b1)
# print(w1)
# # print(w2)
# print(b1.workers)
# print(b1)

# print(w1.boss)
b2.add_worker(w1)
# print(b2.workers)

w2.boss = b2
print(b1.workers)
print(b2.workers)
w2.boss = w1
print(w1.boss)
