'''
Sample file for Github demo
'''

from distutils.archive_util import make_archive


class Car:
    def __init__(self, year:int, model:str):
        self.year = year
        self.model = model
        
if __name__ == "__main__":
    car = Car(2000, "328D")
    
