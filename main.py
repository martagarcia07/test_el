import os
import sys

# pass file as an argument 
# python main.py file.csv

# without passing file as an argument 
# it will look for a csv file in the current folder
# python main.py 
from calculation import calculation

if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.abspath(sys.argv[1]) and os.path.abspath(sys.argv[1]).endswith(".csv"):
        file = sys.argv[1]   
    else:
        for f in os.listdir("."):
            if f.endswith(".csv"):
                file = os.path.join(".", f)
    f = open(file,'r')
    result = calculation(f)