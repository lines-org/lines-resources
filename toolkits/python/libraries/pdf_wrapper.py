import fitz
import pdfplumber
import pdfplumber.display

from pathlib import Path
from typing import Literal


class PdfWrapper:

    def __init__(self, file_path: Path | str):
        self._file_path = Path(file_path)
        self._MM_IN_PT = 2.83465

    @property
    def file_path(self) -> Path:
        return self._file_path

    @property
    def MM_IN_PT(self) -> float:
        return self._MM_IN_PT

    def __get_rotate_path(
        self,
        rotation: Literal[0, 90, 180, 270],
    ) -> str:
        if rotation == 0:
            return self.file_path
        rot_path = self.file_path.parent / f'{self.file_path.stem}.{rotation}.pdf'
        if rot_path.exists():
            return rot_path
        with fitz.open(self.file_path) as pdf:
            for page in pdf:
                page.set_rotation(rotation)
            pdf.save(rot_path)
        return rot_path

    def __get_bbox(
        self,
        bbox: dict[Literal['left', 'top', 'right', 'bottom'], float],
        bbox_units: Literal['pt', 'mm'],
        page_width: float,
        page_height: float,
    ) -> tuple[float, float, float, float]:
        scaler = 1
        if bbox_units == 'mm':
            scaler = self.MM_IN_PT
        res_bbox = (
            scaler * bbox['left'],
            scaler * bbox['top'],
            page_width - scaler * bbox['right'],
            page_height - scaler * bbox['bottom'],
        )
        return res_bbox

    def debug_table_detection(
        self,
        page_index: int,
        page_rotation: Literal[0, 90, 180, 270],
        bbox: tuple[float, float, float, float],
        bbox_units: Literal['pt', 'mm'],
        table_settings: dict[str, any],
    ) -> pdfplumber.display.PageImage:
        file_path = self.__get_rotate_path(page_rotation)
        with pdfplumber.open(file_path) as pdf:
            page = pdf.pages[page_index]
            page = page.crop(self.__get_bbox(bbox, bbox_units, page.width, page.height))
            image = page.to_image().debug_tablefinder(table_settings)
        return image

    def get_tables(
        self,
        page_index: int,
        page_rotation: Literal[0, 90, 180, 270],
        bbox: tuple[float, float, float, float],
        bbox_units: Literal['pt', 'mm'],
        table_settings: dict[str, any],
    ) -> list[list[str | None]]:
        file_path = self.__get_rotate_path(page_rotation)
        with pdfplumber.open(file_path) as pdf:
            page = pdf.pages[page_index]
            page = page.crop(self.__get_bbox(bbox, bbox_units, page.width, page.height))
            tables = page.extract_tables(table_settings)
        return tables
