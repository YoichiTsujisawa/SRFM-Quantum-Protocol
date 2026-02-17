"""
SRFM Experiment B: Decoherence Resilience Test
----------------------------------------------
Author: Yoichi
License: CC BY-NC 4.0
Description:
    Tests the stability of the SRFM attractor against decoherence (T1/T2 relaxation)
    by inserting idle time (Identity gates) into the circuit.
"""

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
USE_REAL_HARDWARE = False 
BACKEND_NAME = "ibm_marrakesh" 
SHOTS = 1024

# ==========================================
# ⚡ EXPERIMENT B CIRCUIT (OpenQASM 2.0)
# ==========================================
# Inserts 'id' (identity) gates to simulate idle noise
qasm_string = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// --- Initialization ---
rz(pi/2) q[0]; sx q[0]; rz(pi/2) q[0];
rz(pi/2) q[1]; sx q[1]; rz(pi/2) q[1];

// --- Entanglement ---
cz q[0], q[1];

// --- SRFM Layer 1 ---
rz(-3*pi/5) q[0]; rx(pi/2) q[0]; rz(pi/2) q[0];
rz(-3*pi/5) q[1]; rx(pi/2) q[1]; rz(pi/2) q[1];

// === DECOHERENCE CHALLENGE ===
// Inserting idle gates to induce relaxation noise
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1]; 
// ==============================

// --- Re-Entanglement ---
cz q[0], q[1];

// --- SRFM Stabilization ---
rz(pi/2) q[0]; rx(pi/2) q[0]; rz(-3*pi/5) q[0];
rz(pi/2) q[1]; rx(pi/2) q[1]; rz(-3*pi/5) q[1];

// --- Measurement ---
measure q[0] -> c[0];
measure q[1] -> c[1];
"""

def run_experiment_b():
    print("--- SRFM Experiment B (Decoherence Test) ---")
    circuit = QuantumCircuit.from_qasm_str(qasm_string)

    if USE_REAL_HARDWARE:
        from qiskit_ibm_runtime import QiskitRuntimeService
        try:
            service = QiskitRuntimeService()
            backend = service.backend(BACKEND_NAME)
        except:
            backend = AerSimulator()
    else:
        backend = AerSimulator()

    job = backend.run(transpile(circuit, backend), shots=SHOTS)
    result = job.result()
    counts = result.get_counts()
    
    print("\nResult Counts:")
    print(counts)
    plot_histogram(counts, title="Experiment B: Decoherence").savefig("Fig2_Decoherence.png")

if __name__ == "__main__":
    run_experiment_b()