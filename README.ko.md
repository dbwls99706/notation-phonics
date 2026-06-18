# notation-phonics

**수학 · 물리 · 로보틱스 표기를 실제로 *어떻게 소리 내어 읽는지* 정리 — 한국어 / 영어.**

α가 "알파"라는 건 어디나 있습니다.  
하지만 `q̇`를 회의에서 어떻게 읽는지, ξ가 "크사이"인지 "크시"인지, ∂가 "디"가 아니라 "파셜"인지 알려주는 곳은 거의 없습니다.  
이 저장소가 그 빈틈을 로보틱스 · 제어 관점에서 채웁니다.

> 🇬🇧 English: **[README.md](README.md)**

각 항목은 두 레이어로 구성됩니다: **발음 코어**(분야 무관 — 어떻게 읽는가)와 **의미 레이어**(로보틱스에서 무엇을 뜻하는가, 헷갈리는 기호 주의).

_기여 환영 — [`data/symbols.yaml`](data/symbols.yaml)에 한 줄 추가하고 `python scripts/generate.py` 실행. [CONTRIBUTING.md](CONTRIBUTING.md) 참고._

## 목차

- [그리스 문자](#greek-letters)
- [악센트 · 장식 기호](#accents--decorations)
- [연산자](#operators)
- [집합 · 논리](#set--logic)
- [로보틱스 · 리 이론](#robotics--lie-theory)

## 그리스 문자

<a id="greek-letters"></a>

| 기호 | LaTeX | 이름 | 읽는 법 | 로보틱스에서 / 의미 | 주의 |
|---|---|---|---|---|---|
| α | `\alpha` | Alpha | 알파 | 각가속도, 받음각, 학습률(learning rate) | — |
| β | `\beta` | Beta | 베타 | 옆미끄럼각(sideslip) | — |
| γ / Γ | `\gamma / \Gamma` | Gamma | 감마 | 할인율(RL discount factor), 표면장력 | — |
| δ / Δ | `\delta / \Delta` | Delta | 델타 | δ: 미소 변화·디랙 델타 / Δ: 변화량 | — |
| ε / ϵ | `\varepsilon / \epsilon` | Epsilon | 엡실론 | 아주 작은 양, ε-greedy | — |
| ζ | `\zeta` | Zeta | 제타 | 감쇠비(damping ratio) — 제어의 핵심 | ξ(크사이)와 혼동 주의 |
| η | `\eta` | Eta | 에타 | 효율, 학습률 | — |
| θ / Θ | `\theta / \Theta` | Theta | 세타 (쎄타/씨타로도 발음, '세타'가 표준) | 관절 각도(joint angle) — 로보틱스 핵심, 파라미터 | — |
| ι | `\iota` | Iota | 이오타 | — | — |
| κ | `\kappa` | Kappa | 카파 | 곡률(curvature), 조건수(condition number) | — |
| λ / Λ | `\lambda / \Lambda` | Lambda | 람다 | 고윳값(eigenvalue), 파장, 라그랑주 승수 | — |
| μ | `\mu` | Mu | 뮤 | 마찰계수, 평균 | — |
| ν | `\nu` | Nu | 뉴 | 푸아송 비, 동점성계수 | ν(뉴) vs 라틴 v vs υ(입실론) — 셋 다 비슷하게 생김 |
| ξ / Ξ | `\xi / \Xi` | Xi | 크사이 / 크시 (둘 다 통용, 합의 없음) | 트위스트(twist) 좌표 — 스크류 이론 | ζ(제타)와 혼동 주의 |
| ο | `o` | Omicron | 오미크론 | — | 라틴 o와 똑같이 생겨 거의 안 씀 |
| π / Π | `\pi / \Pi` | Pi | 파이 | 원주율, Π: 곱(product), 정책(policy, RL) | φ와 둘 다 '파이'로 읽혀 혼동 → 보통 φ를 '피'로 구분 |
| ρ | `\rho` | Rho | 로 ('르호' 아님) | 밀도, 스펙트럴 반지름 | 라틴 p와 혼동 주의 |
| σ / Σ | `\sigma / \Sigma` | Sigma | 시그마 | 표준편차, 특잇값, 응력 / Σ: 합(sum) | — |
| τ | `\tau` | Tau | 타우 | 토크(torque) — 로보틱스 핵심, 시정수(time constant) | — |
| υ | `\upsilon` | Upsilon | 입실론 (웁실론으로도) | — | ν(뉴), 라틴 v와 혼동 주의 |
| φ / ϕ / Φ | `\varphi / \phi / \Phi` | Phi | 파이 또는 피 (π와 구분 위해 '피'를 권장) | 롤 각(roll), 자기선속, 황금비 | π와 둘 다 '파이' → 국립국어원도 phi는 '피'로 표기 |
| χ | `\chi` | Chi | 카이 ('치'·'엑스' 아님) | χ²: 카이제곱(chi-square) | 라틴 x와 혼동 주의 — 모양이 같음 |
| ψ / Ψ | `\psi / \Psi` | Psi | 프사이 / 프시 | 요 각(yaw angle) — 로보틱스, 파동함수 | — |
| ω / Ω | `\omega / \Omega` | Omega | 오메가 | 각속도(angular velocity) — 로보틱스 핵심 / Ω: 옴(저항) | — |

## 악센트 · 장식 기호

<a id="accents--decorations"></a>

| 기호 | LaTeX | 이름 | 읽는 법 | 로보틱스에서 / 의미 | 주의 |
|---|---|---|---|---|---|
| ẋ | `\dot{x}` | x dot | 엑스 닷 / 엑스 도트 | 시간 1차 미분, 관절 속도 | — |
| ẍ | `\ddot{x}` | x double dot | 엑스 더블닷 | 시간 2차 미분, 가속도 | — |
| x̂ | `\hat{x}` | x hat | 엑스 햇 | 추정값(estimate) 또는 단위벡터 | — |
| x̄ | `\bar{x}` | x bar | 엑스 바 | 평균 또는 보수(complement) | — |
| x̃ | `\tilde{x}` | x tilde | 엑스 틸드 | 오차(error) 또는 섭동(perturbation) | — |
| x′ | `x'` | x prime | 엑스 프라임 | 도함수 또는 변환된 좌표계의 값 | — |
| x* | `x^*` | x star | 엑스 스타 | 최적값(optimal) 또는 켤레(conjugate) | — |
| xᵀ | `x^\top` | x transpose | 엑스 트랜스포즈 | 전치(transpose) | — |
| A⁺ | `A^+` | A plus / dagger | 에이 플러스 / 에이 대거(dagger) | 유사역행렬(pseudoinverse) | — |
| ‖x‖ | `\lVert x \rVert` | norm | 엑스 놈 / 노름 | 벡터의 크기(노름) | — |

## 연산자

<a id="operators"></a>

| 기호 | LaTeX | 이름 | 읽는 법 | 로보틱스에서 / 의미 | 주의 |
|---|---|---|---|---|---|
| ∇ | `\nabla` | nabla / del | 나블라 / 델 | 그래디언트(gradient) | ∂(파셜)과 다름 |
| ∇· | `\nabla \cdot` | divergence | 델 닷 / 다이버전스 | 발산(divergence) | — |
| ∇× | `\nabla \times` | curl | 델 크로스 / 컬 | 회전(curl) | — |
| ∂ | `\partial` | partial | 파셜 / 라운드 ('디' 아님) | 편미분. ∂f/∂x = '파셜 에프 파셜 엑스' | — |
| ∑ | `\sum` | summation | 시그마 / 썸 | 총합 | — |
| ∏ | `\prod` | product | 파이 / 프로덕트 | 총곱 | — |
| ∫ | `\int` | integral | 인테그럴 / 적분 | — | — |
| ⊗ | `\otimes` | tensor / Kronecker product | 텐서곱 / 크로네커곱 / 오타임스 | — | — |
| ⊕ | `\oplus` | direct sum / XOR | 직합 / 오플러스 / (논리)엑스오어 | — | — |
| × | `\times` | cross | 크로스 / 외적 | 벡터의 외적 | — |
| · | `\cdot` | dot | 닷 / 내적 | 벡터의 내적 | — |

## 집합 · 논리

<a id="set--logic"></a>

| 기호 | LaTeX | 이름 | 읽는 법 | 로보틱스에서 / 의미 | 주의 |
|---|---|---|---|---|---|
| ∈ | `\in` | element of | ~의 원소 / 엘리먼트 오브 | R∈SO(3) → '알은 에스오쓰리의 원소' | — |
| ∀ | `\forall` | for all | 모든 / 포 올 | — | — |
| ∃ | `\exists` | there exists | 존재한다 / 데어 이그지스츠 | — | — |
| ≜ | `\triangleq` | defined as | 정의된다 / 트라이앵글 이퀄스 | — | — |
| ∝ | `\propto` | proportional to | 비례한다 / 프로포셔널 투 | — | — |

## 로보틱스 · 리 이론

<a id="robotics--lie-theory"></a>

| 기호 | LaTeX | 이름 | 읽는 법 | 로보틱스에서 / 의미 | 주의 |
|---|---|---|---|---|---|
| SE(3) | `SE(3)` | Special Euclidean group | 에스 이 쓰리 | 강체 변환(회전+병진)의 군 | — |
| SO(3) | `SO(3)` | Special Orthogonal group | 에스 오 쓰리 | 3D 회전군 | — |
| 𝔰𝔬(3) / so(3) | `\mathfrak{so}(3)` | Lie algebra so(3) | 스몰 에스 오 쓰리 / 리 대수 에스오쓰리 | 반대칭(skew-symmetric) 행렬 공간 | 대문자 SO(3)와 다름 — 군 vs 대수 |
| [ω]× / ω∧ | `[\omega]_\times / \omega^\wedge` | skew / hat map | 스큐 / 햇 맵 / 오메가 크로스 행렬 | 벡터 → 반대칭 행렬 변환 (so(3)) | — |
| X∨ | `X^\vee` | vee map | 엑스 vee 맵 | 반대칭 행렬 → 벡터 (햇의 역연산) | — |
| J | `J` | Jacobian | 자코비안 | 관절 속도 ↔ 말단 속도 사상 | — |
| ⊞ / ⊟ | `\boxplus / \boxminus` | boxplus / boxminus | 박스플러스 / 박스마이너스 | 매니폴드 위의 가감 연산 (상태추정) | — |
| ᵃRᵦ | `{}^{a}R_{b}` | frame rotation | 에이 알 비 / 'b 좌표계를 a 기준으로' | 위첨자=기준 좌표계, 아래첨자=대상 좌표계 | 팀마다 위/아래 첨자 관습이 반대일 수 있음 |

---

_`data/symbols.yaml`에서 자동 생성됨. 표를 직접 수정하지 마세요._
