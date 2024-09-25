from typing import List
from classes.day_of_week import DayOfWeek
from classes.period import Period


class PeriodSchedule:
    """
    pub id: i32,
    pub day_of_week: DayOfWeek,
    pub number_of_periods: i32,
    pub periods: Vec<Period>,
    """
    def __init__(self, id: int, day_of_week: DayOfWeek, number_of_periods: int, periods: List[Period]):
        self.id = id
        self.day_of_week = day_of_week
        self.number_of_periods = number_of_periods
        self.periods = periods

    def __str__(self):
        return f"Id: {self.id}, Day Of Week: {self.day_of_week}, Number of Periods: {self.number_of_periods}"