from conf import USE_REAL_QCOMP, QISKIT_IBM_TOKEN


def get_quantum_machine():
    if USE_REAL_QCOMP:
        from qiskit import IBMQ
        IBMQ.enable_account(QISKIT_IBM_TOKEN)
        qm = IBMQ.backend(name="ibmqx5")[0]
    else:
        from qiskit import BasicAer
        qm = BasicAer.get_backend("qasm_simulator")
    return qm
