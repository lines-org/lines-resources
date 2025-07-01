from datetime import datetime
from enum import Enum

from pydantic import ValidationError

from .entity import GtfsEntity


class GtfsServiceAvailability(Enum):
    """(Enum) Indicates whether the service operates in the date range specified by the `start_date` and `end_date` fields."""

    NO = 0
    """Service is not available in the date range."""
    YES = 1
    """Service is available in the date range."""


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

    @property
    def id(self) -> str:
        return self.service_id

    @staticmethod
    def from_dict(data):
        try:
            return GtfsCalendar(
                service_id=data.get('service_id'),
                monday=GtfsServiceAvailability(int(data.get('monday'))),
                tuesday=GtfsServiceAvailability(int(data.get('tuesday'))),
                wednesday=GtfsServiceAvailability(int(data.get('wednesday'))),
                thursday=GtfsServiceAvailability(int(data.get('thursday'))),
                friday=GtfsServiceAvailability(int(data.get('friday'))),
                saturday=GtfsServiceAvailability(int(data.get('saturday'))),
                sunday=GtfsServiceAvailability(int(data.get('sunday'))),
                start_date=datetime.strptime(data.get('start_date'), '%Y%m%d'),
                end_date=datetime.strptime(data.get('end_date'), '%Y%m%d'),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

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

    def field_values(self) -> tuple[str]:
        return (
            self.service_id,
            str(self.monday.value),
            str(self.tuesday.value),
            str(self.wednesday.value),
            str(self.thursday.value),
            str(self.friday.value),
            str(self.saturday.value),
            str(self.sunday.value),
            f'{self.start_date.year:04}{self.start_date.month:02}{self.start_date.day:02}',
            f'{self.end_date.year:04}{self.end_date.month:02}{self.end_date.day:02}',
        )
