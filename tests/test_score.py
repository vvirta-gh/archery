from src.models.score import Score
import pytest

@pytest.fixture
def score():
    return Score(arrows=2, point_list=[8, 7])

def test_score_init(score):
    assert score.arrows == 2
    assert score.point_list == [8, 7]

def test_score_get_average(score):
    assert score.get_average() == 7.5

def test_score_create_with_random_points():
    score = Score.create_with_random_points(arrows=10)
    assert score.arrows == 10
    assert len(score.point_list) == 10
    assert score.points_total == sum(score.point_list)