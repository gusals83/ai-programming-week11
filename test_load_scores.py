import pytest
from load_scores import load_scores
from helpers import 쓰기


# 정상 ①
def test_정상_파일을_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert len(kept) == 5
    assert len(skipped) == 5


# 정상 ③
def test_이름에_쉼표가_있어도_읽는다():
    kept, skipped = load_scores("scores.csv")
    assert ("최,네번", 77) in kept


# 예외 ①
def test_없는_파일이면_오류가_난다():
    with pytest.raises(FileNotFoundError):
        load_scores("없는파일.csv")


# 예외 ②
def test_헤더만_있으면_빈_결과():
    kept, skipped = load_scores("empty.csv")
    assert kept == []
    assert skipped == []


# 경계 ①②③
@pytest.mark.parametrize("점수, 유효한가", [
    (-1, False),   # 경계 바로 아래
    (0, True),     # 아래쪽 경계
    (1, True),
    (99, True),
    (100, True),   # 위쪽 경계
    (101, False),  # 경계 바로 위
])
def test_점수_경계값(점수, 유효한가):
    쓰기("임시.csv", 점수)
    kept, skipped = load_scores("임시.csv")
    assert (len(kept) == 1) == 유효한가


# 정상 ②
def test_빈_줄은_건너뛴다(tmp_path):
    파일 = tmp_path / "빈줄.csv"
    파일.write_text("name,score\n김하나,88\n\n박둘,77\n\n", encoding="utf-8")
    kept, skipped = load_scores(str(파일))
    assert kept == [("김하나", 88), ("박둘", 77)]


    # 커버리지 보강: 이름이 빈 줄 (load_scores.py 55~56번 줄)
def test_이름이_비면_건너뛴다():
    kept, skipped = load_scores("weird.csv")
    assert (2, ",90", "이름이 비어 있음") in skipped
    assert kept == [("한겨울", 77), ("윤보람", 88)]