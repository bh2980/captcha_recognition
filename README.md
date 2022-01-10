# CAPTCHA(자동 입력 방지) 문자 인식

> 개요

자동 입력 방지 문자(CAPTCHA) 인식할 수 있는 딥러닝 모델 제작

> 프로젝트 순서

1. 데이터 수집
2. 데이터 라벨링
3. 데이터 가공
4. 프로그램 작성
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
해당 사진의 파일 이름을 보안코드로 바꿔주는 프로그램 작성 후 사용  

> 참고

[Building a Captcha OCR in TF2.0](https://www.kaggle.com/aakashnain/building-a-captcha-ocr-in-tf2-0) in Kaggle  
[20211_AI](https://github.com/bh2980/20211_AI)
