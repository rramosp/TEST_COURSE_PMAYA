import numpy as np
import pandas as pd
grader_function_name = 'grader_02'


def grader_02(functions, variables, caller_userid):
    import numpy as np
        
    print ("---", functions)
        
    # retrieve definitions
    namespace = locals()
    for f in functions.values():
        exec(f, namespace)

    st_mean_funct = namespace['list_mean']
    st_stdev_funct = namespace['list_stdev']
    
    error = False
    msg = 'testing your code with 1000 use cases'
    
    for i in range(100):
        size = np.random.randint(20)+3
        list = np.random.randint(10, size=size)
        mean = np.mean(list)
        stdev = np.std(list)
        if not (mean==st_mean_funct(list)):
            msg += "input\nlist = \n%s\n"%(str(list))
            msg += "expected output:%s\n"%str(mean)
            msg += "output obtained:%s\n"%str(st_mean_funct(list))
            error = True
            break
        if not (stdev==st_stdev_funct(list)):
            msg += "input\nlist = \n%s\n"%(str(list))
            msg += "expected output:%s\n"%str(stdev)
            msg += "output obtained:%s\n"%str(st_stdev_funct(list))
            error = True
            break
    
    if not error:
        msg += u'<b>CORRECT</b>'
        return 5, '<b>correct</b>'
    else:
        msg += u'<b><font color="red">INCORRECT</font></b>'
        return 0, msg

