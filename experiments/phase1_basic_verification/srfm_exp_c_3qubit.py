"""
SRFM Experiment C: Scalability Test (Actual Hardware Implementation)
--------------------------------------------------------------------
Author: Yoichi
License: CC BY-NC 4.0
Description:
    This script executes the exact quantum circuit used in the IBM Quantum 
    experiments. It uses explicitly decomposed gates for maximum compatibility.
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
# ⚡ RAW EXPERIMENT CODE (OpenQASM 2.0)
# ==========================================
# Validated OpenQASM 2.0 code with manual gate decomposition
qasm_string = """
OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

// --- Initialization ---
rz(pi/2) q[0]; sx q[0]; rz(pi/2) q[0];
rz(-pi/2) q[1]; rx(pi/2) q[1]; rz(pi/2) q[1];

// --- Interaction Block 1 ---
cx q[1], q[0]; rz(pi/4) q[0]; cx q[1], q[0]; // rzz
rz(pi/4) q[0]; rx(pi) q[0];
rz(pi/4) q[1]; rx(pi/2) q[1]; rz(-pi/2) q[1];

// --- Interaction Block 2 ---
rz(pi/2) q[2]; sx q[2]; rz(pi/2) q[2];
cz q[2], q[1];
rz(pi/2) q[1]; rx(-pi/2) q[1];

cx q[1], q[0]; rz(pi/4) q[0]; cx q[1], q[0]; // rzz
rz(pi/4) q[0]; rx(-pi/2) q[0];
rz(pi/4) q[1]; rx(pi/2) q[1]; rz(-pi/2) q[1];

cz q[2], q[1];
rx(2*pi/5) q[1];

// --- Mixing Layer ---
cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0];

x q[2];
cx q[2], q[1]; rz(pi/4) q[1]; cx q[2], q[1]; // rzz

// --- Parameter Tuning (SRFM Specific) ---
rz(-1.0995574287564285) q[1];
rx(pi/2) q[1]; rz(pi/2) q[1];

cx q[0], q[1]; rz(pi/4) q[1]; cx q[0], q[1]; // rzz
rz(-pi/4) q[0]; rx(pi/2) q[0]; rz(-pi/2) q[0];
rz(pi/4) q[1]; rx(-pi/2) q[1];

cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0];

rz(-2.0420352248333655) q[2];
rx(pi/2) q[2]; rz(-pi/2) q[2];

cz q[2], q[1];
rz(pi/2) q[1]; rx(-pi/2) q[1];

cx q[1], q[0]; rz(pi/4) q[0]; cx q[1], q[0]; // rzz
rz(pi/4) q[0]; rx(-pi/2) q[0];
rz(pi/4) q[1]; rx(pi/2) q[1]; rz(-pi/2) q[1];

cz q[2], q[1];
rz(0.9*pi) q[1]; // Intentional Shift (SRFM Core)
rx(pi/2) q[1];

cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0]; sx q[0]; sx q[1];
cz q[1], q[0];

x q[2];
cx q[2], q[1]; rz(pi/4) q[1]; cx q[2], q[1]; // rzz

// --- Final Rotations ---
rz(3*pi/4) q[1]; rx(pi/2) q[1]; rz(-3*pi/5) q[1];
rz(pi/4) q[2]; rx(pi/2) q[2]; rz(2*pi/5) q[2];

// --- Measurement ---
measure q[2] -> c[0];
measure q[0] -> c[1];
measure q[1] -> c[2];
"""

def run_experiment_c():
    print("--- SRFM Experiment C (Actual Hardware Code) ---")
    
    # QASM文字列から回路を生成
    circuit = QuantumCircuit.from_qasm_str(qasm_string)

    if USE_REAL_HARDWARE:
        from qiskit_ibm_runtime import QiskitRuntimeService
        try:
            service = QiskitRuntimeService()
            backend = service.backend(BACKEND_NAME)
            print(f"Connected to {BACKEND_NAME}")
        except:
            backend = AerSimulator()
            print("Fallback to Simulator")
    else:
        backend = AerSimulator()
        print("Running on Simulator...")

    job = backend.run(transpile(circuit, backend), shots=SHOTS)
    result = job.result()
    counts = result.get_counts()
    
    print("\nResult Counts (Raw Data):")
    print(counts)
    
    plot_histogram(counts, title="Experiment C: Scalability").savefig("Fig3_Scalability.png")
    print("Graph saved as 'Fig3_Scalability.png'")

if __name__ == "__main__":
    run_experiment_c()