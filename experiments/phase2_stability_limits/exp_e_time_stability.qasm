OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[2];

x q[0];
x q[1];

barrier q[0], q[1];

rz(pi/10) q[0];
rx(pi/10) q[0];
rz(pi/10) q[1];
rx(pi/10) q[1];

cz q[0], q[1];

rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

barrier q[0], q[1];

rz(pi/10) q[0];
rx(pi/10) q[0];
rz(pi/10) q[1];
rx(pi/10) q[1];

cz q[0], q[1];

rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

barrier q[0], q[1];

rz(pi/10) q[0];
rx(pi/10) q[0];
rz(pi/10) q[1];
rx(pi/10) q[1];

cz q[0], q[1];

rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

barrier q[0], q[1];

rz(pi/10) q[0];
rx(pi/10) q[0];
rz(pi/10) q[1];
rx(pi/10) q[1];

cz q[0], q[1];

rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

barrier q[0], q[1];

rz(pi/10) q[0];
rx(pi/10) q[0];
rz(pi/10) q[1];
rx(pi/10) q[1];

cz q[0], q[1];

rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

barrier q[0], q[1];

measure q[0] -> c[0];
measure q[1] -> c[1];
