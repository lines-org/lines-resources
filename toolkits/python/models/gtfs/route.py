from enum import Enum
from typing import Optional

from pydantic import ValidationError

from .entity import GtfsEntity


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

    @property
    def id(self) -> str:
        return self.route_id

    @staticmethod
    def from_dict(data):
        try:
            return GtfsRoute(
                route_id=data.get('route_id'),
                agency_id=data.get('agency_id'),
                route_short_name=data.get('route_short_name'),
                route_long_name=data.get('route_long_name'),
                route_type=GtfsRouteType(int(data.get('route_type'))),
                route_desc=data.get('route_desc'),
                route_url=data.get('route_url'),
                route_color=data.get('route_color'),
                route_text_color=data.get('route_text_color'),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

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
        
    def field_values(self) -> tuple[str]:
        return (
            self.route_id,
            self.agency_id,
            self.route_short_name,
            self.route_long_name,
            str(self.route_type.value),
            self.route_desc if self.route_desc is not None else '',
            self.route_url if self.route_url is not None else '',
            self.route_color if self.route_color is not None else '',
            self.route_text_color if self.route_text_color is not None else '',
        )
