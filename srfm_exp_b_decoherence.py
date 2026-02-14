"""
SRFM Experiment B: Decoherence & Idle Noise Resilience
Author: Yoichi
License: CC BY-NC 4.0 (Non-Commercial Use Only)

Target Backend: IBM Quantum 'ibm_marrakesh' (Recommended)
Description:
    Tests the protocol's stability against idle noise (decoherence) and 
    phase drift by inserting barriers and off-target rotations (9*pi/10).
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
# ⚡ EXPERIMENT B: DECOHERENCE TEST
# ==========================================
qasm_string = """
OPENQASM 3.0;
include "stdgates.inc";
bit[4] c;

// Initialization
rz(pi/2) $0;
sx $0;
rz(pi/2) $0;

rz(pi/2) $1;
sx $1;
rz(pi/2) $1;

// Entanglement
cz $0, $1;

// --- Noise Injection Phase ---
// Intentional drift and idle time simulation
rz(-3*pi/5) $0;
rx(pi/2) $0;
rz(pi/2) $0;

barrier $0; // Force idle time
barrier $0;

rz(9*pi/10) $1; // Phase drift error
barrier $1; // Force idle time
barrier $1;

// Recovery Phase
rz(pi/2) $1;
sx $1;
rz(pi/2) $1;

cz $0, $1;

// Final Adjustment
rz(pi/2) $0;
rx(pi/2) $0;
rz(-3*pi/5) $0;

rz(pi/2) $1;
rx(pi/2) $1;
rz(-3*pi/5) $1;

// Measurement
c[0] = measure $0;
c[1] = measure $1;
"""

def run_experiment():
    print(f"Loading SRFM Experiment B (Decoherence)...")
    try:
        circuit = qiskit.qasm3.loads(qasm_string)
    except Exception as e:
        print(f"Error loading QASM: {e}")
        return

    # バックエンド選択ロジック
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

    # 実行
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=SHOTS)
    result = job.result()
    print("\n=== Experiment B Results ===")
    print(result.get_counts())

if __name__ == "__main__":
    run_experiment()
