from abc import ABC, abstractmethod
from typing import List
from src.models.score import Score
from datetime import datetime
from loguru import logger

class ScoreRepository(ABC):
    @abstractmethod
    def save(self, score: Score) -> None:
        pass  # Ei toteutusta abstraktissa metodissa

    @abstractmethod
    def get_all(self) -> List[Score]:
        pass

    @abstractmethod
    def get_by_date(self, date: datetime) -> List[Score]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Score:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass