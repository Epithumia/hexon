from .hexedge import HexEdge
from .coordinates import AxialCoord, Point
from . import orientation_types


class Hexagon:
    """
    An hexagonal cell inside an HexMap
    """

    def __init__(
        self,
        coords: AxialCoord,
        size: int,
        orientation: orientation_types = orientation_types.pointy,
        offset: Point = Point(0, 0),
    ):
        """
        Initializes a Hexagon with the given coordinates, size, orientation, and offset.

        Parameters:
            coords: The axial coordinates of the hexagon.
            size: The size of the hexagon.
            orientation: The orientation of the hexagon, either pointy or flat.
            offset: The offset of the hexagon in the grid.
        """
        self.coords = coords
        self.orientation = orientation
        self.size = size
        self.offset = offset
        self.properties = {}
        self.edges = []
        for i in range(6):
            edge = HexEdge(coords, i)
            self.edges.append(edge)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Hexagon):
            return False
        return self.coords == value.coords

    def __hash__(self) -> int:
        return hash(self.coords)

    def __repr__(self) -> str:
        return f"Hexagon(coords={self.coords}, orientation={self.orientation}, properties={self.properties}, offset={self.offset}, edges={self.edges})"

    def hex_corner(self, size: int, direction: int) -> Point:
        """
        Computes the position of the nth hexagon corner in pixels.

        Parameters:
            size: The size of the hexagon.
            direction: The direction of the corner, with 0 being the top-right
                corner and increasing clockwise.

        Returns:
            The position of the corner in pixels, relative to the hexagon's position in the grid.
        """
        from math import pi, cos, sin
        from .coordinates import flat_axial_to_pixel, pointy_axial_to_pixel

        if self.orientation == orientation_types.pointy:
            angle_deg = (60 * direction) - 30
            angle_rad = angle_deg * (pi / 180)
            coords = pointy_axial_to_pixel(self.coords, size)
            return Point(
                round(coords.x + size * cos(angle_rad) - self.offset.x),
                round(coords.y + size * sin(angle_rad) - self.offset.y),
            )
        else:
            angle_deg = 60 * direction
            angle_rad = angle_deg * (pi / 180)
            coords = flat_axial_to_pixel(self.coords, size)
            return Point(
                round(coords.x + size * cos(angle_rad) - self.offset.x),
                round(coords.y + size * sin(angle_rad) - self.offset.y),
            )

    def draw(self, draw_interface: "PIL.Image"):  # type: ignore
        """
        Draws the hexagon on the given image.

        Parameters:
            draw_interface: The image to draw on.

        Notes:
            - If the hexagon has a "border" property, it will be used as the outline color.
            - If the hexagon has a "fill" property, it will be used as the fill color.
            - If the hexagon has a "label" property, it will be drawn on the hexagon, and
                - If the hexagon has a "font" property, it will be used as the font for the label.
                - If the hexagon has a "label_color" property, it will be used as the color for the label.
        """
        if "border" not in self.properties:
            outline = (255, 255, 255)
        else:
            outline = self.properties["border"]
        if "fill" not in self.properties:
            fill = (0, 0, 0)
        else:
            fill = self.properties["fill"]
        draw_interface.polygon(
            [
                (
                    self.hex_corner(self.size, i).x,
                    self.hex_corner(self.size, i).y,
                )
                for i in range(6)
            ],
            fill=fill,
            outline=outline,
        )
        if "label" in self.properties:
            from PIL import ImageFont

            font = self.properties.get(
                "font",
                ImageFont.truetype("Roboto-Regular.ttf", max(self.size // 2, 12)),
            )
            color = self.properties.get("label_color", (255, 255, 255))
            _, _, w, h = draw_interface.textbbox(
                (0, 0), self.properties["label"], font=font
            )
            x = (
                self.hex_corner(self.size, 3).x + self.hex_corner(self.size, 0).x
            ) // 2 - w // 2
            y = (
                self.hex_corner(self.size, 3).y + self.hex_corner(self.size, 0).y
            ) // 2 - h // 2
            draw_interface.text((x, y), self.properties["label"], font=font, fill=color)
