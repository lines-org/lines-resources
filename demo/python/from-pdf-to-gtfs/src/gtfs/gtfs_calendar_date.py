from dataclasses import dataclass
from enum import Enum

from .gtfs_entity import GtfsEntity


class GtfsExceptionType(Enum):
    """(Enum) Indicates whether service is available on the date specified in the date field."""

    ADDED = 1
    """Service has been added for the specified date."""
    REMOVED = 2
    """Service has been removed for the specified date."""


@dataclass
class GtfsCalendarDate(GtfsEntity):

    service_id: str
    """(Foreign ID referencing `calendar.service_id` or ID) Identifies a set of dates when a service exception occurs for one or more routes."""

    date: str
    """(Date) Date when service exception occurs."""

    exception_type: GtfsExceptionType
    """Indicates whether service is available on the date specified in the date field."""

    @staticmethod
    def file_stem() -> str:
        return 'calendar_dates'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'service_id',
            'date',
            'exception_type',
        )

    def __iter__(self):
        yield self.service_id
        yield self.date
        yield str(self.exception_type.value)

    def __hash__(self):
        return hash((self.service_id, self.date))
