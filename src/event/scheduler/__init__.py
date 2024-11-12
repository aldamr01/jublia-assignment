from __future__ import annotations

from asyncio import run

from apscheduler import Scheduler as Apscheduler
from apscheduler.triggers.interval import IntervalTrigger

from src.event.scheduler.email_broadcast import main as eb_main


class Scheduler:
    def start():
        scheduler = Apscheduler()
        scheduler.add_schedule(
            eb_main, IntervalTrigger(seconds=60), id="event-broadcast-scheduler"
        )
        scheduler.start_in_background()
