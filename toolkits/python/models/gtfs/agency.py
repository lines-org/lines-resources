from typing import Optional

from pydantic import ValidationError

from .entity import GtfsEntity


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

    @property
    def id(self) -> str:
        return self.agency_id

    @staticmethod
    def from_dict(data):
        try:
            return GtfsAgency(
                agency_id=data.get('agency_id'),
                agency_name=data.get('agency_name'),
                agency_url=data.get('agency_url'),
                agency_timezone=data.get('agency_timezone'),
                agency_lang=data.get('agency_lang'),
            )
        except ValidationError as e:
            raise ValidationError(f'Invalid data provided: {e.errors()}')
        except Exception as e:
            raise Exception(f'Invalid data provided: {e}')

    @staticmethod
    def field_names() -> tuple[str]:
        return (
            'agency_id',
            'agency_name',
            'agency_url',
            'agency_timezone',
            'agency_lang',
        )

    def field_values(self) -> tuple[str]:
        return (
            self.agency_id,
            self.agency_name,
            self.agency_url,
            self.agency_timezone,
            self.agency_lang if self.agency_lang is not None else '',
        )
