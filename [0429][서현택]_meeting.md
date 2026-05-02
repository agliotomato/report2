## 0429 미팅 내용 정리

1. z_bg를 원본 latent로 변경 (검정 처리 제거)
2. latent weighted-sum 을 SHS 방식으로 교체 후 재평가 (샘플링 방식이면 안 되고, area pooling 방식으로, 여기서 area 는 matte 값으로 진행)
3. 전체 데이터에 대해 비교한 것 정량평가 결과 저장하고, 비교 sheet 구성. (추후 유리한 것 확인)
4. SHS 에서 한계로 직접 언급한 이미지에 대해 실험 후 비교.

## 0430 미팅 내용 정리

1. unbraid 한 데이터에 대해서도 test 해볼것
2. 나노바나나 생성 이미지 remover 하고 다시 test
3. vision banana 이미지에서 stroke을 뺄 수 있는 거. 데이터 증강
aggressive 에 대한 원천 차단 갱
4. braid 평가 / unbraid 평가 / 통합 평가 세 개 다 진행