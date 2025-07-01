from dataclasses import dataclass
from datetime import timedelta

from .gtfs_entity import GtfsEntity


@dataclass
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

    @staticmethod
    def file_stem() -> str:
        return 'stop_times'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'trip_id',
            'arrival_time',
            'departure_time',
            'stop_id',
            'stop_sequence',
        )

    def __iter__(self):
        yield self.trip_id
        total_seconds = int(self.arrival_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        yield f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        total_seconds = int(self.departure_time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        yield f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        yield self.stop_id
        yield str(self.stop_sequence)

    def __hash__(self):
        return hash((self.trip_id, self.stop_id, self.stop_sequence))
