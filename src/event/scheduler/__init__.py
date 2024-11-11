from __future__ import annotations

from asyncio import run

from apscheduler import Scheduler as Apscheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.event.scheduler.email_broadcast import tick


class Scheduler:
    def start():
        scheduler = Apscheduler()
        scheduler.add_schedule(tick, IntervalTrigger(seconds=1), id="tick")
        scheduler.start_in_background()
            