# Ablation Study C: Curriculum Learning Strategy

## 실험 설정

Curriculum Learning 전략에 따른 성능 차이를 분석한다. 비교 대상은 다음 5가지 조건이다.

| 조건 | 설명 |
|------|------|
| Unbraid Only (c1) | Unbraid 태스크만으로 단독 학습 |
| Braid Only (c2) | Braid 태스크만으로 단독 학습 |
| Joint (c3) | 두 태스크를 동시에 병렬 학습 |
| Reverse Curriculum (c4) | 어려운 태스크(Braid) → 쉬운 태스크(Unbraid) 순서 학습 |
| Ours / Forward Curriculum (c5) | 쉬운 태스크(Unbraid) → 어려운 태스크(Braid) 순서 학습 |

평가는 Combined(전체), Braid 전용, Unbraid 전용 세 구간으로 분리하여 수행하였다.

### 데이터셋 규모

| Split | Data | 비고 |
|-------|------:|------|
| Braid | 107 | |
| Unbraid | 466 | |
| Combined | 573 | Braid + Unbraid |

---


**측정 지표** (unbraid / braid 평가셋 각각):
- Hair FID, Hair LPIPS, SSIM, PSNR
- Edge IoU, Chamfer Distance (braid 구조 정밀도)

## 1. 종합 성능 요약 (Combined) : 573 dataset

Combined 결과는 Braid Only 베이스라인이 없으며, 세 커리큘럼 조건을 직접 비교한다.

| Metric | Joint | Reverse Curriculum | **Ours (Forward)** |
|--------|------:|-------------------:|-------------------:|
| Edge IoU ↑ | 0.0613 | 0.0607 | **0.0616** |
| Chamfer ↓ | **5.3523** | 5.5852 | 5.6994 |
| Sketch LPIPS ↓ | 0.6742 | **0.6717** | 0.6720 |
| PSNR ↑ | 16.1149 | 15.5648 | **16.2746** |
| SSIM ↑ | 0.6047 | 0.5969 | **0.6094** |
| LPIPS ↓ | **0.1928** | 0.2054 | 0.1993 |
| Hair FID ↓ | **50.67** | 55.62 | 53.07 |

**Forward Curriculum이 우세한 지표**: Edge IoU, PSNR, SSIM (3/7)  
**Joint가 우세한 지표**: Chamfer, LPIPS, Hair FID (3/7)  
**Reverse Curriculum이 우세한 지표**: Sketch LPIPS (1/7)

전체적으로 
- Forward Curriculum은 픽셀 수준 재현 품질(PSNR, SSIM)과 구조 검출(Edge IoU)에서 가장 우수하다. 

- 반면 Chamfer와 Hair FID는 Joint가 더 낮아 공간적 정밀도와 분포 충실도 측면에서 Joint가 유리하다.
- Reverse Curriculum은 PSNR(15.56)과 SSIM(0.5969)이 세 조건 중 가장 낮아 전반적 성능이 떨어진다.

---

## 2. Braid 도메인 분석 : 107 Dataset

Braid 전용 이미지에 대한 4개 조건 비교이다.

| Metric | Braid Only | Joint | Reverse Curriculum | **Ours (Forward)** |
|--------|----------:|------:|-------------------:|-------------------:|
| Edge IoU ↑ | 0.1001 | 0.0996 | 0.0995 | **0.1007** |
| Chamfer ↓ | **2.8776** | 2.8807 | 2.8923 | 2.9370 |
| Sketch LPIPS ↓ | 0.7095 | **0.6932** | 0.7058 | 0.7126 |
| PSNR ↑ | 15.3378 | 15.6549 | 14.5220 | **15.8495** |
| SSIM ↑ | 0.6055 | 0.6107 | 0.5872 | **0.6144** |
| LPIPS ↓ | 0.1906 | **0.1780** | 0.2033 | 0.1858 |
| Hair FID ↓ | 80.62 | **79.32** | 103.15 | 83.31 |

**Forward Curriculum이 우세한 지표**: Edge IoU, PSNR, SSIM (3/7)  
**Joint가 우세한 지표**: Sketch LPIPS, LPIPS, Hair FID (3/7)  
**Braid Only가 우세한 지표**: Chamfer (1/7)

- Forward Curriculum은 Braid 도메인에서 픽셀 수준 재현 품질(PSNR 15.85, SSIM 0.6144)에서 가장 우수한 성능을 보인다.

