# notation-phonics

**How to actually *say* math, physics & robotics notation out loud — KO / EN.**

Plenty of references tell you α is "alpha."  
Almost none tell you how to read `q̇` aloud in a meeting, whether ξ is "ksy" or "zy," or that ∂ is "partial," not "dee."  
This repo fills that gap, with a robotics / control bias.

> 🇰🇷 한국어: **[README.ko.md](README.ko.md)**

Two layers per entry: a **pronunciation core** (field-agnostic — how to say it) and a **meaning layer** (what it denotes in robotics, plus look-alikes to avoid).

_Contributions welcome — add a line to [`data/symbols.yaml`](data/symbols.yaml) and run `python scripts/generate.py`. See [CONTRIBUTING.md](CONTRIBUTING.md)._

## Contents

- [Greek letters](#greek-letters)
- [Accents & decorations](#accents--decorations)
- [Operators](#operators)
- [Set & logic](#set--logic)
- [Robotics & Lie theory](#robotics--lie-theory)

## Greek letters

<a id="greek-letters"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| α | `\alpha` | Alpha | AL-fuh | angular acceleration, angle of attack, learning rate | — |
| β | `\beta` | Beta | BAY-tuh (US) / BEE-tuh (UK) | sideslip angle | — |
| γ / Γ | `\gamma / \Gamma` | Gamma | GAM-uh | discount factor (RL), surface tension | — |
| δ / Δ | `\delta / \Delta` | Delta | DEL-tuh | δ: small change / Dirac delta · Δ: difference, change | — |
| ε / ϵ | `\varepsilon / \epsilon` | Epsilon | EP-si-lon | an arbitrarily small quantity, ε-greedy | — |
| ζ | `\zeta` | Zeta | ZAY-tuh (US) / ZEE-tuh (UK) | damping ratio — core to control theory | do not confuse with ξ (xi) |
| η | `\eta` | Eta | AY-tuh (US) / EE-tuh (UK) | efficiency, learning rate | — |
| θ / Θ | `\theta / \Theta` | Theta | THAY-tuh | joint angle — robotics core, model parameters | — |
| ι | `\iota` | Iota | eye-OH-tuh | — | — |
| κ | `\kappa` | Kappa | KAP-uh | curvature, condition number | — |
| λ / Λ | `\lambda / \Lambda` | Lambda | LAM-duh | eigenvalue, wavelength, Lagrange multiplier | — |
| μ | `\mu` | Mu | MYOO | coefficient of friction, mean | — |
| ν | `\nu` | Nu | NYOO / NOO | Poisson's ratio, kinematic viscosity | ν vs Latin v vs υ (upsilon) — all look alike |
| ξ / Ξ | `\xi / \Xi` | Xi | KSY / ZY / SY — genuinely contested | twist coordinates — screw theory | do not confuse with ζ (zeta) |
| ο | `o` | Omicron | OM-i-kron | — | looks identical to Latin o; rarely used |
| π / Π | `\pi / \Pi` | Pi | PY | the constant π, Π: product, policy (RL) | shares '파이' with φ in Korean; φ often read '피' to disambiguate |
| ρ | `\rho` | Rho | ROH | density, spectral radius | do not confuse with Latin p |
| σ / Σ | `\sigma / \Sigma` | Sigma | SIG-muh | standard deviation, singular value, stress / Σ: summation | — |
| τ | `\tau` | Tau | TAW / TOW | torque — robotics core, time constant | — |
| υ | `\upsilon` | Upsilon | UP-si-lon / YOOP-si-lon | — | confusable with ν (nu) and Latin v |
| φ / ϕ / Φ | `\varphi / \phi / \Phi` | Phi | FY / FEE — both used | roll angle, magnetic flux, golden ratio | shares 'fy' confusion with π; KR convention reads φ as '피' |
| χ | `\chi` | Chi | KY (rhymes with 'sky') | χ²: chi-square | looks like Latin x but is never said 'eks' |
| ψ / Ψ | `\psi / \Psi` | Psi | SY / PSY (the p is often silent) | yaw angle — robotics, wavefunction | — |
| ω / Ω | `\omega / \Omega` | Omega | oh-MAY-guh (US) / OH-mig-uh (UK) | angular velocity — robotics core / Ω: ohm | — |

## Accents & decorations

<a id="accents--decorations"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ẋ | `\dot{x}` | x dot | x dot | first time derivative, joint velocity | — |
| ẍ | `\ddot{x}` | x double dot | x double dot | second time derivative, acceleration | — |
| x̂ | `\hat{x}` | x hat | x hat | estimate, or unit vector | — |
| x̄ | `\bar{x}` | x bar | x bar | mean, or complement | — |
| x̃ | `\tilde{x}` | x tilde | x tilde | error, or perturbation | — |
| x′ | `x'` | x prime | x prime | derivative, or a transformed-frame quantity | — |
| x* | `x^*` | x star | x star | optimal value, or conjugate | — |
| xᵀ | `x^\top` | x transpose | x transpose | transpose | — |
| A⁺ | `A^+` | A plus / dagger | A plus / A dagger | Moore–Penrose pseudoinverse | — |
| ‖x‖ | `\lVert x \rVert` | norm | norm of x | vector norm / magnitude | — |

## Operators

<a id="operators"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ∇ | `\nabla` | nabla / del | del (US classroom default) / nabla | gradient | distinct from ∂ (partial) |
| ∇· | `\nabla \cdot` | divergence | del dot / divergence | divergence of a vector field | — |
| ∇× | `\nabla \times` | curl | del cross / curl | curl of a vector field | — |
| ∂ | `\partial` | partial | partial / curly d / die | partial derivative. ∂f/∂x = 'partial f partial x' | — |
| ∑ | `\sum` | summation | sum / summation | summation | — |
| ∏ | `\prod` | product | product | product over a sequence | — |
| ∫ | `\int` | integral | integral | — | — |
| ⊗ | `\otimes` | tensor / Kronecker product | tensor product / Kronecker product / o-times | — | — |
| ⊕ | `\oplus` | direct sum / XOR | direct sum / o-plus / (logic) XOR | — | — |
| × | `\times` | cross | cross / times | cross product | — |
| · | `\cdot` | dot | dot | dot product | — |

## Set & logic

<a id="set--logic"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ∈ | `\in` | element of | in / element of | R∈SO(3) → 'R in S-O three' | — |
| ∀ | `\forall` | for all | for all | — | — |
| ∃ | `\exists` | there exists | there exists | — | — |
| ≜ | `\triangleq` | defined as | defined as / is defined to be | — | — |
| ∝ | `\propto` | proportional to | proportional to | — | — |

## Robotics & Lie theory

<a id="robotics--lie-theory"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| SE(3) | `SE(3)` | Special Euclidean group | S-E three | group of rigid-body transforms (rotation + translation) | — |
| SO(3) | `SO(3)` | Special Orthogonal group | S-O three | group of 3D rotations | — |
| 𝔰𝔬(3) / so(3) | `\mathfrak{so}(3)` | Lie algebra so(3) | little S-O three / Lie algebra S-O three | space of skew-symmetric matrices | distinct from SO(3): the group vs its algebra |
| [ω]× / ω∧ | `[\omega]_\times / \omega^\wedge` | skew / hat map | skew of omega / omega hat / omega cross-matrix | vector → skew-symmetric matrix (so(3)) | — |
| X∨ | `X^\vee` | vee map | X vee | skew-symmetric matrix → vector (inverse of hat) | — |
| J | `J` | Jacobian | Jacobian (juh-KOH-bee-un) | maps joint velocities to end-effector velocities | — |
| ⊞ / ⊟ | `\boxplus / \boxminus` | boxplus / boxminus | boxplus / boxminus | manifold-aware add/subtract (state estimation) | — |
| ᵃRᵦ | `{}^{a}R_{b}` | frame rotation | a R b / 'rotation of frame b expressed in a' | superscript = reference frame, subscript = target frame | sub/superscript convention varies by team/textbook |

---

_Generated from `data/symbols.yaml`. Do not edit the tables by hand._
