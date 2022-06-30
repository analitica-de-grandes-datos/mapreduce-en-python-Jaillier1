#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import itertools 

if __name__ == '__main__':
    curkey=None
    total=0

    for line in sys.stdin:
        key, val = line.split("\n")
        val = int(val)


    sys.stdout.write("{}\t{}\n".format(key,sorted( value)))
