from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .gtfs_entity import GtfsEntity


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


@dataclass
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

    @staticmethod
    def file_stem() -> str:
        return 'stops'

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

    def __iter__(self):
        yield self.stop_id
        yield self.stop_name
        yield str(self.stop_lat)
        yield str(self.stop_lon)
        yield self.stop_code if self.stop_code is not None else ''
        yield self.zone_id if self.zone_id is not None else ''
        yield self.stop_url if self.stop_url is not None else ''
        yield str(self.location_type.value)

    def __hash__(self):
        return hash(self.stop_id)
