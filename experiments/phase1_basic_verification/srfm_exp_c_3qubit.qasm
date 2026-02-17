// Experiment 3: Scalability Test (Actual Hardware Implementation)
// Author: Yoichi
// Target: IBM Quantum Composer (OpenQASM 2.0)
// Description: SRFM 3-qubit chain with manual gate decomposition for max compatibility.

OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

// --- Initialization ---
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];

rz(-pi/2) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// --- Interaction Block 1 ---
// Decomposed rzz(pi/4) on q[1], q[0]
cx q[1], q[0];
rz(pi/4) q[0];
cx q[1], q[0];

rz(pi/4) q[0];
rx(pi) q[0];
rz(pi/4) q[1];
rx(pi/2) q[1];
rz(-pi/2) q[1];

// --- Interaction Block 2 ---
rz(pi/2) q[2];
sx q[2];
rz(pi/2) q[2];
cz q[2], q[1];

rz(pi/2) q[1];
rx(-pi/2) q[1];

// Decomposed rzz(pi/4) on q[1], q[0]
cx q[1], q[0];
rz(pi/4) q[0];
cx q[1], q[0];

rz(pi/4) q[0];
rx(-pi/2) q[0];

rz(pi/4) q[1];
rx(pi/2) q[1];
rz(-pi/2) q[1];

cz q[2], q[1];
rx(2*pi/5) q[1];

// --- Mixing Layer ---
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];

x q[2];

// Decomposed rzz(pi/4) on q[2], q[1]
cx q[2], q[1];
rz(pi/4) q[1];
cx q[2], q[1];

// --- Parameter Tuning (SRFM Specific) ---
rz(-1.0995574287564285) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// Decomposed rzz(pi/4) on q[0], q[1]
cx q[0], q[1];
rz(pi/4) q[1];
cx q[0], q[1];

rz(-pi/4) q[0];
rx(pi/2) q[0];
rz(-pi/2) q[0];

rz(pi/4) q[1];
rx(-pi/2) q[1];

cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];

rz(-2.0420352248333655) q[2];
rx(pi/2) q[2];
rz(-pi/2) q[2];

cz q[2], q[1];
rz(pi/2) q[1];
rx(-pi/2) q[1];

// Decomposed rzz(pi/4) on q[1], q[0]
cx q[1], q[0];
rz(pi/4) q[0];
cx q[1], q[0];

rz(pi/4) q[0];
rx(-pi/2) q[0];
rz(pi/4) q[1];
rx(pi/2) q[1];
rz(-pi/2) q[1];

cz q[2], q[1];
rz(0.9*pi) q[1]; // Intentional Shift (SRFM Core)
rx(pi/2) q[1];

cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];

x q[2];

// Decomposed rzz(pi/4) on q[2], q[1]
cx q[2], q[1];
rz(pi/4) q[1];
cx q[2], q[1];

// --- Final Rotations ---
rz(3*pi/4) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

rz(pi/4) q[2];
rx(pi/2) q[2];
rz(2*pi/5) q[2];

// --- Measurement ---
measure q[2] -> c[0];
measure q[0] -> c[1];
measure q[1] -> c[2];