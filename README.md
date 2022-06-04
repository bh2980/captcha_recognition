# Captcha Image Recognition
<img alt="Python" src ="https://img.shields.io/badge/Python-3776AB.svg?&style=round&logo=Python&logoColor=white"/> <img alt="Jupyter" src ="https://img.shields.io/badge/Jupyter-F37626.svg?&style=round&logo=Jupyter&logoColor=white"/> <img alt="Keras" src ="https://img.shields.io/badge/Keras-D00000.svg?&style=round&logo=Keras&logoColor=white"/>
<img alt="OpenCV" src ="https://img.shields.io/badge/OpenCV-5C3EE8.svg?&style=round&logo=OpenCV&logoColor=white"/>
<img alt="NumPy" src ="https://img.shields.io/badge/NumPy-013243.svg?&style=round&logo=NumPy&logoColor=white"/>
<img alt="scikit-learn" src ="https://img.shields.io/badge/scikit-learn-F7931E.svg?&style=round&logo=scikit-learn&logoColor=white"/>


## Description  

* 자동 입력 방지 문자(CAPTCHA) 이미지를 인식할 수 있는 딥러닝 모델 제작
* 개발 인원 : 1명
* 프로젝트 기간 : 2021.08
* 개발 당시 Google Colaboratory로 개발하였으나 현재 Jupyter Notebook으로 구동 가능하도록 수정  

## IDE & Language  

- ~~Google Colaboratory~~ Jupyter Notebook
- python 3.7.7


## Library

```
matplotlib                   3.5.2
numpy                        1.22.4
opencv-python                4.5.5.64
sklearn                      0.0
tensorflow                   2.9.1
```

## Project Process  

1. 데이터 수집
2. 데이터 라벨링
3. 데이터 가공
4. 모델
5. 테스트
6. 결론
  
## Project Detail
<br>

>데이터 수집

![labeled 2021-08-11 오후 1_29_57](https://user-images.githubusercontent.com/74360958/128970367-8d9f1db1-a13b-4a3d-a572-da619e688df5.png)

selenium 라이브러리를 통해서 0.1초마다 새로고침하여 captcha 이미지를 다운로드하는 이미지 다운봇 제작  
<br>

>데이터 라벨링

![캡처](https://user-images.githubusercontent.com/74360958/128970424-7b6c2f69-1ede-4fbd-8480-30d99c0c0cbe.PNG)

파이썬 기본 GUI 라이브러리인 tkinter를 이용하여  
폴더 내부의 사진을 하나씩 띄워주고 입력창에 보안 코드를 작성 후 엔터를 치면  
해당 사진의 파일 이름을 입력한 보안코드로 바꿔주는 프로그램 작성 후 사용  

[2, 3, 4, 5, 6, 7, 8, a, b, c, d, e, f, g, h, k, m, n, p, r, w, x, y] 중 4개의 글자로 구성된  
총 6150개의 라벨링 된 데이터를 얻을 수 있었다.  
<br>

>데이테 가공

![frame2](https://user-images.githubusercontent.com/74360958/148836497-6961a5c0-bff8-40fa-9d35-a8e95aaa8b1f.png)

다음과 같이 샘플에서 적절한 frame 너비와 위치를 계산한다

- frame_size: 28px x 40px
- start_padding : 5px
- overlapped : 8px

그 후 opencv를 이용하여 grayscale로 로드 후 각 이미지를 frame에 맞게 자른다.
<br>

<img width="427" alt="화면 캡처 2022-01-11 060119" src="https://user-images.githubusercontent.com/74360958/148838844-c63c5fc2-ce3d-497b-9a52-b4f5505689b6.png">

나뉘어진 data를 opencv를 후처리한다.

<br>

>모델

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 flatten (Flatten)           (None, 1120)              0         
                                                                 
 dense (Dense)               (None, 128)               143488    
                                                                 
 dense_1 (Dense)             (None, 128)               16512     
                                                                 
 dense_2 (Dense)             (None, 128)               16512     
                                                                 
 dense_3 (Dense)             (None, 23)                2967      
                                                                 
=================================================================
Total params: 179,479
Trainable params: 179,479
Non-trainable params: 0
_________________________________________________________________
```
후처리된 각 글자별 테스트 셋을 이용해 위 모델을 학습시킨다.

<br>


>테스트  

unlabeled test set에 대해서 test를 진행해보았다.
<br>

#### - 글자 1개에 대한 테스트

|w|p|
|---|---|
|![image](https://user-images.githubusercontent.com/74360958/172026579-c4ad99c3-ead3-46aa-8bba-a54919e16d97.png)|![image](https://user-images.githubusercontent.com/74360958/172026906-4efa65d3-6a75-4539-bd4c-0ba56dfc3fae.png)|
|![image](https://user-images.githubusercontent.com/74360958/172026894-4c581ff9-0f46-4b5e-a61b-dee78e8e18d7.png)|![image](https://user-images.githubusercontent.com/74360958/172026909-cbf8388c-1933-410d-bc43-82a6d4a9003d.png)|

<br>

#### - 전체 글자에 대한 테스트

|cycr|472h|
|---|---|
|![cycr](https://user-images.githubusercontent.com/74360958/172026954-3e8711fd-cbc7-432e-a373-46cb9d64b0d5.png)|![427h](https://user-images.githubusercontent.com/74360958/172027071-3e73390b-0d14-417d-997e-2884d54094a0.png)|
|![image](https://user-images.githubusercontent.com/74360958/172026722-2d2fee1d-db8f-4224-9344-3a10b94b26fa.png)|![image](https://user-images.githubusercontent.com/74360958/172027076-a796bf3f-d99e-4c59-abb8-4cb092c63714.png)|
|![image](https://user-images.githubusercontent.com/74360958/172026734-2c58474d-5a7d-44cb-8b87-145212987992.png)|![image](https://user-images.githubusercontent.com/74360958/172027092-97f0cbc2-087d-4c67-b364-0a8e56fc88c9.png)|

<br>

> 결론

* 간단한 모델임에도 불구하고 생각보다 높은 정확도를 보여 놀라움.
* 그러나 이미지를 고정크기로 잘라 인식하므로 m과 같이 긴 글자의 경우 n으로 예측하는 빈도가 높음.

<br>


> 참고

[Building a Captcha OCR in TF2.0](https://www.kaggle.com/aakashnain/building-a-captcha-ocr-in-tf2-0) in Kaggle  
[20211_AI](https://github.com/bh2980/20211_AI)
