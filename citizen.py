class Citizen:  # create python class called Citizen

    """A class describing a citizen of the City of python"""#docstring explaining the class
    greeting ='For the glory of Python!'  # class variable which is a string set to For the glory of Python!


    #i
    def __init__(self, first_name:str, last_name:str):
        '''init method taking first name and last name as arguments-strings and assigns them as instance variables'''
        self.first_name=first_name
        self.last_name=last_name
    
    def full_name(self):
        '''instance method that returns a string  that combines the first and last name  instance variables, with a single space between them'''
        return f'{self.first_name} {self.last_name}'
