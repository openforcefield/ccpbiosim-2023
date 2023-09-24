import pathlib

from importlib_metadata import entry_points


def get_force_field_origin(force_field: str):
    for entry_point in entry_points().select(
        group="openforcefield.smirnoff_forcefield_directory",
    ):
        loaded = entry_point.load()()

        assert len(loaded) == 1
        if "openforcefields" in loaded[0]:
            file = pathlib.Path(loaded[0]) / force_field
            if file.is_file():
                return file
