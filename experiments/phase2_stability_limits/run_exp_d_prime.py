"""
SRFM Experiment Runner (Phase 2)
--------------------------------
This script loads the external QASM 2.0 file and executes it using Qiskit.
It serves as the standard procedure to reproduce the experimental results.

Usage:
    python run_exp_d_prime.py
"""

import json
import os
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit_ibm_runtime import QiskitRuntimeService

# --- CONFIGURATION ---
# 読み込むQASMファイル名（博士が修正したファイルを指定）
QASM_FILE = "exp_d_prime_y_shape.qasm"

# 実機で動かす場合は True にする（APIトークン設定済み前提）
USE_REAL_HARDWARE = False
BACKEND_NAME = "ibm_marrakesh"
SHOTS = 1024

def main():
    # 1. QASMファイルの読み込み
    if not os.path.exists(QASM_FILE):
        print(f"Error: File '{QASM_FILE}' not found.")
        return

    print(f"Loading circuit from {QASM_FILE}...")
    qc = QuantumCircuit.from_qasm_file(QASM_FILE)
    print("Circuit loaded successfully.")
    
    # 回路図の簡易表示（確認用）
    print("\n--- Circuit Structure ---")
    print(qc.draw(output='text'))

    # 2. バックエンドの選択
    if USE_REAL_HARDWARE:
        print(f"\nConnecting to IBM Quantum Service...")
        service = QiskitRuntimeService()
        backend = service.backend(BACKEND_NAME)
        print(f"Running on Real Hardware: {BACKEND_NAME}")
    else:
        print(f"\nUsing Local Simulator (Aer)...")
        backend = AerSimulator()

    # 3. トランスパイル & 実行
    # optimization_level=0: 博士の意図したゲート構造を壊さないように最適化をオフにする
    t_qc = transpile(qc, backend, optimization_level=0)
    
    print(f"Executing job (Shots: {SHOTS})...")
    job = backend.run(t_qc, shots=SHOTS)
    
    # 4. 結果の取得と表示
    result = job.result()
    counts = result.get_counts()
    
    print("\n--- Experiment Results ---")
    print(counts)

    # 5. JSONデータとして保存（再現性のため）
    output_filename = f"result_{QASM_FILE.replace('.qasm', '.json')}"
    with open(output_filename, "w") as f:
        json.dump(counts, f, indent=4)
    print(f"\nResults saved to '{output_filename}'")

if __name__ == "__main__":
    main()