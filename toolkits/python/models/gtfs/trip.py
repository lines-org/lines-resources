from pydantic import ValidationError

from .entity import GtfsEntity


class GtfsTrip(GtfsEntity):

    route_id: str
    """(Foreign ID referencing `routes.route_id`) Identifies a route."""

    service_id: str
    """(Foreign ID referencing `calendar.service_id` or `calendar_dates.service_id`) Identifies a set of dates when service is available for one or more routes."""

    trip_id: str
    """(Unique ID) Identifies a trip."""

    @property
    def id(self) -> str:
        return self.trip_id

    @staticmethod
    def from_dict(data):
        try:
            return GtfsTrip(
                route_id=data.get('route_id'),
                service_id=data.get('service_id'),
                trip_id=data.get('trip_id'),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'route_id',
            'service_id',
            'trip_id',
        )

    def field_values(self) -> tuple[str]:
        return (
            self.route_id,
            self.service_id,
            self.trip_id,
        )
