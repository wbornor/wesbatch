#!/cygdrive/c/Python25/python
import sys, os

def get_distincts(entries, distincts=[]):
    for entry in entries:
        try:
            i = distincts.index(entry) 
        except ValueError:
            distincts.append(entry)
            
    return distincts

if __name__ == '__main__':
    if len(sys.argv) > 1:
        distincts = []
        for filename in sys.argv[1:]:
            fd = open(filename, 'r')
            distincts = get_distincts([line.strip() for line in fd], distincts)
    else:
        distincts = get_distincts([line.strip() for line in sys.stdin])
    
    for line in distincts:    
        print line
        