from src.repositories.score_repository import ScoreRepository
from src.models.score import Score
from loguru import logger
import pathlib
import csv
from typing import List, Optional
from datetime import datetime



class CSVScoreRepository(ScoreRepository):
    def __init__(self, file_path: pathlib.Path) -> None:
        self.file_path = file_path
        if not self.file_path.exists():
            self.file_path.touch()
            # Lisätään otsikkorivi
            with open(self.file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['id',' arrows', 'point_list', 'points_total', 'distance', 'note', 'date'])


    def _get_next_id(self) -> int:
        scores = self.get_all()
        if not scores:
            return 1
        return max(score.id for score in scores if score.id is not None)
    

    def save(self, score: Score) -> None:
        if not hasattr(score, 'id') or score.id is None:
            score.id = self._get_next_id()
        
        with open(self.file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                score.id,
                score.arrows,
                str(score.point_list),
                score.points_total,
                score.distance,
                score.notes,
                score.date.strftime('%Y-%m-%d %H:%M:%S')
            ])
        logger.debug('Score saved to CSV: {}', score)

    def get_all(self) -> List[Score]:
        scores = []
        with open(self.file_path, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Ohitetaan header
            for row in reader:
                score = Score(
                    id=int(row[0]),
                    arrows=int(row[1] if row[1] != '' else 10),
                    point_list=[int(x) for x in row[2].strip('[]').split(',') if x.strip()],
                    points_total=int(row[3]),
                    distance=float(row[4]),
                    notes=row[5] if row[5] != 'None' else None,
                    date=datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S')
                )
                scores.append(score)
        return scores

    def get_by_date(self, date: datetime) -> Optional[Score]:
        scores = self.get_all()
        for score in scores:
            if score.date.date() == date.date():
                return score
        return None


    def get_by_id(self, id: int) -> Optional[Score]:
        scores = self.get_all()
        for score in scores:
            if score.id == id:
                return score
        return None


    def delete(self, id: int) -> None:
        scores = self.get_all()
        scores = [score for score in scores if score.id != id]

        with open(self.file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id',' arrows', 'point_list', 'points_total', 'distance', 'note', 'date'])
            for score in scores:
                writer.writerow([
                    score.id,
                    score.arrows,
                    str(score.point_list),
                    score.points_total,
                    score.distance,
                    score.notes,
                    score.date.strftime('%Y-%m-%d %H:%M:%S')
                ])
        logger.debug('Score deleted from CSV: {}', id)
    
    

if __name__ == "__main__":
    pass