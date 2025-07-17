from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from loguru import logger
import random

class Score(BaseModel):
    id: Optional[int] = None 
    arrows: int | None = Field(ge=1, le=10)
    point_list:list[int] = Field(default_factory=list)
    points_total: int = Field(ge=0, le=120, default=0)  # Lisää default
    distance: float = Field(ge=7, le=30, default=18.0)  # Lisää default
    notes: Optional[str] = Field(max_length=100, default=None)  # Lisää default
    date: datetime = Field(default_factory=datetime.now)


    def get_average(self) -> float:
        if not self.point_list:
            return 0.0
        return sum(self.point_list) / len(self.point_list)
    

    @classmethod
    def generate_random_shooting_points(cls, num_arrows: int = 10) -> list[int]:
        return [random.randint(0, 12) for _ in range(num_arrows)]

    
    @classmethod
    def create_with_random_points(cls, arrows: int = 10, **kwargs) -> 'Score':
        """Luo Score-objekti satunnaisilla pisteillä"""
        point_list = cls.generate_random_shooting_points(arrows)
        points_total = sum(point_list)
        return cls(
            arrows=arrows,
            point_list=point_list,
            points_total=points_total,
            **kwargs
        )

if __name__ == "__main__":
    pass