"""
SRFM: Self-Regulating Field Model Protocol (Core Logic)
Author: Yoichi
License: CC BY-NC 4.0 (Non-Commercial Use Only)

Target Backend: IBM Quantum 'ibm_marrakesh' (Recommended)
Description:
    This script defines the core SRFM quantum circuit using OpenQASM 3.0
    to ensure precise gate rotation angles (intentional imperfections).
"""

import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# ==========================================
# ⚙️ CONFIGURATION (設定)
# ==========================================
# True: IBM Quantum実機を使用 (要APIトークン)
# False: ローカルシミュレーターを使用 (誰でも実行可能)
USE_REAL_HARDWARE = False 

# 実機を使う場合の設定 (自分の環境に合わせて書き換えてください)
BACKEND_NAME = "ibm_marrakesh" 
SHOTS = 4000

# ==========================================
# ⚡ SRFM CORE CIRCUIT (OpenQASM 3.0)
# ==========================================
qasm_string = """
OPENQASM 3.0;
include "stdgates.inc";
bit[4] c;

// Qubit 0 Initialization (Superposition / Hadamard-like)
rz(pi/2) $0;
sx $0;
rz(pi/2) $0;

// Qubit 1 Initialization
rz(pi/2) $1;
sx $1;
rz(pi/2) $1;

// --- Entanglement & Intentional Noise Injection ---
cz $0, $1;

// SRFM Rotation Layer 1 (Specific Phase: -3*pi/5)
rz(-3*pi/5) $0;
rx(pi/2) $0;
rz(pi/2) $0;

rz(-3*pi/5) $1;
rx(pi/2) $1;
rz(pi/2) $1;

// --- Entanglement Layer 2 ---
cz $0, $1;

// SRFM Rotation Layer 2
rz(pi/2) $0;
rx(pi/2) $0;
rz(-3*pi/5) $0;

rz(pi/2) $1;
rx(pi/2) $1;
rz(-3*pi/5) $1;

// --- Measurement ---
c[0] = measure $0;
c[1] = measure $1;
"""

def run_experiment():
    print(f"Loading SRFM Circuit from OpenQASM 3.0...")
    try:
        circuit = qiskit.qasm3.loads(qasm_string)
    except Exception as e:
        print(f"Error loading QASM: {e}")
        return

    print("Circuit created successfully.")
    # print(circuit.draw()) # 回路図を見たい場合はコメントアウトを外す

    # バックエンドの選択
    if USE_REAL_HARDWARE:
        from qiskit_ibm_runtime import QiskitRuntimeService
        try:
            # QiskitRuntimeService.save_account(token="YOUR_TOKEN") # 初回のみ必要
            service = QiskitRuntimeService()
            backend = service.backend(BACKEND_NAME)
            print(f"Running on Real Device: {BACKEND_NAME}")
        except Exception as e:
            print(f"Failed to connect to IBM Quantum: {e}")
            print("Falling back to local simulator...")
            backend = AerSimulator()
    else:
        backend = AerSimulator()
        print("Running on Local Simulator (Aer)...")

    # トランスパイルと実行
    transpiled_circuit = transpile(circuit, backend)
    job = backend.run(transpiled_circuit, shots=SHOTS)
    
    print("Job submitted. Waiting for results...")
    result = job.result()
    counts = result.get_counts()

    print("\n=== SRFM Experiment Results ===")
    print(counts)
    
    # グラフの保存 (オプション)
    # plot_histogram(counts, title="SRFM Convergence Result").savefig("srfm_result.png")
    # print("Histogram saved as 'srfm_result.png'")

if __name__ == "__main__":
    run_experiment()
