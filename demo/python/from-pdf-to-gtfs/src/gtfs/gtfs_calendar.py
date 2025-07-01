from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from .gtfs_entity import GtfsEntity


class GtfsServiceAvailability(Enum):
    """(Enum) Indicates whether the service operates in the date range specified by the `start_date` and `end_date` fields."""

    NO = 0
    """Service is not available in the date range."""
    YES = 1
    """Service is available in the date range."""


@dataclass
class GtfsCalendar(GtfsEntity):

    service_id: str
    """(Unique ID) Identifies a set of dates when service is available for one or more routes."""

    monday: GtfsServiceAvailability
    """(Enum) Indicates whether the service operates on all Mondays in the date range specified by the `start_date` and `end_date` fields."""

    tuesday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Tuesdays"""

    wednesday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Wednesdays"""

    thursday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Thursdays"""

    friday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Fridays"""

    saturday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Saturdays"""

    sunday: GtfsServiceAvailability
    """(Enum) Functions in the same way as monday except applies to Sundays"""

    start_date: datetime
    """(Date) Start service day for the service interval."""

    end_date: datetime
    """(Date) End service day for the service interval. This service day is included in the interval."""

    @staticmethod
    def file_stem() -> str:
        return 'calendar'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'service_id',
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
            'start_date',
            'end_date',
        )

    def __iter__(self):
        yield self.service_id
        yield str(self.monday.value)
        yield str(self.tuesday.value)
        yield str(self.wednesday.value)
        yield str(self.thursday.value)
        yield str(self.friday.value)
        yield str(self.saturday.value)
        yield str(self.sunday.value)
        yield f'{self.start_date.year:04}{self.start_date.month:02}{self.start_date.day:02}'
        yield f'{self.end_date.year:04}{self.end_date.month:02}{self.end_date.day:02}'

    def __hash__(self):
        return hash(self.service_id)
