from pathlib import Path

from .gtfs_entity import GtfsEntity


class GtfsCsvWriter:

    def __init__(self, directory_path: Path | str):
        self._directory_path = Path(directory_path)

    @property
    def directory_path(self) -> Path:
        return self._directory_path

    def write(self, *gtfs_entities: GtfsEntity):
        gtfs_entity_type = type(gtfs_entities[0])

        file_name = gtfs_entity_type.file_stem() + '.txt'
        field_names = gtfs_entity_type.field_names()

        self.directory_path.mkdir(parents=True, exist_ok=True)
        with open(self.directory_path / file_name, 'w') as f:
            f.write(','.join(field_names) + '\n')
            for gtfs_entity in gtfs_entities:
                f.write(','.join(list(gtfs_entity)) + '\n')
