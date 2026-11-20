# 성적 CSV 읽기 프로그램 (load_scores)

## ① 무엇을 하나요 (What)
성적 CSV 파일을 읽어 0~100점 사이의 올바른 점수만 골라 내고, 잘못된 줄은 줄 번호와 이유를 함께 따로 모아 주는 프로그램입니다.

## ② 왜 만들었나요 (Why)
실제 성적 파일은 깨끗하지 않습니다. 평범해 보였던 scores.csv에도 105점처럼 범위를 벗어난 점수와 칸 수가 맞지 않는 줄이 5줄이나 섞여 있었고, weird.csv에는 이름이 빈 줄, 점수가 빈 줄, 1000점, -100점, 88.5점, "7 2" 같은 값이 들어 있었습니다.
이런 파일을 그냥 읽으면 프로그램이 오류로 멈추거나, 잘못된 점수가 평균 같은 분석 결과에 그대로 섞입니다.
데이터를 분석하기 전에 "믿을 수 있는 줄"과 "버려야 할 줄"을 먼저 나눠 두려고 만들었습니다.

## ③ 어떻게 쓰나요 (How)
Python 3가 설치되어 있으면 추가로 설치할 것 없이 실행됩니다.

```
git clone https://github.com/gusals83/ai-programming-week11.git
cd ai-programming-week11
python load_scores.py scores.csv
```

실행하면 읽어 들인 학생과 건너뛴 줄(줄 번호와 이유)이 화면에 출력됩니다.
다른 파일을 읽으려면 `scores.csv` 자리에 파일 이름을 바꿔 넣으면 됩니다.

코드 안에서 쓸 때는 이렇게 부릅니다.

```python
from load_scores import load_scores
kept, skipped = load_scores("scores.csv")
# kept    : [(이름, 점수), ...]           올바른 줄
# skipped : [(줄 번호, 원본 줄, 이유), ...] 건너뛴 줄
```

## ④ 어떻게 테스트하나요
```
python -m pip install pytest pytest-cov
python -m pytest
```

통과 화면:
```
collected 12 items

test_load_scores.py ............                  [100%]

12 passed
```

커버리지까지 보려면:
```
python -m pytest --cov=load_scores --cov-report=term-missing
```
커버리지는 80%입니다. 남은 77~86번 줄은 파일을 직접 실행할 때만 도는 출력 부분이라 pytest로는 지나가지 않습니다.

## ⑤ 파일 구성
| 파일 | 하는 일 |
|---|---|
| load_scores.py | 성적 CSV를 읽어 올바른 줄(kept)과 건너뛴 줄(skipped)로 나누는 프로그램 |
| test_load_scores.py | 정상·예외·경계값 테스트 (함수 7개, 12번 실행) |
| helpers.py | 경계값 테스트에서 점수 한 줄짜리 임시 파일을 만드는 도우미 함수 |
| scores.csv | 정상 5줄과 잘못된 5줄이 섞인 예시 성적 파일 |
| empty.csv | 헤더만 있는 파일 (예외 테스트용) |
| weird.csv | 이름 빈 칸, 점수 빈 칸, 범위 밖 점수 등이 모인 파일 (커버리지 보강용) |
| LICENSE | MIT 라이선스 |

## ⑥ 만든 사람
- 박현민 2026101024 · 경영학부 데이터경영전공
- AI를 어디에 썼는지
  - 학교 AI 챗봇: pytest 테스트 코드 작성 방법, git 사용 순서, README 초안 정리에 도움을 받음 (커밋에 Assisted-by로 표기)
  - VS Code Copilot: pytest 실행 경로(PATH) 설정
  - 테스트 케이스 설계표는 코드를 보지 않고 명세만 보고 직접 작성함
  - Why 칸은 직접 겪은 내용을 바탕으로 작성함