// SRFM Experiment F: Robust Search for Target |101>
// Author: Yoichi
// Target State: |101> (q2=1, q1=0, q0=1)
// Method: Using SRFM dynamics to drive convergence to the target solution.

OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[3];

// --- 1. Initialization (Uniform Superposition) ---
// 全探索空間を用意
h q[0];
h q[1];
h q[2];

barrier q;

// --- 2. Oracle (Marking the Target |101>) ---
// |101> の位相を反転させる (Phase Flip)
x q[1]; // 0を1にする
h q[2];
ccx q[0], q[1], q[2]; // q0, q1(flipped), q2 が全て1なら反転
h q[2];
x q[1]; // 元に戻す

barrier q;

// --- 3. SRFM "Attractor" Mixing (The Engine) ---
// グローバーの拡散演算子の代わりに、SRFMで正解へ「誘導」する

// q[0] -> Target '1' (Standard SRFM)
rz(-3*pi/5) q[0]; rx(pi/2) q[0]; rz(pi/2) q[0];

// q[1] -> Target '0' (Inverted SRFM: X -> SRFM -> X)
x q[1]; 
rz(-3*pi/5) q[1]; rx(pi/2) q[1]; rz(pi/2) q[1];
x q[1];

// q[2] -> Target '1' (Standard SRFM)
rz(-3*pi/5) q[2]; rx(pi/2) q[2]; rz(pi/2) q[2];

// --- 4. Reinforcement (Repeat for Stability) ---
// もう一度、アトラクター効果を強める
barrier q;

// q[0] -> Target '1'
rz(pi/2) q[0]; rx(pi/2) q[0]; rz(-3*pi/5) q[0];

// q[1] -> Target '0'
x q[1];
rz(pi/2) q[1]; rx(pi/2) q[1]; rz(-3*pi/5) q[1];
x q[1];

// q[2] -> Target '1'
rz(pi/2) q[2]; rx(pi/2) q[2]; rz(-3*pi/5) q[2];

// --- 5. Measurement ---
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];