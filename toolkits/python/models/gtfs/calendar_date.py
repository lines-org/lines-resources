from enum import Enum

from pydantic import ValidationError

from .entity import GtfsEntity


class GtfsExceptionType(Enum):
    """(Enum) Indicates whether service is available on the date specified in the date field."""

    ADDED = 1
    """Service has been added for the specified date."""
    REMOVED = 2
    """Service has been removed for the specified date."""


class GtfsCalendarDate(GtfsEntity):

    service_id: str
    """(Foreign ID referencing `calendar.service_id` or ID) Identifies a set of dates when a service exception occurs for one or more routes."""

    date: str
    """(Date) Date when service exception occurs."""

    exception_type: GtfsExceptionType
    """Indicates whether service is available on the date specified in the date field."""

    @property
    def id(self) -> str:
        return f'{self.service_id}:{self.date}'

    @staticmethod
    def from_dict(data):
        try:
            return GtfsCalendarDate(
                service_id=data.get('service_id'),
                date=data.get('date'),
                exception_type=GtfsExceptionType(int(data.get('exception_type'))),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'service_id',
            'date',
            'exception_type',
        )

    def field_values(self) -> tuple[str]:
        return (
            self.service_id,
            self.date,
            str(self.exception_type.value),
        )
