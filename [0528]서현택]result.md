# [0528] Roundtrip 결과 — inverse_semi_spatial

> `[hair_orig | sketch_pred | matte | hair_recon]`

- hair_orig : 원본 이미지
- sketch_pred : inverse 모델이 생성한 sketch
- matte : 원본 matte
- hair_recon : sketch_pred를 forward 모델 input으로 주고 생성한 결과

![0000](inverse_semi_spatial/roundtrip_grid.png)


# 이전 결과와 비교.
 - **Sketch Before** (`stage2_check`): DiT-only inverse — DiT feature 32×32에서 stroke 위치 예측, binary mask + grid color sampling 방식. strand-level 공간 정보 소실로 스케치 품질 불량.
- **Sketch After** (`inverse_semi_spatial/last`): CNN + Cross-Attention Fusion 도입 — CNN pixel-space encoder(512→64)로 strand-level 공간 정보 보존, DiT semantic feature를 Cross-Attention(Q=CNN, K/V=DiT)으로 융합. direct RGB prediction으로 mean-collapse 방지.


| GT Sketch | GT Hair | Sketch Before | Hair Before | Sketch After | Hair After |
|-----------|---------|---------------|-------------|--------------|------------|
| <img src="dataset/braid/sketch/test/braid_2534.png" width="150"> | <img src="dataset/braid/img/test/braid_2534.png" width="150"> | <img src="stage2_check/braid_2534_sketch.png" width="150"> | <img src="stage2_roundtrip_result/0000_result.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2534_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0000.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2537.png" width="150"> | <img src="dataset/braid/img/test/braid_2537.png" width="150"> | <img src="stage2_check/braid_2537_sketch.png" width="150"> | <img src="stage2_roundtrip_result/0001_result.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2537_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0001.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2539.png" width="150"> | <img src="dataset/braid/img/test/braid_2539.png" width="150"> | <img src="stage2_check/braid_2539_sketch.png" width="150"> | <img src="stage2_roundtrip_result/0002_result.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2539_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0002.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2562.png" width="150"> | <img src="dataset/braid/img/test/braid_2562.png" width="150"> | <img src="stage2_check/braid_2562_sketch.png" width="150"> | <img src="stage2_roundtrip_result/0004_result.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2562_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0004.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2572.png" width="150"> | <img src="dataset/braid/img/test/braid_2572.png" width="150"> | <img src="stage2_check/braid_2572_sketch.png" width="150"> | <img src="stage2_roundtrip_result/0005_result.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2572_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0005.png" width="150"> |


# Forward 모델과의 비교

- **Hair\_Forward** (`results/DiT(before)`): GT sketch를 입력으로 forward ControlNet만 적용한 결과
- **Sketch\_After** (`inverse_semi_spatial/last`): SemiSpatialNet(CNN+Cross-Attn)으로 hair → sketch 변환
- **Hair\_After** (`inverse_semi_spatial/roundtrip_onlyhair`): inverse sketch를 forward에 통과시킨 roundtrip 결과

| GT Sketch | GT Hair | Hair\_Forward (GT→Forward) | Sketch\_After (Inverse) | Hair\_After (Roundtrip) |
|-----------|---------|---------------------------|------------------------|------------------------|
| <img src="dataset/braid/sketch/test/braid_2534.png" width="150"> | <img src="results/DiT(before)/0000_target.png" width="150"> | <img src="results/DiT(before)/0000_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2534_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0000.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2537.png" width="150"> | <img src="results/DiT(before)/0001_target.png" width="150"> | <img src="results/DiT(before)/0001_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2537_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0001.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2539.png" width="150"> | <img src="results/DiT(before)/0002_target.png" width="150"> | <img src="results/DiT(before)/0002_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2539_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0002.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2548.png" width="150"> | <img src="results/DiT(before)/0003_target.png" width="150"> | <img src="results/DiT(before)/0003_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2548_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0003.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2562.png" width="150"> | <img src="results/DiT(before)/0004_target.png" width="150"> | <img src="results/DiT(before)/0004_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2562_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0004.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2572.png" width="150"> | <img src="results/DiT(before)/0005_target.png" width="150"> | <img src="results/DiT(before)/0005_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2572_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0005.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2574.png" width="150"> | <img src="results/DiT(before)/0006_target.png" width="150"> | <img src="results/DiT(before)/0006_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2574_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0006.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2576.png" width="150"> | <img src="results/DiT(before)/0007_target.png" width="150"> | <img src="results/DiT(before)/0007_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2576_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0007.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2590.png" width="150"> | <img src="results/DiT(before)/0008_target.png" width="150"> | <img src="results/DiT(before)/0008_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2590_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0008.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2592.png" width="150"> | <img src="results/DiT(before)/0009_target.png" width="150"> | <img src="results/DiT(before)/0009_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2592_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0009.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2617.png" width="150"> | <img src="results/DiT(before)/0010_target.png" width="150"> | <img src="results/DiT(before)/0010_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2617_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0010.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2625.png" width="150"> | <img src="results/DiT(before)/0011_target.png" width="150"> | <img src="results/DiT(before)/0011_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2625_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0011.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2652.png" width="150"> | <img src="results/DiT(before)/0012_target.png" width="150"> | <img src="results/DiT(before)/0012_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2652_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0012.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2653.png" width="150"> | <img src="results/DiT(before)/0013_target.png" width="150"> | <img src="results/DiT(before)/0013_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2653_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0013.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2657.png" width="150"> | <img src="results/DiT(before)/0014_target.png" width="150"> | <img src="results/DiT(before)/0014_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2657_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0014.png" width="150"> |
| <img src="dataset/braid/sketch/test/braid_2676.png" width="150"> | <img src="results/DiT(before)/0015_target.png" width="150"> | <img src="results/DiT(before)/0015_gen.png" width="150"> | <img src="inverse_semi_spatial/last/braid_2676_sketch.png" width="150"> | <img src="inverse_semi_spatial/roundtrip_onlyhair/0015.png" width="150"> |
