# SRFM: Self-Regulating Field Model
### Robust Quantum Search & Stabilization Protocol for NISQ Devices

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

## Overview
**SRFM (Self-Regulating Field Model)** is a novel quantum search algorithm designed specifically for Noisy Intermediate-Scale Quantum (NISQ) devices. Unlike conventional Grover's algorithm, SRFM utilizes **intentional gate imperfections** and **dissipative dynamics** to stabilize the target quantum state without quantum error correction.

This protocol demonstrates that noise and decoherence can be harnessed to form a **stable eigenspace (attractor)**, achieving high-fidelity convergence even in imperfect hardware environments.

---

## Key Features
* **Noise Resilience:** Maintains >90% fidelity under significant gate errors (e.g., $Rx(0.9\pi)$).
* **Calibration-Free:** Operates robustly without precise pulse calibration.
* **Subspace Stabilization:** Convergence to a specific eigenspace (e.g., $|1*1\rangle$ in 3-qubit systems) rather than a single point, providing structural stability.

---

## Experimental Results (IBM Quantum)

### 1. Robustness against Gate Errors (2-Qubit)
Testing with intentional $10\%$ under-rotation ($Rx(0.9\pi)$) on IBM Quantum hardware.
* **Result:** The target state $|11\rangle$ achieved **>90% probability**, significantly outperforming standard amplitude amplification.

### 2. Resilience to Decoherence (Idle Noise)
Testing with inserted `Identity` gates and `Barriers` to induce relaxation.
* **Result:** The system self-corrected the phase drift, maintaining the target peak.

### 3. Scalability (3-Qubit Expansion)
Despite the increased circuit depth and connectivity overhead (SWAP/CNOT), the protocol successfully identified the target subspace.
* **Observation:** Convergence to $|111\rangle$ and $|101\rangle$ suggests the formation of a **Decoherence-Free Subspace (DFS)-like structure**, where $q_1$ acts as a buffer degree of freedom.

*(Please refer to the `/data` folder for raw Qiskit results and histograms.)*

---

## Theoretical Basis
Eigenvalue analysis of the SRFM unitary operator $U_{SRFM}$ reveals that the target states form a **quasi-invariant subspace**. The intentional imperfection creates a broad resonance peak (flat-top profile), making the search process robust against parameter drift.

$$
U_{SRFM} |\psi_{target}\rangle \approx e^{i\phi} |\psi_{target}\rangle
$$

---

## Usage & License
This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

### ✅ You are free to:
* **Share:** Copy and redistribute the material in any medium or format.
* **Adapt:** Remix, transform, and build upon the material.

### ❌ Under the following terms:
* **NonCommercial:** You may **NOT** use the material for commercial purposes (including corporate R&D, product development, or patent applications) without explicit permission.

---

## Contact for Commercial Licensing
For commercial usage, joint research, or technical advisory, please contact the author:

**Yoichi [Last Name]**
* Email: [Your Email Address]
* Profile: [Link to Zenodo or LinkedIn if available]

---
*© 2026 Yoichi. All rights reserved.*
