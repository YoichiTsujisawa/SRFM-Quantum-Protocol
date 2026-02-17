// SRFM: Self-Regulating Field Model (Composer Compatible)
// Author: Yoichi
// License: CC BY-NC 4.0
// Target: IBM Quantum Composer (OpenQASM 2.0)

OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// --- Initialization (Superposition / Hadamard equivalent) ---
// Applying H using native gates: Rz(pi/2) -> Sx -> Rz(pi/2)
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];

rz(pi/2) q[1];
sx q[1];
rz(pi/2) q[1];

// --- Entanglement & Intentional Noise Injection ---
cz q[0], q[1];

// Layer 1: SRFM Phase Injection (-3*pi/5)
rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// Layer 2: Re-Entanglement
cz q[0], q[1];

// Layer 3: Stabilization
rz(pi/2) q[0];
rx(pi/2) q[0];
rz(-3*pi/5) q[0];

rz(pi/2) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

// --- Measurement ---
measure q[0] -> c[0];
measure q[1] -> c[1];