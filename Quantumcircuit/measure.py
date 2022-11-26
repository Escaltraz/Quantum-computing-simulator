#importing required modules
from Quantumcircuit import circuit as q
import random,numpy
import matplotlib.pyplot as bar

def measure(circuit):
    '''
    measures the state of a particular qubit

    Parameters
    ----------
    circuit : integer
        describes the circuit number.

    Returns
    -------
    None.

    '''
    
    #getting the required statevector
    p=q.qc.get(circuit)
    
    #condition to check entangled states
    if len(p)==2:
        #creating a list of vector representations
        l=['|0>','|1>']
        
        #creating a list of weighted random distributions based on probability to simulate a quantum computer
        rl=random.choices(l,weights=((p[0,0])**2,(p[1,0])**2),k=1024)
        
        #calculating the probability
        v=[rl.count(l[0])/1024,rl.count(l[1])/1024]
        
        #creating a bar graph based on the probability
        bar.bar(l,v,color='blue',width=0.3)
        bar.ylabel('probability amplitude')
        bar.xlabel('qubit state')
        bar.show()
        
        #update the collapsed state of the qubit
        q.qc.update({circuit:numpy.matrix('1 ; 0')})

    elif len(p)==4:
        #creating a list of vector representations
        l=['|00>','|01>','|10>','|11>']
        
        #creating a list of weighted random distributions based on probability to simulate a quantum computer
        rl=random.choices(l,weights=((p[0,0])**2,(p[1,0])**2,(p[2,0])**2,(p[3,0])**2),k=1024)
        
        #calculating the probability
        v=[rl.count(l[0])/1024,rl.count(l[1])/1024,rl.count(l[2])/1024,rl.count(l[3])/1024]
        
        #creating a bar graph based on the probability
        bar.bar(l,v,color='blue',width=0.5)
        bar.ylabel('probability')
        bar.xlabel('qubit state')
        bar.show()
        
        #update the collapsed state of the qubit
        q.qc.update({circuit:numpy.matrix('1 ; 0')})
        
    elif len(p)==8:
        #creating a list of vector representations
        l=['|000>','|001>','|010>','|011>','|100>','|101>','|110>','|111>']
        
        #creating a list of weighted random distributions based on probability to simulate a quantum computer
        rl=random.choices(l,weights=((p[0,0])**2,(p[1,0])**2,(p[2,0])**2,(p[3,0])**2,(p[4,0])**2,(p[5,0])**2,(p[6,0])**2,(p[7,0])**2),k=1024)
        
        #calculating the probability
        v=[rl.count(l[0])/1024,rl.count(l[1])/1024,rl.count(l[2])/1024,rl.count(l[3])/1024,rl.count(l[4])/1024,rl.count(l[5])/1024,rl.count(l[6])/1024,rl.count(l[7])/1024]
        
        #creating a bar graph based on the probability
        bar.bar(l,v,color='blue',width=0.5)
        bar.ylabel('probability')
        bar.xlabel('qubit state')
        bar.show()
        
        #update the collapsed state of the qubit
        q.qc.update({circuit:numpy.matrix('1 ; 0')})


