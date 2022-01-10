# CAPTCHA(자동 입력 방지) 문자 인식

> 개요

자동 입력 방지 문자(CAPTCHA) 인식할 수 있는 딥러닝 모델 제작

> 프로젝트 순서

1. 데이터 수집
2. 데이터 라벨링
3. 데이터 가공
4. 모델 정의
5. 학습
6. 테스트
7. 결론

> 사용 언어 및 라이브러리

- python 3.7.7
- selenium
- python-opencv
- tkinter

## 1. 데이터 수집

![labeled 2021-08-11 오후 1_29_57](https://user-images.githubusercontent.com/74360958/128970367-8d9f1db1-a13b-4a3d-a572-da619e688df5.png)

selenium 라이브러리를 통해서 수강신청 홈페이지에 17분마다 자동 로그인 후  
0.1초마다 새로고침하여 캡챠 이미지를 다운로드하는 이미지 다운봇 제작

## 2. 데이터 라벨링

![캡처](https://user-images.githubusercontent.com/74360958/128970424-7b6c2f69-1ede-4fbd-8480-30d99c0c0cbe.PNG)

파이썬 기본 GUI 라이브러리인 tkinter를 이용하여  
폴더 내부의 사진을 하나씩 띄워주고 입력창에 보안 코드를 작성 후 엔터를 치면  
해당 사진의 파일 이름을 입력한 보안코드로 바꿔주는 프로그램 작성 후 사용
총 6150개의 라벨링 된 데이타를 얻을 수 있었다.

## 3. 데이터 가공

![frame2](https://user-images.githubusercontent.com/74360958/148836497-6961a5c0-bff8-40fa-9d35-a8e95aaa8b1f.png)

다음과 같이 샘플에서 적절한 frame 너비와 위치를 계산한다

- frame_size: 28px x 40px
- start_padding : 5px
- between_padding : 8px

그 후 opencv를 이용하여 grayscale로 로드 후 각 이미지를 frame에 맞게 자른다.

![2_0](https://user-images.githubusercontent.com/74360958/148837068-4d96407a-6e93-4037-8e29-15bbc0c8ee64.png)
![5_29](https://user-images.githubusercontent.com/74360958/148837098-b7dbf392-223d-4003-ab3a-b8eeeefd0159.png)
![k_134](https://user-images.githubusercontent.com/74360958/148837125-a40fb673-e427-47bc-b383-b6bf705a18c2.png)

<img width="427" alt="화면 캡처 2022-01-11 060119" src="https://user-images.githubusercontent.com/74360958/148838844-c63c5fc2-ce3d-497b-9a52-b4f5505689b6.png">

나뉘어진 data를 구글 드라이브에 업로드 후 colab에서 불러와 opencv의 adaptiveThreshold 함수를 이용해 후처리한다.

![p_6153](https://user-images.githubusercontent.com/74360958/148838045-fc1fcfa3-6e59-46e9-a5d3-40b9e9178437.png)
후처리 전

![148837559-dd89375b-f4fa-4bde-b676-a69c0339ff21](https://user-images.githubusercontent.com/74360958/148838379-854941d3-3378-4c95-aee4-8a10eab51b6e.png)
후처리 후

4. 모델 정의

```python
import tensorflow as tf

# act = "linear"
# act = "sigmoid"
# act = "tanh"
act = "relu"

# 3개의 층 128개의 노드
model1 = tf.keras.models.Sequential([
  # 28x28 입력층
  tf.keras.layers.Flatten(input_shape=(40, 28)),
  tf.keras.layers.Dense(128, activation=act),
  tf.keras.layers.Dense(128, activation=act),
  tf.keras.layers.Dense(128, activation=act),
  tf.keras.layers.Dense(23, activation="softmax")
])

opt = tf.keras.optimizers.Adam(learning_rate=0.005)
# opt = tf.keras.optimizers.RMSprop(learning_rate=0.01, momentum=0.1)

model1.compile(loss='categorical_crossentropy', optimizer = opt, metrics=['accuracy'])
```

5. 학습

```python
model1.fit(d_train, l_train_1hot, epochs = 50)
```

6. 테스트

이후 unlabeled test set에 대해서 test를 진행해보았다.

- 글자 1개에 대한 테스트

<img width="415" alt="image" src="https://user-images.githubusercontent.com/74360958/148839373-f40d9141-c254-4d90-84ec-d30016d6799c.png">

b를 정상적으로 b로 출력하고 있다.(왼쪽 하단)



- 전체 글자에 대한 테스트

![download](https://user-images.githubusercontent.com/74360958/148839662-c5e14c7b-813f-4ec1-9261-0addcd8cd18e.png)

ma5c라 적힌 이미지를 gray scale로 불러온 모습

![download](https://user-images.githubusercontent.com/74360958/148839707-855ed582-a941-4a99-b642-cf3dd716dae0.png)

opencv의 adaptiveThreshold 함수를 이용해 후처리 한 모습

<img width="498" alt="image" src="https://user-images.githubusercontent.com/74360958/148839800-f272cd1e-946b-4e4d-aef2-fa61c93f8239.png">

결과값으로 ma5c로 예측하는 모습이 보인다.(왼쪽 하단)


7. 결론

unlabelded data에 대해서 돌려본 정확도는 대략 70~80% 정도로 나왔다.
고정된 프레임으로 자르다보니 m과 n와 같이 가로로 긴 글자 중 잘릴 경우 비슷하게 나오는 글자에서 틀리는 경우가 많았다.

> 참고

[Building a Captcha OCR in TF2.0](https://www.kaggle.com/aakashnain/building-a-captcha-ocr-in-tf2-0) in Kaggle  
[20211_AI](https://github.com/bh2980/20211_AI)
