"""
Execution Script for SRFM Experiment E (Temporal Stability)
-----------------------------------------------------------
Loads 'exp_e_time_stability.qasm' and executes it.
Crucially uses optimization_level=0 to preserve the specific gate sequence
and barriers, preventing the compiler from simplifying the noise injection steps.
"""

import json
import os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

# --- CONFIGURATION ---
QASM_FILE = "exp_e_time_stability.qasm"
BACKEND_NAME = "ibm_marrakesh"  # Target Hardware
USE_REAL_HARDWARE = False       # Set True for real execution
SHOTS = 1024

def main():
    # 1. Load QASM
    if not os.path.exists(QASM_FILE):
        print(f"Error: {QASM_FILE} not found.")
        return

    print(f"Loading circuit from {QASM_FILE}...")
    qc = QuantumCircuit.from_qasm_file(QASM_FILE)
    
    # Show circuit depth (Should be 5 cycles deep)
    print(f"Circuit loaded. Depth: {qc.depth()}")

    # 2. Setup Backend
    if USE_REAL_HARDWARE:
        service = QiskitRuntimeService()
        backend = service.backend(BACKEND_NAME)
        print(f"Running on Real Hardware: {BACKEND_NAME}")
    else:
        backend = AerSimulator()
        print("Running on Simulator (Aer)")

    # 3. Transpile & Run
    # IMPORTANT: optimization_level=0 is required!
    # We explicitly want to execute the redundant gates for noise simulation.
    t_qc = transpile(qc, backend, optimization_level=0)
    
    print(f"Submitting job (Shots: {SHOTS})...")
    job = backend.run(t_qc, shots=SHOTS)
    
    result = job.result()
    counts = result.get_counts()
    
    print("\n--- Result Counts ---")
    print(counts)

    # 4. Save Data
    output_filename = f"result_{QASM_FILE.replace('.qasm', '.json')}"
    with open(output_filename, "w") as f:
        json.dump(counts, f, indent=4)
    print(f"Data saved to {output_filename}")

if __name__ == "__main__":
    main()