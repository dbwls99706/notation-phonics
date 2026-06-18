# notation-phonics

**How to actually *say* math, physics & robotics notation out loud — KO / EN.**

Plenty of references tell you α is "alpha."  
Almost none tell you how to read `q̇` aloud in a meeting, whether ξ is "ksy" or "zy," or that ∂ is "partial," not "dee."  
This repo fills that gap, with a robotics / control / ML bias.

**🔎 Live search + audio → https://dbwls99706.github.io/notation-phonics/**

> 🇰🇷 한국어: **[README.ko.md](README.ko.md)**

Two layers per entry: a **pronunciation core** (field-agnostic — how to say it) and a **meaning layer** (what it denotes in robotics & ML, plus look-alikes to avoid).

_Contributions welcome — add a line to [`data/symbols.yaml`](data/symbols.yaml) and run `python scripts/generate.py`. See [CONTRIBUTING.md](CONTRIBUTING.md)._

## Contents

- [Greek letters](#greek-letters)
- [Accents & decorations](#accents--decorations)
- [Operators](#operators)
- [Relations & comparison](#relations--comparison)
- [Set & logic](#set--logic)
- [Number sets](#number-sets)
- [Probability & statistics](#probability--statistics)
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
| ∘ | `\circ` | composition / ring | (function) composition / ring / 'of' | function composition. f∘g = 'f after g' / 'f composed with g' | not the dot product (·) nor degree (°) |
| ⊙ | `\odot` | Hadamard / elementwise product | Hadamard product / elementwise product / o-dot | elementwise multiply — common in deep learning | — |
| ⟨·,·⟩ | `\langle \cdot, \cdot \rangle` | inner product / angle brackets | inner product / 'angle brackets' / 'x y inner product' | inner product ⟨x,y⟩; also Dirac bra-ket | — |
| ∇² / Δ | `\nabla^2 / \Delta` | Laplacian | Laplacian / del squared / nabla squared | Laplace operator (∇·∇) | the Δ form collides with delta (difference) — disambiguate by context |
| ⌊x⌋ / ⌈x⌉ | `\lfloor x \rfloor / \lceil x \rceil` | floor / ceiling | floor of x / ceiling of x | round down / round up to an integer | — |
| A† | `A^\dagger` | dagger / conjugate transpose | A dagger / A Hermitian (conjugate) transpose | conjugate (Hermitian) transpose; sometimes the pseudoinverse | equals plain transpose xᵀ for real matrices |
| ⊥ | `\perp` | perpendicular / orthogonal | perp / perpendicular / orthogonal to | a⊥b = 'a perp b'; orthogonal complement V⊥ | — |
| ∥ | `\parallel` | parallel | parallel to | — | do not confuse with the norm ‖·‖ |
| O(·) | `\mathcal{O}(\cdot)` | big-O | big-O / order of | asymptotic complexity. O(n²) = 'big-O of n squared' | the letter O, not zero |
| ∇θ | `\nabla_\theta` | gradient w.r.t. θ | del theta / gradient with respect to θ | gradient taken w.r.t. parameters θ — backbone of gradient descent | subscript names the variable differentiated against |
| arg max / arg min | `\arg\max / \arg\min` | argmax / argmin | arg max / arg min | the input that maximizes/minimizes — returns the argument x*, not the value | — |
| ℓ | `\ell` | script ell | ell (script l) | the 'ℓ' in ℓ₂/ℓ₁ norms; also a loss ℓ(·) | distinct from the digit 1 and capital I |
| ∗ | `\ast` | convolution | convolution / asterisk | (f∗g) = 'f convolved with g' — CNNs & signal processing | different from superscript star x* (optimal/conjugate) |
| δᵢⱼ | `\delta_{ij}` | Kronecker delta | Kronecker delta / 'delta i j' | 1 if i=j, else 0 — the entries of the identity matrix | different from the Dirac delta δ(x) |
| ∮ | `\oint` | contour integral | contour integral / closed integral / 'oint' | integral over a closed loop — electromagnetics & complex analysis | — |

## Relations & comparison

<a id="relations--comparison"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ≈ | `\approx` | approximately equal | approximately equal / approx | — | — |
| ≃ / ≅ | `\simeq / \cong` | isomorphic / congruent | isomorphic to / congruent to | ≅ often reads 'isomorphic to' for groups/spaces | — |
| ≡ | `\equiv` | identical / equivalent | identically equal / equivalent / congruent (mod) | a≡b (mod n) = 'a is congruent to b modulo n' | — |
| ∼ | `\sim` | tilde relation | tilde / 'distributed as' / 'on the order of' | X∼N(0,1) = 'X is distributed as standard normal' | — |
| ≠ | `\neq` | not equal | not equal to | — | — |
| ≤ / ≥ | `\leq / \geq` | less than or equal / greater than or equal | less than or equal / greater than or equal | — | — |
| ≪ / ≫ | `\ll / \gg` | much less / much greater than | much less than / much greater than | — | — |
| ± / ∓ | `\pm / \mp` | plus-minus / minus-plus | plus or minus / minus or plus | — | — |
| ∞ | `\infty` | infinity | infinity | ℓ∞ norm = 'L-infinity norm' / max norm | — |
| → | `\to / \rightarrow` | to / arrow | 'to' / 'goes to' / 'approaches' | f: A→B = 'f from A to B'; xₙ→x = 'converges to' | different from ↦ (maps to): → is between sets |
| ↦ | `\mapsto` | maps to | maps to | x↦x² = 'x maps to x squared'; element-level rule | → relates sets; ↦ relates elements |
| ⇒ | `\Rightarrow / \implies` | implies | implies / 'if … then' | — | — |
| ⇔ | `\Leftrightarrow / \iff` | if and only if | if and only if / iff | — | — |
| := | `\coloneqq` | colon-equals / defined as | colon-equals / 'is defined as' / 'gets' | definition or assignment. x := x+1 = 'x gets x plus 1' | overlaps with ≜ for 'defined as' |

## Set & logic

<a id="set--logic"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ∈ | `\in` | element of | in / element of | R∈SO(3) → 'R in S-O three' | — |
| ∀ | `\forall` | for all | for all | — | — |
| ∃ | `\exists` | there exists | there exists | — | — |
| ≜ | `\triangleq` | defined as | defined as / is defined to be | — | — |
| ∝ | `\propto` | proportional to | proportional to | — | — |
| ∅ | `\emptyset / \varnothing` | empty set | empty set / the null set | — | not Greek φ (phi) nor the digit 0 |
| ∪ / ∩ | `\cup / \cap` | union / intersection | union / intersection ('cup' / 'cap') | — | — |
| ⊂ / ⊆ | `\subset / \subseteq` | subset | subset of / subset of or equal to | — | — |
| ¬ | `\neg / \lnot` | logical not | not / negation | — | — |
| ∧ / ∨ | `\land / \lor` | logical and / or | logical and / logical or ('wedge' / 'vee') | — | ∧ also the wedge product; ∨ also the vee map |
| ∴ / ∵ | `\therefore / \because` | therefore / because | therefore / because | — | — |
| ∉ | `\notin` | not an element of | not an element of / not in | — | — |

## Number sets

<a id="number-sets"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| ℝ | `\mathbb{R}` | real numbers | the reals / real numbers / 'R' | set of reals. ℝⁿ = 'R n', n-dimensional real space | — |
| ℝⁿ / ℝᵐˣⁿ | `\mathbb{R}^n / \mathbb{R}^{m\times n}` | real vector / matrix space | R n / R m by n | n-vectors / m×n matrices — the workhorse dimension tag | — |
| ℤ | `\mathbb{Z}` | integers | the integers / 'Z' | integers (from German 'Zahlen') | — |
| ℂ | `\mathbb{C}` | complex numbers | the complexes / complex numbers / 'C' | — | — |
| ℕ | `\mathbb{N}` | natural numbers | the naturals / natural numbers / 'N' | — | — |
| ℚ | `\mathbb{Q}` | rational numbers | the rationals / rational numbers / 'Q' | rationals (from 'quotient') | — |

## Probability & statistics

<a id="probability--statistics"></a>

| Symbol | LaTeX | Name | Say it | In robotics / meaning | Watch out |
|---|---|---|---|---|---|
| 𝔼[·] | `\mathbb{E}[\cdot]` | expectation | expectation / expected value / 'E of' | 𝔼[X] = 'expected value of X' — estimation & RL core | — |
| ℙ(·) | `\mathbb{P}(\cdot)` | probability | probability / 'P of' | ℙ(A) = 'probability of event A' | — |
| 𝒩(μ,σ²) | `\mathcal{N}(\mu, \sigma^2)` | Normal / Gaussian | Normal / Gaussian / 'N of mu, sigma squared' | Normal distribution with mean μ and variance σ² | — |
| 𝟙[·] | `\mathbb{1}[\cdot]` | indicator function | indicator function / 'one if' | 1 if the condition holds, else 0 | — |
| D_KL(P‖Q) | `D_{\mathrm{KL}}(P \,\|\, Q)` | KL divergence | K-L divergence / Kullback–Leibler divergence | divergence between two distributions; reads 'KL of P from Q' | asymmetric: D_KL(P‖Q) ≠ D_KL(Q‖P) |

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
| ℒ | `\mathcal{L}` | Lagrangian / loss | Lagrangian / (deep learning) loss | ℒ=T−V in dynamics, or the loss function in ML | script ℒ also denotes the Laplace transform or likelihood |
| ℋ | `\mathcal{H}` | Hamiltonian / Hilbert space | Hamiltonian / Hilbert space | Hamiltonian in optimal control/dynamics; Hilbert space in analysis | — |

---

_Generated from `data/symbols.yaml`. Do not edit the tables by hand._
