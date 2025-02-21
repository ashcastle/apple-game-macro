🇺🇸 [Apple Game](README_us.md)

🇯🇵 [Apple Game](README_jp.md)

# 🍎 사과게임 매크로 (Apple Game Macro)

맥북 레티나 디스플레이 기준으로 작성된 사과게임 자동화 매크로입니다.
[사과게임 링크](https://www.gamesaien.com/game/fruit_box_a/)

> 이 프로젝트는 순수하게 교육 및 학습 목적으로 제작되었습니다. 실제 게임에서의 매크로 사용은 게임 이용약관에 위배될 수 있으며, 제작자는 이로 인한 어떠한 책임도 지지 않습니다.

## 🚀 설치 방법

1. Python 가상환경 생성 및 활성화

~~~zsh
python -m venv venv
source venv/bin/activate
~~~

2. 필요한 패키지 설치

~~~zsh
pip install -r requirements.txt
~~~

## 🎮 실행 방법
1. 게임 화면을 띄운 상태에서 아래 명령어로 매크로 실행

~~~zsh
python apple_game_solver.py
~~~

## ✨ 주요 기능

- 🔢 화면에서 1-9까지의 숫자(사과) 자동 인식
- 🎯 합이 10이 되는 조합을 찾아 자동으로 드래그
- 📏 수평/수직 라인 및 사각형 영역 내 유효한 조합 탐색
- 🖥️ 레티나 디스플레이 해상도 자동 보정
- 🔄 연속된 2개 이상의 숫자 조합 자동 탐지
- ➕ 사각형 영역 내 숫자 합 계산

## ⚠️ 참고사항

- 💻 MacBook 레티나 디스플레이에 최적화
- 🔧 다른 환경에서 사용 시 좌표값 조정 필요
- ⌨️ 게임 실행 중 매크로를 종료하려면 Ctrl+C
- 🎯 실행 전 게임 화면이 활성화되어 있어야 함
- ⏱️ 3초 간격으로 새로운 스캔 수행
