// SRFM Experiment B: Decoherence Resilience Test
OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Initialization
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];
rz(pi/2) q[1];
sx q[1];
rz(pi/2) q[1];

// Entanglement
cz q[0], q[1];

// --- Noise Injection & Idle Time ---
rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

// Barriers create idle time (decoherence window)
barrier q[0];
barrier q[0];

// Intentional Phase Drift on q[1] (9*pi/10)
rz(9*pi/10) q[1];
barrier q[1];
barrier q[1];

// Recovery
rz(pi/2) q[1];
sx q[1];
rz(pi/2) q[1];

cz q[0], q[1];

// Final Adjustment
rz(pi/2) q[0];
rx(pi/2) q[0];
rz(-3*pi/5) q[0];
rz(pi/2) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
