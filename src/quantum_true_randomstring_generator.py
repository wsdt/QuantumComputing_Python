# (c) Riedl A. Kevin, 2019
# https://github.com/wsdt
# https://www.linkedin.com/in/kevin-riedl-947219158

import math, argparse, warnings
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute

MAX_QUBITS = 5


def get_register_sizes(n, max_qubits):
    register_sizes = [max_qubits for i in range(int(n/max_qubits))]
    remainder = n % max_qubits
    return register_sizes if remainder == 0 else register_sizes+[remainder]


def num_bits(n):
    return math.floor(math.log(n, 2))+1


def bit_from_counts(counts):
    return [k for k, v in counts.items() if v == 1][0]


def random_int(max, remote=False):
    bits = ''
    n_bits = num_bits(max-1)
    register_sizes = get_register_sizes(n_bits, MAX_QUBITS)
    backend = "ibmqx4" if remote else "local_qasm_simulator"

    for x in register_sizes:
        q = QuantumRegister(x)
        c = ClassicalRegister(x)
        qc = QuantumCircuit(q, c)

        qc.h(q)
        qc.measure(q, c)

        job_sim = execute(qc, backend, shots=1)
        sim_result = job_sim.result()
        counts = sim_result.get_counts(qc)

        bits += bit_from_counts(counts)
    return int(bits, 2)


result = random_int(15, False)
print(result)
