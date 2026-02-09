import typer

from typing_extensions import Annotated
from enum import Enum
from pathlib import Path
from .structs import orientation_types, map_types
from .structs.hexmap import RectHexMap, CircularHexMap

cli = typer.Typer(add_completion=False, rich_markup_mode="rich", no_args_is_help=True)


@cli.command()
def map(
    type: Annotated[map_types, typer.Argument()],
    output: Annotated[
        Path | None,
        typer.Option(
            "--output", "-o", help="Output file", file_okay=True, writable=True
        ),
    ] = None,
    png_output: Annotated[
        Path | None,
        typer.Option(
            "--png-output", "-p", help="PNG output file", file_okay=True, writable=True
        ),
    ] = None,
    radius: Annotated[
        int, typer.Option("--radius", "-r", help="Radius for hex map")
    ] = 1,
    width: Annotated[int, typer.Option("--width", "-w", help="Width for rect map")] = 6,
    height: Annotated[
        int, typer.Option("--height", "-h", help="Height for rect map")
    ] = 4,
    hex_size: Annotated[int, typer.Option("--hex-size", "-s", help="Hex size")] = 10,
    orientation: Annotated[
        orientation_types,
        typer.Option(
            "--orientation",
            "-O",
            help="Orientation of the hexagons. pointy : pointy corner up, flat : flat side up",
        ),
    ] = orientation_types.pointy,
):
    if type == map_types.rect:
        hex_map = RectHexMap(width, height, hex_size, orientation)  # type: ignore
    elif type == map_types.hex:
        hex_map = CircularHexMap(radius, hex_size, orientation)  # type: ignore

    if output is not None:
        with open(output, "w") as f:
            f.write(str(hex_map))

    if png_output is not None:
        hex_map.draw(png_output)
