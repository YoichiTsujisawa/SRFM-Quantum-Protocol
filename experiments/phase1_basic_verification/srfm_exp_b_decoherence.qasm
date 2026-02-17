// Experiment B: Decoherence Resilience Test
// Author: Yoichi
// Target: IBM Quantum Composer
// Description: Inserting 'id' gates to simulate noise during idle time.

OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

// Init
rz(pi/2) q[0]; sx q[0]; rz(pi/2) q[0];
rz(pi/2) q[1]; sx q[1]; rz(pi/2) q[1];

// Entangle
cz q[0], q[1];

// SRFM Layer 1
rz(-3*pi/5) q[0]; rx(pi/2) q[0]; rz(pi/2) q[0];
rz(-3*pi/5) q[1]; rx(pi/2) q[1]; rz(pi/2) q[1];

// === NOISE INJECTION (Idle Time) ===
barrier q; // Visual barrier
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1];
id q[0]; id q[1];
barrier q;
// ===================================

// Re-Entangle
cz q[0], q[1];

// Stabilization
rz(pi/2) q[0]; rx(pi/2) q[0]; rz(-3*pi/5) q[0];
rz(pi/2) q[1]; rx(pi/2) q[1]; rz(-3*pi/5) q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];