from dataclasses import dataclass
from typing import Optional

from .gtfs_entity import GtfsEntity


@dataclass
class GtfsAgency(GtfsEntity):

    agency_id: str
    """(Unique ID) Identifies a transit brand which is often synonymous with a transit agency."""

    agency_name: str
    """(Text) Full name of the transit agency."""

    agency_url: str
    """(URL) URL of the transit agency."""

    agency_timezone: str
    """(Timezone) Timezone where the transit agency is located."""

    agency_lang: Optional[str] = None
    """(Language) Primary language used by this transit agency."""

    @staticmethod
    def file_stem() -> str:
        return 'agency'

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'agency_id',
            'agency_name',
            'agency_url',
            'agency_timezone',
            'agency_lang',
        )

    def __iter__(self):
        yield self.agency_id
        yield self.agency_name
        yield self.agency_url
        yield self.agency_timezone
        yield self.agency_lang if self.agency_lang is not None else ''

    def __hash__(self):
        return hash(self.agency_id)
