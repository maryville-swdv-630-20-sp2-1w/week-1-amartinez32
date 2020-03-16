class Teams:
    
    def __init__(self,members):
        self.__myTeam = members
        
    def __len__(self):
        return len(self.__myTeam)
    
    def __contains__(self,classmate):
        return classmate in self.__myTeam
    
    def __iter__(self):
        self.__iter = 0
        return self
    
    def __next__(self):
        if self.__iter < len(self.__myTeam):
            classmate = self.__myTeam[self.__iter]
            self.__iter += 1
            return classmate
        else:
             raise StopIteration
        
        
    def check_for_classmates(self,name):
        
        if name in self.__myTeam:
            is_classmate = True
        else:
            is_classmate = False
        print('{} in in the class: {}\n'.format(name,is_classmate))

def main():
    
    classmates = Teams(['John', 'Steve', 'Tim'])
    
    
    # Exercise  1 
    mates = ['Sam', 'Tim', 'John', 'Angelo']
    for m in mates:
        classmates.check_for_classmates(m)
        
    # Exercise 2     
    name = iter(classmates)
    x = 0
    while x != len(classmates):
        print('{} is in the class.'.format(next(name)))
        x +=1
    # Exercise 3
    print('\n There are {} classmates in the class. \n'.format(len(classmates)))
    
    
        
        
main()
    
    