from datetime import datetime
from time import strftime
from time import gmtime


class BusGetter:
    @staticmethod
    def _get_seconds_from_string(t: str):
        hours, minutes = t.split(":")
        return int(hours) * 3600 + int(minutes) * 60

    @staticmethod
    def _get_today_in_seconds():
        today = datetime.today()
        return today.hour * 3600 + today.minute * 60

    @staticmethod
    def _convert_seconds_to_schedule(seconds: list[int]):
        return [strftime("%H:%M", gmtime(t)) for t in seconds]

    @classmethod
    def _convert_times_to_seconds(cls, times: list[str]):
        return [cls._get_seconds_from_string(t) for t in times]

    @classmethod
    def get_next_three_bus(cls, times: list[str], now=None):
        if now is None:
            now = cls._get_today_in_seconds()
        schedule = cls._convert_times_to_seconds(times)
        next_three = []
        for i in range(len(schedule) - 1):
            if schedule[i] < now <= schedule[i + 1]:
                next_three = schedule[i+1:i+4]
        return cls._convert_seconds_to_schedule(next_three)
