from typing import List

from classes.period_schedule import PeriodSchedule


class Timetable:
    def __init__(self, period_schedules: List[PeriodSchedule]):
        self.period_schedules = period_schedules

    def __str__(self):
        period_schedules: List[str] = ", ".join([f"{period_schedule}" for period_schedule in self.period_schedules])
        return f"Period schedules: {period_schedules}"