"""
SRFM Experiment C: 3-Qubit Scalability & Subspace Convergence
Author: Yoichi
License: CC BY-NC 4.0 (Non-Commercial Use Only)

Target Backend: IBM Quantum 'ibm_marrakesh' (Recommended)
Description:
    Demonstrates the scalability of SRFM on a 3-qubit system.
    The circuit utilizes custom Rzz interactions and specific non-Clifford 
    rotations (e.g., -1.099...) to guide the state into a stable eigenspace 
    (Attractor basin) despite the increased Hilbert space dimension.
"""

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
USE_REAL_HARDWARE = False 
BACKEND_NAME = "ibm_marrakesh" 
SHOTS = 4000

# ==========================================
# ⚡ EXPERIMENT C: 3-QUBIT SCALABILITY
# ==========================================
qasm_string = """
OPENQASM 3.0;
include "stdgates.inc";

// Custom Rzz Gate Definition for SRFM interaction
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}

bit[3] c;

// --- Layer 1: Initialization & Superposition ---
rz(pi/2) $0;
sx $0;
rz(pi/2) $0;

rz(-pi/2) $1;
rx(pi/2) $1;
rz(pi/2) $1;

// --- Layer 2: Interaction Block A (Q1-Q0) ---
rzz(pi/4) $1, $0;
rz(pi/4) $0;
rx(pi) $0;
rz(pi/4) $1;
rx(pi/2) $1;
rz(-pi/2) $1;

// --- Layer 3: Interaction Block B (Q2-Q1) ---
rz(pi/2) $2;
sx $2;
rz(pi/2) $2;
cz $2, $1;

rz(pi/2) $1;
rx(-pi/2) $1;
rzz(pi/4) $1, $0;
rz(pi/4) $0;
rx(-pi/2) $0;

rz(pi/4) $1;
rx(pi/2) $1;
rz(-pi/2) $1;

cz $2, $1;
rx(2*pi/5) $1; // SRFM Specific Phase

// --- Layer 4: Dense Entanglement (Swapping/Mixing) ---
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;

x $2;
rzz(pi/4) $2, $1;

// --- Layer 5: Fine-tuned SRFM Parameters ---
rz(-1.0995574287564285) $1; // Precise tuning
rx(pi/2) $1;
rz(pi/2) $1;

rzz(pi/4) $0, $1;
rz(-pi/4) $0;
rx(pi/2) $0;
rz(-pi/2) $0;

rz(pi/4) $1;
rx(-pi/2) $1;

// Mixing Block
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;

// --- Layer 6: Final Stabilization ---
rz(-2.0420352248333655) $2; // Precise tuning
rx(pi/2) $2;
rz(-pi/2) $2;

cz $2, $1;
rz(pi/2) $1;
rx(-pi/2) $1;
rzz(pi/4) $1, $0;

rz(pi/4) $0;
rx(-pi/2) $0;
rz(pi/4) $1;
rx(pi/2) $1;
rz(-pi/2) $1;

cz $2, $1;
rz(9*pi/10) $1; // Intentional Offset
rx(pi/2) $1;

// Final Mixing
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;
sx $0;
sx $1;
cz $1, $0;

x $2;
rzz(pi/4) $2, $1;

// Final Rotations
rz(3*pi/4) $1;
rx(pi/2) $1;
rz(-3*pi/5) $1;

rz(pi/4) $2;
rx(pi/2) $2;
rz(2*pi/5) $2;

// --- Measurement (Specific Mapping) ---
c[0] = measure $2;
c[1] = measure $0;
c[2] = measure $1;
"""

def run_experiment():
    print(f"Loading SRFM Experiment C (3-Qubit)...")
    try:
        circuit = qiskit.qasm3.loads(qasm_string)
    except Exception as e:
        print(f"Error loading QASM: {e}")
        return

    if USE_REAL_HARDWARE:
        from qiskit_ibm_runtime import QiskitRuntimeService
        try:
            service = QiskitRuntimeService()
            backend = service.backend(BACKEND_NAME)
            print(f"Running on Real Device: {BACKEND_NAME}")
        except Exception:
            backend = AerSimulator()
            print("Fallback to Simulator.")
    else:
        backend = AerSimulator()
        print("Running on Local Simulator (Aer)...")

    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=SHOTS)
    result = job.result()
    print("\n=== Experiment C Results ===")
    print(result.get_counts())

if __name__ == "__main__":
    run_experiment()
