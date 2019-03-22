# (c) Riedl A. Kevin, 2019
# https://github.com/wsdt
# https://www.linkedin.com/in/kevin-riedl-947219158

# Inspired by
# https://medium.com/rigetti/how-to-write-a-quantum-program-in-10-lines-of-code-for-beginners-540224ac6b45

from pyquil.quil import Program
from pyquil.gates import H
from functools import reduce
from conf.controllers.c_general_conf import get_quantum_machine

# Fetches quantum machine for current set setting (e.g. real quantum computer or vm)
qm = get_quantum_machine()

# Create dice with 5 qubits (H gate -> Hadamard gate = qubit in superposition [50/50]
dice = Program(H(0), H(1), H(2), H(3), H(4))

# Resolve superpositions of qubits to get a measurable result
roll_dice = dice.measure_all()

# Execute
result = qm.run(roll_dice)
print("Your gate values -> "+str(result))

# Print a readable result
dice_value = reduce(lambda x, y: 2*x + y, result[0], 0)+1
print("Quantum dice roll -> ", dice_value)
