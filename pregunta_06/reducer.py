#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#


import  sys 

import itertools 

if __name__ == '__main__':

    curkey = None
    maximo = 0
    minimo = 0

    for line in sys.stdin:

        key, val = line.split("\t") 
        val = float(val)
        if key == curkey:

            if (val> maximo):
                maximo=val
            if (val< minimo):
                minimo=val  
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo))

            curkey = key
            maximo = val
            minimo = val
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, maximo, minimo)) 
