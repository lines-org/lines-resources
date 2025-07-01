from enum import Enum
from typing import Optional

from pydantic import ValidationError

from .entity import GtfsEntity


class GtfsLocationType(Enum):
    """(Enum) Location type."""

    STOP = 0
    """Stop (or Platform). A location where passengers board or disembark from a transit vehicle. Is called a platform when defined within a `parent_station`."""
    STATION = 1
    """Station. A physical structure or area that contains one or more platform."""
    ENTRANCE_EXIT = 2
    """Entrance/Exit. A location where passengers can enter or exit a station from the street. If an entrance/exit belongs to multiple stations, it may be linked by pathways to both, but the data provider must pick one of them as parent."""
    GENERIC_NODE = 3
    """Generic Node. A location within a station, not matching any other `location_type`, that may be used to link together pathways define in `pathways.txt`."""
    BOARDING_AREA = 4
    """Boarding Area. A specific location on a platform, where passengers can board and/or alight vehicles."""


class GtfsStop(GtfsEntity):

    stop_id: str
    """(Unique ID) Identifies a location: stop/platform, station, entrance/exit, generic node or boarding area."""

    stop_name: str
    """(Text) Name of the location."""

    stop_lat: float
    """(Latitude) Latitude of the location."""

    stop_lon: float
    """(Longitude) Longitude of the location."""

    stop_code: Optional[str] = None
    """(Text) Short text or a number that identifies the location for riders."""

    zone_id: Optional[str] = None
    """(ID) Identifies the fare zone for a stop."""

    stop_url: Optional[str] = None
    """(URL) URL of a web page about the location."""

    location_type: GtfsLocationType = GtfsLocationType.STOP
    """(Enum) Location type."""

    @property
    def id(self) -> str:
        return self.stop_id

    @staticmethod
    def from_dict(data):
        try:
            return GtfsStop(
                stop_id=data.get('stop_id'),
                stop_name=data.get('stop_name'),
                stop_lat=float(data.get('stop_lat')),
                stop_lon=float(data.get('stop_lon')),
                stop_code=data.get('stop_code'),
                zone_id=data.get('zone_id'),
                stop_url=data.get('stop_url'),
                location_type=GtfsLocationType(int(data.get('location_type'))),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'stop_id',
            'stop_name',
            'stop_lat',
            'stop_lon',
            'stop_code',
            'zone_id',
            'stop_url',
            'location_type',
        )

    def field_values(self) -> tuple[str]:
        return (
            self.stop_id,
            self.stop_name,
            str(self.stop_lat),
            str(self.stop_lon),
            self.stop_code if self.stop_code is not None else '',
            self.zone_id if self.zone_id is not None else '',
            self.stop_url if self.stop_url is not None else '',
            str(self.location_type.value),
        )
