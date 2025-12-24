import numpy as np

class QuantumProcessingUnit:
    def __init__(self, qubits=4):
        self.num_qubits = qubits
        self.dim = 2**qubits
        self.state = np.zeros(self.dim, dtype=complex)
        self.state[0] = 1.0 + 0j

    def apply_hadamard(self):
        """Applies Hadamard gate (Superposition) via Tensor Product"""
        H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
        full_op = H
        for _ in range(self.num_qubits - 1):
            full_op = np.kron(full_op, H)
        self.state = full_op @ self.state

    def apply_entanglement(self, complexity):
        """Simulates CNOT entanglement"""
        if complexity < 0.1: return
        interaction_strength = np.pi * complexity
        phase_matrix = np.exp(1j * interaction_strength * np.random.rand(self.dim))
        self.state = self.state * phase_matrix

    def collapse_wavefunction(self, complexity_level):
        """Superposition -> Entanglement -> Measurement"""
        self.state = np.zeros(self.dim, dtype=complex)
        self.state[0] = 1.0 + 0j
        
        self.apply_hadamard()
        self.apply_entanglement(complexity_level)
        
        probabilities = np.abs(self.state)**2
        probabilities /= np.sum(probabilities)
        
        indices = np.arange(self.dim)
        chosen_idx = np.random.choice(indices, p=probabilities)
        bitstring = format(chosen_idx, f'0{self.num_qubits}b')
        
        coherence = 1.0 - (complexity_level * 0.4)
        return coherence, bitstring
