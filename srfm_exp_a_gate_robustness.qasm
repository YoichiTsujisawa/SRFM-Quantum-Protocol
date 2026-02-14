OPENQASM 2.0;
include "qelib1.inc";

// 2量子ビットと2古典ビットのレジスタを定義
qreg q[2];
creg c[2];

// --- 初期化 (Hadamardライクな重ね合わせ) ---
// Qubit 0
rz(pi/2) q[0];
sx q[0];
rz(pi/2) q[0];

// Qubit 1
rz(pi/2) q[1];
sx q[1];
rz(pi/2) q[1];

// --- 意図的なノイズ注入とエンタングルメント (SRFM Core) ---
cz q[0], q[1];

// Layer 1: 特徴的な位相 (-3*pi/5) を注入
rz(-3*pi/5) q[0];
rx(pi/2) q[0];
rz(pi/2) q[0];

rz(-3*pi/5) q[1];
rx(pi/2) q[1];
rz(pi/2) q[1];

// Layer 2: 再エンタングルメント
cz q[0], q[1];

// Layer 3: 位相の調整
rz(pi/2) q[0];
rx(pi/2) q[0];
rz(-3*pi/5) q[0];

rz(pi/2) q[1];
rx(pi/2) q[1];
rz(-3*pi/5) q[1];

// --- 測定 ---
measure q[0] -> c[0];
measure q[1] -> c[1];
