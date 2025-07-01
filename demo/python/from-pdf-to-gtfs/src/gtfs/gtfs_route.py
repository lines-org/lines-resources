from dataclasses import dataclass
from enum import Enum
from typing import Optional

from .gtfs_entity import GtfsEntity


class GtfsRouteType(Enum):
    """(Enum) Indicates the type of transportation used on a route."""

    TRAM = 0
    """Tram, Streetcar, Light rail. Any light rail or street level system within a metropolitan area."""
    SUBWAY = 1
    """Subway, Metro. Any underground rail system within a metropolitan area."""
    RAIL = 2
    """Rail. Used for intercity or long-distance travel."""
    BUS = 3
    """Bus. Used for short- and long-distance bus routes."""
    FERRY = 4
    """Ferry. Used for short- and long-distance boat service."""
    CABLE_TRAM = 5
    """Cable tram. Used for street-level rail cars where the cable runs beneath the vehicle (e.g., cable car in San Francisco)."""
    AERIAL_LIFT = 6
    """Aerial lift, suspended cable car (e.g., gondola lift, aerial tramway). Cable transport where cabins, cars, gondolas or open chairs are suspended by means of one or more cables."""
    FUNICULAR = 7
    """Funicular. Any rail system designed for steep inclines."""
    TROLLEYBUS = 11
    """Trolleybus. Electric buses that draw power from overhead wires using poles."""
    MONORAIL = 12
    """Monorail. Railway in which the track consists of a single rail or a beam."""


@dataclass
class GtfsRoute(GtfsEntity):

    route_id: str
    """(Unique ID) Identifies a route."""

    agency_id: str
    """(ID) Agency for the specified route."""

    route_short_name: str
    """(Text) Short name of a route."""

    route_long_name: str
    """(Text) Full name of a route."""

    route_type: GtfsRouteType
    """(Enum) Indicates the type of transportation used on a route."""

    route_desc: Optional[str] = None
    """(Text) Description of a route that provides useful, quality information."""

    route_url: Optional[str] = None
    """(URL) URL of a web page about the particular route."""

    route_color: Optional[str] = None
    """(Color) Route color designation that matches public facing material."""

    route_text_color: Optional[str] = None
    """(Color) Legible color to use for text drawn against a background of `route_color`."""

    @staticmethod
    def file_stem() -> str:
        return 'routes'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'route_id',
            'agency_id',
            'route_short_name',
            'route_long_name',
            'route_type',
            'route_desc',
            'route_url',
            'route_color',
            'route_text_color',
        )

    def __iter__(self):
        yield self.route_id
        yield self.agency_id
        yield self.route_short_name
        yield self.route_long_name
        yield str(self.route_type.value)
        yield self.route_desc if self.route_desc is not None else ''
        yield self.route_url if self.route_url is not None else ''
        yield self.route_color if self.route_color is not None else ''
        yield self.route_text_color if self.route_text_color is not None else ''

    def __hash__(self):
        return hash(self.route_id)
