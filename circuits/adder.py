from qiskit import QuantumCircuit

def add_two_qubits(q0: bool, q1: bool) -> QuantumCircuit:
    qc = QuantumCircuit(4, 2)
    if q0:
        qc.x(0)
    if q1:
        qc.x(1)
    # apply the controller-NOT gate controlled by q0 and targeting q2
    qc.cx(0, 2)
    # apply the controller-NOT gate controlled by q1 and targeting q2
    qc.cx(1, 2)
    # apply the Toffoli gate controlled by q0 and q1 and targeting q3
    qc.ccx(0, 1, 3)
    qc.measure([2, 3], [0, 1])
    return qc

