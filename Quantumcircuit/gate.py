#importing required modules
import numpy,math
from Quantumcircuit import circuit as q

#defining value of a
a=math.e**(1j*math.pi/4)

#defining the matrix values of some quantum gates
X=numpy.matrix('0 1 ; 1 0')
Y=numpy.matrix('0 -1j ; 1j 0')
Z=numpy.matrix('1 0 ; 0 -1')
H=numpy.matrix('1 1 ; 1 -1')
P=numpy.matrix('1 0 ; 0 1j')
T=numpy.matrix('1 0 ; 0 0.7071067811865476+0.7071067811865476j')
CNOT=numpy.matrix('1 0 0 0 ; 0 1 0 0 ; 0 0 0 1 ; 0 0 1 0')
CZ=numpy.matrix('1 0 0 0 ; 0 1 0 0 ; 0 0 1 0 ; 0 0 0 -1')
S=numpy.matrix('1 0 0 0 ; 0 0 1 0 ; 0 1 0 0 ; 0 0 0 1')
CCNOT=numpy.matrix('1 0 0 0 0 0 0 0 ; 0 1 0 0 0 0 0 0 ; 0 0 1 0 0 0 0 0 ; 0 0 0 1 0 0 0 0 ; 0 0 0 0 1 0 0 0 ; 0 0 0 0 0 1 0 0 ; 0 0 0 0 0 0 0 1 ; 0 0 0 0 0 0 1 0')

def x(circuit):
    '''
    applies operation x on a given circuit
    
    Parameters
    ----------
    circuit : integer 
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=X*q.qc.get(circuit)
    
    #update the statevector
    q.qc.update({circuit:r})
    
def y(circuit):
    '''
    applies operation y on a given circuit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=Y*q.qc.get(circuit)
    
    #update the statevector
    q.qc.update({circuit:r})
    
def z(circuit):
    '''
    applies operation z on a given circuit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=Z*q.qc.get(circuit)
    
    #update the statevector
    q.qc.update({circuit:r})
    
def h(circuit):
    '''
    applies operation h on a given circuit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=H*q.qc.get(circuit)
    
    #update the statevector
    q.qc.update({circuit:r})
    
def p(circuit):
    '''
    applies operation p on a given circuit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=P*q.qc.get(circuit)
    
    #update the state vector
    q.qc.update({circuit:r})
    
def t(circuit):
    '''
    applies operation t on a given circuit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    r=T*q.qc.get(circuit)
    
    #update the state vector
    q.qc.update({circuit:r})
    
def cnot(circuit,target):
    '''
    applies operation cnot with the control and target circuit

    Parameters
    ----------
    circuit : integer
        describes the control circuit.
    target : integer
        describes the target circuit.

    Returns
    -------
    None.

    '''
    
    tensor=numpy.kron(q.qc.get(circuit),q.qc.get(target))
    r=CNOT*tensor
    
    #update the combined state vector
    q.qc.update({circuit:r})
    q.qc.update({target:r})
    
def cz(circuit,target):
    '''
    applies operation cz with the control and target circuit

    Parameters
    ----------
    circuit : integer
        describes the control circuit.
    target : integer
        describes the target circuit.

    Returns
    -------
    None.

    '''
    
    tensor=numpy.kron(q.qc.get(circuit),q.qc.get(target))
    r=CZ*tensor
    
    #update the combined state vector
    q.qc.update({circuit:r})
    q.qc.update({target:r})
    
def s(circuit,target):
    '''
    applies operation s with the control and target circuit

    Parameters
    ----------
    circuit : integer
        describes the control circuit.
    target : integer
        describes the target circuit.

    Returns
    -------
    None.

    '''
    
    tensor=numpy.kron(q.qc.get(circuit),q.qc.get(target))
    r=S*tensor
    
    #update the combined state vector
    q.qc.update({circuit:r})
    q.qc.update({target:r})
    
def ccnot(c1,c2,target):
    '''
    applies operation ccnot

    Parameters
    ----------
    c1 : integer
        describes control circuit 1.
    c2 : integer
        describes control circuit 2.
    target : integer
        describes target circuit.

    Returns
    -------
    None.

    '''
    
    tensor=numpy.kron(q.qc.get(c1),q.qc.get(c2))
    tensor=numpy.kron(tensor,q.qc.get(target))
    r=CCNOT*tensor
    
    #update the combined state vector
    q.qc.update({c1:r})
    q.qc.update({c2:r})
    q.qc.update({target:r})
