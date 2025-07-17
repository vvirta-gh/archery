import pytest
import pathlib
import tempfile
from datetime import datetime
from src.repositories.csv_score_repository import CSVScoreRepository
from src.models.score import Score

@pytest.fixture
def temp_csv_file(tmp_path: pathlib.Path) -> pathlib.Path:
    return tmp_path / 'test_scores.csv'


@pytest.fixture
def csv_repository(temp_csv_file: pathlib.Path) -> CSVScoreRepository:
    return CSVScoreRepository(temp_csv_file)


def test_save_score(csv_repository: CSVScoreRepository):
    score = Score(
        arrows=10,
        point_list=[10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
        points_total=100,
        distance=18.0,
        notes='Test score',
        date=datetime.now()
    )