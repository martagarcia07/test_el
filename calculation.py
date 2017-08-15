import os
import sys

# pass file as an argument 
# python main.py file.csv

# without passing file as an argument 
# it will look for a csv file in the current folder
# python main.py 
class calculation:
    def __init__(self,f):
        self.calculate(f)

    def calculate(self,f):
        try:
            directory= "results"
            if not os.path.exists(directory):
                os.makedirs(directory)
            new_file= open("results/result.csv",'w+')
            for l in f:
                encoded_scale= list(l.split(',')[1])
                result=0
                x=0
                reversed_line= reversed(list(l.split(',')[2].split('\n')[0]))
                for i in reversed_line:
                    y=encoded_scale.index(i)*len(encoded_scale)**(x)
                    x=x+1
                    result= result+y
                new_file.write(l.split(',')[0]+','+str(result)+'\n')
            new_file.close()
            return True
        except:
            print "file error"
            return False