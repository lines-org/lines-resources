from datetime import timedelta

from pydantic import ValidationError

from .entity import GtfsEntity


class GtfsStopTime(GtfsEntity):

    trip_id: str
    """(Foreign ID referencing `trips.trip_id`) Identifies a trip."""

    arrival_time: timedelta
    """(Time) Arrival time at the stop (defined by `stop_times.stop_id`) for a specific trip (defined by `stop_times.trip_id`) in the time zone specified by `agency.agency_timezone`, not `stops.stop_timezone`."""

    departure_time: timedelta
    """(Time) Departure time from the stop (defined by `stop_times.stop_id`) for a specific trip (defined by `stop_times.trip_id`) in the time zone specified by `agency.agency_timezone`, not `stops.stop_timezone`."""

    stop_id: str
    """(Foreign ID referencing `stops.stop_id`) Identifies the serviced stop."""

    stop_sequence: int
    """(Non-negative integer) Order of stops, location groups, or GeoJSON locations for a particular trip."""

    @property
    def id(self) -> str:
        return f'{self.trip_id}:{self.stop_id}:{self.stop_sequence}'

    @staticmethod
    def from_dict(data):
        try:
            hours, minutes, seconds = map(int, data.get('arrival_time').split(':'))
            arrival_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            hours, minutes, seconds = map(int, data.get('departure_time').split(':'))
            departure_time = timedelta(hours=hours, minutes=minutes, seconds=seconds)
            return GtfsStopTime(
                trip_id=data.get('trip_id'),
                arrival_time=arrival_time,
                departure_time=departure_time,
                stop_id=data.get('stop_id'),
                stop_sequence=int(data.get('stop_sequence')),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'trip_id',
            'arrival_time',
            'departure_time',
            'stop_id',
            'stop_sequence',
        )

    def field_values(self) -> tuple[str]:
        total_seconds = int(self.arrival_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        arrival_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        total_seconds = int(self.departure_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        departure_time = f'{hours:02d}:{minutes:02d}:{seconds:02d}'

        return (
            self.trip_id,
            arrival_time,
            departure_time,
            self.stop_id,
            str(self.stop_sequence),
        )
