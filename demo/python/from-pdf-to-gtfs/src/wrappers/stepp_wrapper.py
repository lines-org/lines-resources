import geopandas as gpd
import pandas as pd
import zipfile

from pathlib import Path


class SteppWrapper:

    def __init__(self, file_path: Path | str):
        self._file_path = Path(file_path)

    @property
    def file_path(self) -> Path:
        return self._file_path

    def get_data(self) -> dict[str, pd.DataFrame | gpd.GeoDataFrame]:
        # Extract database from zipped file
        extract_path = self.file_path.parent / self.file_path.stem
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        # Construct path to database
        gdb_path = extract_path / 'dados' / 'dados.gdb'
        # Load layers from database
        circulacoes = gpd.read_file(gdb_path, layer='circulacoes')
        paragens = gpd.read_file(gdb_path, layer='paragens')
        segmentos = gpd.read_file(gdb_path, layer='segmentos')
        servicos = gpd.read_file(gdb_path, layer='servicos')
        # Convert coordinates to ESPG:4326
        paragens.to_crs(epsg=4326, inplace=True)
        segmentos.to_crs(epsg=4326, inplace=True)
        return {
            'circulacoes': circulacoes,
            'paragens': paragens,
            'segmentos': segmentos,
            'servicos': servicos,
        }
