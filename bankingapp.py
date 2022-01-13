# Banking App

from ast import literal_eval


def get_type(input_data):
    try:
        return type(literal_eval(input_data))
    except (ValueError, SyntaxError):
        # A string, so return str
        return str


class Bank:
    def __init__(self, name, age, gender):
        # super().__init__(name, age, gender)
        self.balance = 0
        self.amount = 0
        self.name = name
        self.age = age
        self.gender = gender.lower()

        if get_type(self.name) != str:
            print('The name gotten is not a letter')
            self.name = input("input your name: ")
            # self.__init__(name, age, gender)

        try:
            if get_type(self.age) != int:
                print('kindly input your age in numbers')
                self.age = int(input('Enter your age in numbers: '))
        except:
            self.age = age

        try:
            if self.gender != 'male' and self.gender != 'female':
                print('The your gender should either be a male or a female')
                gender = input('Input your gender as a male or female')
                self.gender = gender
        except:
            self.gender = gender

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print('your updated amount is: #', self.balance)

    def withdraw(self, amount):
        self.amount = amount

        if self.amount > self.balance:
            print('Insufficient amount, your balance is #: ', self.balance)
        else:
            self.balance = self.balance - self.amount
            print('your new balance is #: ', self.balance)

    def view_balance(self):
        self.show_details()
        print('Account balance is: ', self.balance)

    def show_details(self):
        print('User details')
        print("Name: ", self.name)
        print('Age: ', self.age)
        print('Gender: ', self.gender)


'''

    def ensure_type(value, types):
    if isinstance(value, types):
        return value
    else:
        raise TypeError('Value {value} is {value_type}, but should be {types}!'.format(
            value=value, value_type=type(value), types=types))

    @property
    def name(self):
        return self.__dict__['name']

    @name.setter
    def name(self, value):
        self.__dict__['name'] = ensure_type(value, str)

    @property
    def age(self):
        return self.__dict__['name']

    @age.setter
    def age(self, value):
        self.__dict__['age'] = ensure_type(value, int)

    @property
    def gender(self):
        return self.__dict__['name']

    @gender.setter
    def gender(self, value):
        self.__dict__['gender'] = ensure_type(value, str)'''