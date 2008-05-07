import sys,os

if __name__ == '__main__':
        prev = ''

        if len(sys.argv) > 2:
                print "unique.py - from a sorted file, print only unique lines"
                print "\tusage: python unique.py [sorted_file]"
                print "\tor:    python unique.py < sorted_file"
                sys.exit(5)

        if len(sys.argv) == 2:
                fd = open(sys.argv[1], 'r')
        else:
                fd = sys.stdin

        while 1:
                line = fd.readline().strip()
                if line  == '': break

                if line != prev:
                        prev = line
                        print line