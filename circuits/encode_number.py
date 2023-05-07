from qiskit import QuantumCircuit

def encode_number(number: int) -> QuantumCircuit:
    # to remove the '0b' prefix and transform into little-endian notation
    bits = bin(number)[2:][::-1]
    # instantiate a circuit with len(bits) qubits and classical bits
    circuit = QuantumCircuit(len(bits), len(bits))
    # collect indices of 1s
    one_indices = [i for i, bit in enumerate(bits) if bit == '1']
    # apply X-gates to qubits under these indices
    circuit.x(one_indices)
    # measure qubits to the already existing classical bits
    circuit.measure_all(add_bits=False)
    # return the circuit
    return circuit

