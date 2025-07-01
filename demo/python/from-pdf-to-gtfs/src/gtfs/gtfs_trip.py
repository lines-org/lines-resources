from dataclasses import dataclass

from .gtfs_entity import GtfsEntity


@dataclass
class GtfsTrip(GtfsEntity):

    route_id: str
    """(Foreign ID referencing `routes.route_id`) Identifies a route."""

    service_id: str
    """(Foreign ID referencing `calendar.service_id` or `calendar_dates.service_id`) Identifies a set of dates when service is available for one or more routes."""

    trip_id: str
    """(Unique ID) Identifies a trip."""

    @staticmethod
    def file_stem() -> str:
        return 'trips'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'route_id',
            'service_id',
            'trip_id',
        )

    def __iter__(self):
        yield self.route_id
        yield self.service_id
        yield self.trip_id

    def __hash__(self):
        return hash(self.trip_id)
