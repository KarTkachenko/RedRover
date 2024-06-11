class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def hello(self):
        return f'{self.fname} says Hello'


class Programmer(Person):
    def __init__(self, language, job_title):
        # super().__init__(fname, lname)
        self.language = language
        self.job_title = job_title


coder1 = Programmer('Python', 'qa_engineer', 'kjhgff')
person1 = Person('Olga', 'Ytuo')
# print(person1.fname)
print(coder1.hello())
