'''
Sample file for Github demo
second line of text
third line of text
fourth line of text
'''

from distutils.archive_util import make_archive

class Car:
    def __init__(self, year:int, make:str, model:str):
        self.year = year
        self.make = make
        self.model = model
        
    '''
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"    
    '''    
    
        
if __name__ == "__main__":
    car = Car(2000, "BMW","328D")
    print(car)