- 이는 Unbraid를 선행 학습함으로써 생성 일반화 능력이 향상된 결과로 해석된다. 

- 그러나 Sketch LPIPS(0.7126), LPIPS(0.1858), Hair FID(83.31)는 Joint에 못 미쳐 지각 품질과 분포 충실도 측면에서 Joint가 여전히 우세하다.

- Chamfer는 Braid Only(2.8776)가 가장 낮아 단일 태스크 특화 학습이 구조적 정밀도에서 유리함을 보여 준다.

- Reverse Curriculum은 Hair FID(103.15)가 심각하게 높아 역순 학습이 Braid 도메인의 분포 학습을 크게 저해함을 시사한다.

---

## 3. Unbraid 도메인 분석 : 466 Dataset

Unbraid 전용 이미지에 대한 4개 조건 비교이다.

| Metric | Unbraid Only | Joint | Reverse Curriculum | **Ours (Forward)** |
|--------|------------:|------:|-------------------:|-------------------:|
| Edge IoU ↑ | 0.0523 | 0.0524 | 0.0518 | **0.0527** |
| Chamfer ↓ | **5.8657** | 5.9198 | 6.2035 | 6.3337 |
| Sketch LPIPS ↓ | 0.6871 | 0.6698 | 0.6638 | **0.6627** |
| PSNR ↑ | 16.0440 | 16.2205 | 15.8042 | **16.3722** |
| SSIM ↑ | 0.6011 | 0.6034 | 0.5992 | **0.6083** |
| LPIPS ↓ | 0.1973 | **0.1962** | 0.2059 | 0.2024 |
| Hair FID ↓ | **53.89** | 54.55 | 58.70 | 56.94 |

**Forward Curriculum이 우세한 지표**: Edge IoU, Sketch LPIPS, PSNR, SSIM (4/7)  
**Joint가 우세한 지표**: LPIPS (1/7)  
**Unbraid Only가 우세한 지표**: Chamfer, Hair FID (2/7)

- Forward Curriculum은 Unbraid 도메인에서 전체적으로 우세하다.
- Edge IoU, Sketch LPIPS, PSNR, SSIM 4개 지표에서 동시에 우위이다.
- Braid를 후속 학습함으로써 오히려 Unbraid 재현 능력이 강화된 결과로 해석할 수 있다.
- LPIPS는 Joint(0.1962)가 근소하게 앞서고, Chamfer와 Hair FID는 Unbraid Only 단독 학습이 가장 낮다.

---

## 4. 지표별 종합 순위

아래는 Combined 기준 7개 지표 각각에서의 방법별 순위 요약이다 (Combined 기준, 단일 태스크 베이스라인 제외).

| Metric | 1위 | 2위 | 3위 |
|--------|-----|-----|-----|
| Edge IoU ↑ | **Ours** (0.0616) | Joint (0.0613) | Reverse (0.0607) |
| Chamfer ↓ | **Joint** (5.3523) | Reverse (5.5852) | Ours (5.6994) |
| Sketch LPIPS ↓ | **Reverse** (0.6717) | Ours (0.6720) | Joint (0.6742) |
| PSNR ↑ | **Ours** (16.2746) | Joint (16.1149) | Reverse (15.5648) |
| SSIM ↑ | **Ours** (0.6094) | Joint (0.6047) | Reverse (0.5969) |
| LPIPS ↓ | **Joint** (0.1928) | Ours (0.1993) | Reverse (0.2054) |
| Hair FID ↓ | **Joint** (50.67) | Ours (53.07) | Reverse (55.62) |

Ours: 3승 / Joint: 3승 / Reverse: 1승 (Combined 기준)

---

## 5. 결론

- Forward Curriculum(Ours)이 Combined, Braid, Unbraid 세 구간에서 PSNR과 SSIM 기준으로 일관되게 최고 성능을 보인다. 
- 지각 품질(LPIPS)과 분포 충실도(Hair FID) 측면에서는 Joint가 우위이다

- Reverse Curriculum은 전반적으로 성능이 떨어지므로, 커리큘럼 학습의 방향성이 결과에 영향을 미침을 보여 준다. 

- 어떤 것을 Ours로 해야할지 의문

---

## 6. 정성적 비교 (Qualitative Results)

### 6.1 Unbraid 결과 비교 (c1, c3, c4, c5)

