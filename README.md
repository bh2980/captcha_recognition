CAPTCHA(자동 입력 방지) 문자 인식

> 참고

[OpenCV Word Segmenting on CAPTCHA Images](https://www.kaggle.com/fournierp/opencv-word-segmenting-on-captcha-images)

> 관련

[20211_AI](https://github.com/bh2980/20211_AI)

> 개요

경북대학교 수강신청 사이트의 자동 입력 방지 문자(CAPTCHA) 인식 프로그램 제작

> 프로젝트 순서

1. 데이터 수집
2. 공통 이미지 제외
3. 데이터 라벨링
4. 프로그램 작성
5. 학습
6. 테스트
7. 결론

> 사용 언어 및 라이브러리

- python 3.7.7
- selenium
- python-opencv

## 1. 데이터 수집

selenium 라이브러리를 통해서 경북대학교 수강신청 홈페이지에 17분마다 자동 로그인 후  
0.5초마다 새로고침하여 캡챠 이미지를 다운로드하는 이미지 다운봇 제작

## 2. 데이터 라벨링
