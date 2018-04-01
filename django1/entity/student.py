class Student:

    id = None
    create_time = None
    update_time = None
    note = None
    number = None
    age = None
    name = None

    def __init__(self, id=None, create_time=None, update_time=None, note=None, number=None, age=None, name=None):
        self.id = id
        self.create_time = create_time
        self.update_time = update_time
        self.note = note
        self.number = number
        self.age = age
        self.name = name

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, item, value):
        self.__dict__[item] = value

