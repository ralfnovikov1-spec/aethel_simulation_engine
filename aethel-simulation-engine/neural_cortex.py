import numpy as np

class NeuralCortex:
    def __init__(self, input_size=4, hidden_size=16):
        # Weights (No PyTorch needed!)
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros(hidden_size)
        self.W2 = np.random.randn(hidden_size, 1) * 0.1
        self.b2 = np.zeros(1)
        self.lr = 0.01

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        s = self.sigmoid(x)
        return s * (1 - s)

    def process_thought(self, quantum_data):
        # 1. Prepare Input
        x = np.array([float(b) for b in quantum_data]).reshape(1, -1)
        
        # 2. Forward Pass (Manual Math)
        z1 = np.dot(x, self.W1) + self.b1
        a1 = np.maximum(0, z1) # ReLU
        z2 = np.dot(a1, self.W2) + self.b2
        a2 = self.sigmoid(z2) # Output
        
        output = a2[0][0]
        
        # 3. Calculate Loss
        target = 1.0 if np.mean(x) > 0.5 else 0.0
        loss = (output - target) ** 2
        
        # 4. Backward Pass (Manual Backprop)
        d_output = 2 * (output - target)
        d_z2 = d_output * self.sigmoid_derivative(z2)
        d_W2 = np.dot(a1.T, d_z2)
        d_b2 = np.sum(d_z2, axis=0)
        d_a1 = np.dot(d_z2, self.W2.T)
        d_z1 = d_a1.copy()
        d_z1[z1 <= 0] = 0
        d_W1 = np.dot(x.T, d_z1)
        d_b1 = np.sum(d_z1, axis=0)
        
        # 5. Update Weights
        self.W1 -= self.lr * d_W1
        self.b1 -= self.lr * d_b1
        self.W2 -= self.lr * d_W2
        self.b2 -= self.lr * d_b2
        
        return output, loss
