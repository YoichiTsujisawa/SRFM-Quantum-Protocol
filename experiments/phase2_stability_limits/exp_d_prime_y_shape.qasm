OPENQASM 2.0;
include "qelib1.inc";

qreg q[4];
creg c[4];

// --- Initial rotations ---
rz(pi/2) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(pi/2) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

rz(pi/2) q[2];
rx(pi/2) q[2];
rz(pi/2) q[2];

// --- First entanglement ---
cz q[1], q[2];

rz(-3*pi/5) q[2];
rx(pi/2) q[2];
rz(pi/2) q[2];

rz(pi/2) q[3];
rx(pi/2) q[3];
rz(pi/2) q[3];

cz q[1], q[3];
cz q[1], q[0];

// --- Middle rotations ---
rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

cz q[1], q[2];

rz(pi/2) q[2];
rx(pi/2) q[2];
rz(-3*pi/5) q[2];

rz(-3*pi/5) q[3];
rx(pi/2) q[3];
rz(pi/2) q[3];

cz q[1], q[3];
cz q[1], q[0];

// --- Final rotations ---
rz(pi/2) q[0];
rx(pi/2) q[0];
rz(-3*pi/5) q[0];

rz(pi/2) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

rz(pi/2) q[3];
rx(pi/2) q[3];
rz(-3*pi/5) q[3];

// --- Measurement ---
measure q[2] -> c[0];
measure q[1] -> c[1];
measure q[3] -> c[2];
measure q[0] -> c[3];
