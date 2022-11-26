### DESCRIPTION:

A quantum circuit simulator can be very useful to test out your code as a proof of concept, or even if you want to debug it before you run it on an actual quantum computer. A quantum circuit uses qubits instead of bits. The advantage of quantum computing is the ability to send a message that contains 2 bits of data with just one qubit. This is possible because of entanglement. When you measure the state of one entangled particle, you know the state of the other one without even measuring it. So you just need to send one qubit and not both.

This is an attempt to create a basic quantum simulator to simulate some aspects of what an ideal quantum computer does. The quantum simulator can perform the following tasks-

1]Initialize a quantum system to the default state, i.e. the |0> state. Its is implemented by just storing it as a state vector.

2]Evolve: Applies an operator to the circuit. Here the operator is basically different quantum gates.

3]Measure: Measures the state of a given quantum circuit and uses wighted random choice to simulate what you would get with an ideal quantum computer.

### MODULES IMPLEMENTED:

  1]numpy
  
  2]math
  
  3]random
  
  4]matplotlib

### INSTRUCTIONS:
`from Quantumcircuit import circuit,gate,measure`
imports the required files from Quantumcircuit.

`circuit.quantumcircuit(n)`
Creates a n quantum circuits. `n` is any integer greater than 0

`gate.x(circuit)`
Performs a x-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.y(circuit)`
Performs a y-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.z(circuit)`
Performs a z-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.h(circuit)`
Performs a h-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.p(circuit)`
Performs a p-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.t(circuit)`
Performs a t-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.cnot(circuit,target)`
Performs a cnot-gate operation on a required circuit. Here `circuit` represents the circuit number.

`gate.cz(circuit,target)`
Performs a cz-gate operation on a required circuit. Here `circuit` represents the control circuit number and `target` represents the target circuit number.

`gate.s(circuit,target)`
Performs a swap-gate operation on a required circuit. Here `circuit` represents the circuit number and `target` represents the target circuit number.

`gate.ccnot(c1,c2,target)`
Performs a ccnot-gate operation on a required circuit. Here `c1` and `c2` represents the control circuit number and `target` represents the target circuit number.

`measure.measure(circuit)`
Measures the state of a particular circuit.

### SAMPLE PROGRAM
```#import the required modules
from Quantumcircuit import circuit,gate,measure

#create 5 quantum circuits
circuit.quantumcircuit(5)

#perform x gate operation on 0th qubit
gate.x(0)

#perform cnot operation on 0th and 1st qubits
gate.cnot(0,1)

#perform ccnot operation on 2nd, 3rd and 4th qubits
gate.ccnot(2,3,4)

#measure the value of 0th qubit
measure.measure(0)
```

### sample output
![image](https://user-images.githubusercontent.com/119108677/204089779-9cfb7d31-45be-463d-874b-7642b544eda7.png)
