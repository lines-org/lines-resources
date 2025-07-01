from abc import abstractmethod

from pydantic import BaseModel


class GtfsEntity(BaseModel):

    @property
    @abstractmethod
    def id(self) -> str:
        pass

    def __hash__(self):
        return hash(self.id)

    @staticmethod
    @abstractmethod
    def from_dict(data: dict) -> 'GtfsEntity':
        pass

    @staticmethod
    @abstractmethod
    def field_names() -> tuple[str]:
        pass

    @abstractmethod
    def field_values(self) -> tuple[str]:
        pass
