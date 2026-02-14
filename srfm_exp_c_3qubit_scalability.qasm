OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

// --- 初期化 ---
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];

rz(-pi/2) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// --- 相互作用ブロック1 ---
// rzz(pi/4) q[1], q[0] の展開
cx q[1], q[0];
rz(pi/4) q[0];
cx q[1], q[0];

rz(pi/4) q[0];
rx(pi) q[0];
rz(pi/4) q[1];
rx(pi/2) q[1];
rz(-pi/2) q[1];

// --- 相互作用ブロック2 ---
rz(pi/2) q[2];
sx q[2];
rz(pi/2) q[2];
cz q[2], q[1];

rz(pi/2) q[1];
rx(-pi/2) q[1];

// rzz(pi/4) q[1], q[0] の展開
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

// --- 混合層 (Mixing) ---
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];

x q[2];

// rzz(pi/4) q[2], q[1] の展開
cx q[2], q[1];
rz(pi/4) q[1];
cx q[2], q[1];

// --- パラメータ調整 (SRFM Specific) ---
rz(-1.0995574287564285) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// rzz(pi/4) q[0], q[1] の展開 (順序注意)
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

// rzz(pi/4) q[1], q[0] の展開
cx q[1], q[0];
rz(pi/4) q[0];
cx q[1], q[0];

rz(pi/4) q[0];
rx(-pi/2) q[0];
rz(pi/4) q[1];
rx(pi/2) q[1];
rz(-pi/2) q[1];

cz q[2], q[1];
rz(0.9*pi) q[1]; // 意図的なズレ (SRFM core)
rx(pi/2) q[1];

cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];
sx q[0];
sx q[1];
cz q[1], q[0];

x q[2];

// rzz(pi/4) q[2], q[1] の展開
cx q[2], q[1];
rz(pi/4) q[1];
cx q[2], q[1];

// --- 最終回転 ---
rz(3*pi/4) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

rz(pi/4) q[2];
rx(pi/2) q[2];
rz(2*pi/5) q[2];

// --- 測定 ---
measure q[2] -> c[0];
measure q[0] -> c[1];
measure q[1] -> c[2];
