"""
SRFM: Self-Regulating Field Model Protocol (Core Implementation)
----------------------------------------------------------------
Author: Yoichi (Independent Researcher)
Date:   February 2026
License: CC BY-NC 4.0 (Attribution-NonCommercial 4.0 International)
         * Commercial use is strictly prohibited without permission.

Target Hardware: IBM Quantum 'ibm_marrakesh' (156-qubit Heron Processor)
Description:
    This script implements the SRFM algorithm using OpenQASM 3.0 to define
    precise gate rotation angles. It demonstrates the formation of a stable
    eigenspace (attractor) under intentional gate imperfections.
"""

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

# ==========================================
# ⚙️ CONFIGURATION
# ==========================================
# True: Use IBM Quantum Real Hardware (Requires API Token & Account)
# False: Use Local Simulator (Aer) - Accessible to everyone
USE_REAL_HARDWARE = False 

# Configuration for Real Hardware
BACKEND_NAME = "ibm_marrakesh" 
SHOTS = 1024  # Standardized to match the paper/README

# ==========================================
# ⚡ SRFM CORE CIRCUIT (OpenQASM 3.0)
# ==========================================
# Note: Specific rotation angles (e.g., -3*pi/5) and under-rotations
# are intentional to induce the self-regulating dynamic.
qasm_string = """
OPENQASM 3.0;
include "stdgates.inc";
bit[2] c;

// --- Initialization (Superposition) ---
rz(pi/2) $0; sx $0; rz(pi/2) $0;
rz(pi/2) $1; sx $1; rz(pi/2) $1;

// --- Entanglement & Intentional Noise Injection ---
cz $0, $1;

// Layer 1: SRFM Phase Injection (-3*pi/5)
rz(-3*pi/5) $0; rx(pi/2) $0; rz(pi/2) $0;
rz(-3*pi/5) $1; rx(pi/2) $1; rz(pi/2) $1;

// Layer 2: Re-Entanglement
cz $0, $1;

// Layer 3: Stabilization
rz(pi/2) $0; rx(pi/2) $0; rz(-3*pi/5) $0;
rz(pi/2) $1; rx(pi/2) $1; rz(-3*pi/5) $1;

// --- Measurement ---
c[0] = measure $0;
c[1] = measure $1;
"""

def run_experiment():
    print(f"--- SRFM Protocol Execution Started ---")
    print(f"Loading Circuit from OpenQASM 3.0...")
    
    try:
        circuit = qiskit.qasm3.loads(qasm_string)
    except Exception as e:
        print(f"Error loading QASM: {e}")
        return

    print("Circuit created successfully.")

    # Backend Selection Logic
    if USE_REAL_HARDWARE:
        print(f"Attempting to connect to IBM Quantum Real Hardware ({BACKEND_NAME})...")
        from qiskit_ibm_runtime import QiskitRuntimeService
        try:
            # Note: User must have saved their account using QiskitRuntimeService.save_account()
            service = QiskitRuntimeService()
            backend = service.backend(BACKEND_NAME)
            print(f"SUCCESS: Connected to {BACKEND_NAME}")
        except Exception as e:
            print(f"WARNING: Failed to connect to IBM Quantum: {e}")
            print("Falling back to local simulator (Aer)...")
            backend = AerSimulator()
    else:
        backend = AerSimulator()
        print("Mode: Local Simulator (Aer)")

    # Execution
    print(f"Transpiling and Running (Shots: {SHOTS})...")
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=SHOTS)
    
    if USE_REAL_HARDWARE:
        print(f"Job ID: {job.job_id()}")
        print("Waiting for results from cloud...")
    
    result = job.result()
    counts = result.get_counts()

    # Display Results
    print("\n=== SRFM Experiment Results ===")
    print(f"Raw Counts: {counts}")
    
    # Identify Dominant State
    most_frequent = max(counts, key=counts.get)
    probability = counts[most_frequent] / SHOTS * 100
    print(f"Dominant State: |{most_frequent}> ({probability:.2f}%)")

    # Save Histogram
    output_filename = "srfm_result_histogram.png"
    fig = plot_histogram(counts, title=f"SRFM Result (Shots={SHOTS})")
    fig.savefig(output_filename)
    print(f"\nHistogram saved as '{output_filename}'")
    print("--- Execution Complete ---")

if __name__ == "__main__":
    run_experiment()