| GT * matte | c1 (Unbraid Only) | c3 (Joint) | c4 (Reverse) | c5 (Ours) |
|:------:|:-----------------:|:----------:|:------------:|:---------:|
| <img src="matted_samples/CM_1004_masked.png" width="150"> | <img src="ablation_cl_run2/c1_unbraid_only/unbraid/CM_1004.png" width="150"> | <img src="ablation_cl_run2/c3_joint/unbraid/CM_1004.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/unbraid/CM_1004.png" width="150"> | <img src="ablation_cl_run2/c5_ours/unbraid/CM_1004.png" width="150"> |
| <img src="matted_samples/CM_1005_masked.png" width="150"> | <img src="ablation_cl_run2/c1_unbraid_only/unbraid/CM_1005.png" width="150"> | <img src="ablation_cl_run2/c3_joint/unbraid/CM_1005.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/unbraid/CM_1005.png" width="150"> | <img src="ablation_cl_run2/c5_ours/unbraid/CM_1005.png" width="150"> |
| <img src="matted_samples/CM_1006_masked.png" width="150"> | <img src="ablation_cl_run2/c1_unbraid_only/unbraid/CM_1006.png" width="150"> | <img src="ablation_cl_run2/c3_joint/unbraid/CM_1006.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/unbraid/CM_1006.png" width="150"> | <img src="ablation_cl_run2/c5_ours/unbraid/CM_1006.png" width="150"> |
| <img src="matted_samples/CM_1007_masked.png" width="150"> | <img src="ablation_cl_run2/c1_unbraid_only/unbraid/CM_1007.png" width="150"> | <img src="ablation_cl_run2/c3_joint/unbraid/CM_1007.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/unbraid/CM_1007.png" width="150"> | <img src="ablation_cl_run2/c5_ours/unbraid/CM_1007.png" width="150"> |
| <img src="matted_samples/CM_1008_masked.png" width="150"> | <img src="ablation_cl_run2/c1_unbraid_only/unbraid/CM_1008.png" width="150"> | <img src="ablation_cl_run2/c3_joint/unbraid/CM_1008.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/unbraid/CM_1008.png" width="150"> | <img src="ablation_cl_run2/c5_ours/unbraid/CM_1008.png" width="150"> |

---

### 6.2 Braid 결과 비교 (c2, c3, c4, c5)

| GT * matte | c2 (Braid Only) | c3 (Joint) | c4 (Reverse) | c5 (Ours) |
|:------:|:---------------:|:----------:|:------------:|:---------:|
| <img src="matted_samples/braid_2534_masked.png" width="150"> | <img src="ablation_cl_run2/c2_braid_only/braid/braid_2534.png" width="150"> | <img src="ablation_cl_run2/c3_joint/braid/braid_2534.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/braid/braid_2534.png" width="150"> | <img src="ablation_cl_run2/c5_ours/braid/braid_2534.png" width="150"> |
| <img src="matted_samples/braid_2537_masked.png" width="150"> | <img src="ablation_cl_run2/c2_braid_only/braid/braid_2537.png" width="150"> | <img src="ablation_cl_run2/c3_joint/braid/braid_2537.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/braid/braid_2537.png" width="150"> | <img src="ablation_cl_run2/c5_ours/braid/braid_2537.png" width="150"> |
| <img src="matted_samples/braid_2539_masked.png" width="150"> | <img src="ablation_cl_run2/c2_braid_only/braid/braid_2539.png" width="150"> | <img src="ablation_cl_run2/c3_joint/braid/braid_2539.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/braid/braid_2539.png" width="150"> | <img src="ablation_cl_run2/c5_ours/braid/braid_2539.png" width="150"> |
| <img src="matted_samples/braid_2548_masked.png" width="150"> | <img src="ablation_cl_run2/c2_braid_only/braid/braid_2548.png" width="150"> | <img src="ablation_cl_run2/c3_joint/braid/braid_2548.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/braid/braid_2548.png" width="150"> | <img src="ablation_cl_run2/c5_ours/braid/braid_2548.png" width="150"> |
| <img src="matted_samples/braid_2562_masked.png" width="150"> | <img src="ablation_cl_run2/c2_braid_only/braid/braid_2562.png" width="150"> | <img src="ablation_cl_run2/c3_joint/braid/braid_2562.png" width="150"> | <img src="ablation_cl_run2/c4_reverse/braid/braid_2562.png" width="150"> | <img src="ablation_cl_run2/c5_ours/braid/braid_2562.png" width="150"> |

---

