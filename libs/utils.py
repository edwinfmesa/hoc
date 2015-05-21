from settings import *

def print_state(p, cont, function_name):
    guiones = (20-len(str(cont)+str(function_name)))*'-'
    if PRINT_STATES:
        try:
            a = ' TYPE: ' + p.type
        except:
            try:
                a = ' : ' + ' '.join((x.__class__.__name__ if (x.__class__.__name__ !='str' and x.__class__.__name__ != 'float') else str(x)) for x in p[1:]) 
            except:
                a = ' ERROR: '
                print "ERROR", p
        print " "+str(cont)+(2-len(str(cont)))*" "+" . "+str(function_name)+guiones+a
    return 