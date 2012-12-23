import numpy as np
from .common import FakeFunc
from .cdist_func import Normalize
import inspect
def better_arg_spec(f):
    """
    
    :param f:
    """
    #built-in funccode
    try:
        return f.func_code.co_varnames[:f.func_code.co_argcount]
    except Exception as e:
        #print e
        pass
    #using __call__ funccode
    try:
        vnames = f.__call__.func_code.co_varnames
        return f.__call__.func_code.co_varnames[1:f.__call__.func_code.co_argcount]
    except Exception as e:
        #print e
        pass
    return inspect.getargspec(f)[0]

#decorators
#@normalized_function(xmin,xmax)
#def function_i_have_no_idea_how_to_normalize(x,y,z)
#   return complicated_function(x,y,z)
#
class normalized_function:
    """

    :param xmin:
    :param xmax:
    """

    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
    def __call__(self,f):
        return Normalize(f,(self.xmin,self.xmax))

class rename_parameters:
    """

    :param arg:
    """

    def __init__(self,*arg):
        self.arg = arg
    def __call__(self,f):
        return FakeFunc(f,self.arg)

def extended(f):
    """

    :param f:
    :return:
    """
    return Extended(f)

#useful for highlight some xrange
def vertical_highlight(x1,x2=None,color='g',alpha=0.3,ax=None):
    """

    :param x1:
    :param x2:
    :param color:
    :param alpha:
    :param ax:
    """
    from matplotlib import pyplot as plt
    if(ax is None): ax=plt.gca()
    if x2 is None:
        x1,x2=x1
    ylim = plt.gca().get_ylim()
    y = np.array(ylim)
    ax.fill_betweenx(y,np.array(x1,x1),np.array(x2,x2),color=color,alpha=alpha)
    ax.set_ylim(ylim) #sometime it will decide to resize the plot

def describe(f):
    """

    :param f:
    :return:
    """
    return better_arg_spec(f)
    #return f.func_code.co_varnames[:f.func_code.co_argcount]

def parse_arg(f,kwd,offset=0):
    """

    :param f:
    :param kwd:
    """
    vnames = describe(f)
    return tuple([kwd[k] for k in vnames[offset:]])