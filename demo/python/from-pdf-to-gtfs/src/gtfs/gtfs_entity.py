from abc import abstractmethod


class GtfsEntity:

    @staticmethod
    @abstractmethod
    def file_stem() -> str:
        pass

    @staticmethod
    @abstractmethod
    def field_names() -> tuple[str]:
        pass
