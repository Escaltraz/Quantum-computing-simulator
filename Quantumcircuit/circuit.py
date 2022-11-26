#importing required modules
import numpy

#creating a dictionary to save state-vector of a particular qubit
qc={}

def quantumcircuit(n):
    '''
    Parameters
    ----------
    n : accepts integer values
        describes the number of circuits to be initialized.

    Returns
    -------
    None.

    '''
    #loop to create n circuits
    for i in range(n):
        
        #initializing circuit with a default value
        qc.update({i:numpy.matrix('1 ; 0')})