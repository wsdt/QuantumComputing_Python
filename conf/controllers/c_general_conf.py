from conf import USE_REAL_QCOMP


def get_quantum_machine():
    if USE_REAL_QCOMP:
        from pyquil.api import QVMConnection
        qm = QVMConnection()
    else:
        from pyquil.api import QPUConnection
        # Agave 8-qubit chip should be live and freely available
        qm = QPUConnection('8Q-Agave')
    return qm
