from dataclasses import dataclass
from typing import Callable


@dataclass
class Point:
    """
    Pixel coordinates.

    Attributes:
        x: The x coordinate.
        y: The y coordinate.
    """
    x: int | float
    y: int | float

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Point):
            return False
        return self.x == value.x and self.y == value.y


@dataclass
class AxialCoord:
    """
    Axial (and cube) coordinates.

    Attributes:
        q: The q coordinate of the hexagon.
        r: The r coordinate of the hexagon
        s: The s coordinate of the hexagon.
    """
    q: int | float
    r: int | float

    @property
    def s(self):
        return -self.q - self.r

    def __add__(self, other):
        return AxialCoord(self.q + other.q, self.r + other.r)

    def __sub__(self, other):
        return AxialCoord(self.q - other.q, self.r - other.r)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, AxialCoord):
            return False
        return self.q == value.q and self.r == value.r

    def __hash__(self) -> int:
        return hash((self.q, self.r))


NEIGHBORS = [
    AxialCoord(1, 0),
    AxialCoord(1, -1),
    AxialCoord(0, -1),
    AxialCoord(-1, 0),
    AxialCoord(-1, 1),
    AxialCoord(0, 1),
]


@dataclass
class OffsetCoord:
    """
    Offset coordinates.

    Attributes:
        col: The column of the hexagon.
        row: the row of the hexagon.
    """
    col: int | float
    row: int | float


def axial_to_oddr(hex: AxialCoord) -> OffsetCoord:
    """
    Convert an AxialCoord to an OffsetCoord. Used when you
    have "pointy top" hexagons, and you want odd rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The AxialCoord to convert.

    Returns:
        The converted OffsetCoord.
    """
    parity = int(hex.r) & 1
    col = hex.q + (hex.r - parity) // 2
    row = hex.r
    return OffsetCoord(col=col, row=row)


def oddr_to_axial(hex: OffsetCoord) -> AxialCoord:
    """
    Convert an OffsetCoord to an AxialCoord. Used when you
    have "flat top" hexagons, and you want odd rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.row) & 1
    q = hex.col - (hex.row - parity) // 2
    r = hex.row
    return AxialCoord(q, r)


def axial_to_evenr(hex: AxialCoord) -> OffsetCoord:
    """
    Convert an AxialCoord to an OffsetCoord. Used when you
    have "pointy top" hexagons, and you want even rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.r) & 1
    col = hex.q + (hex.r + parity) // 2
    row = hex.r
    return OffsetCoord(col=col, row=row)


def evenr_to_axial(hex: OffsetCoord) -> AxialCoord:
    """
    Convert an OffsetCoord to an AxialCoord. Used when you
    have "pointy top" hexagons, and you want even rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.row) & 1
    q = hex.col - (hex.row + parity) // 2
    r = hex.row
    return AxialCoord(q, r)


def axial_to_oddq(hex: AxialCoord) -> OffsetCoord:
    """
    Convert an AxialCoord to an OffsetCoord. Used when you
    have "flat top" hexagons, and you want odd rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.q) & 1
    col = hex.q
    row = hex.r + (hex.q - parity) // 2
    return OffsetCoord(col=col, row=row)


def oddq_to_axial(hex: OffsetCoord) -> AxialCoord:
    """
    Convert an OffsetCoord to an AxialCoord. Used when you
    have "flat top" hexagons, and you want odd rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.col) & 1
    q = hex.col
    r = hex.row - (hex.col - parity) // 2
    return AxialCoord(q, r)


def axial_to_evenq(hex: AxialCoord) -> OffsetCoord:
    """
    Convert an AxialCoord to an OffsetCoord. Used when you
    have "flat top" hexagons, and you want even rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.q) & 1
    col = hex.q
    row = hex.r + (hex.q + parity) // 2
    return OffsetCoord(col=col, row=row)


def evenq_to_axial(hex: OffsetCoord) -> AxialCoord:
    """
    Convert an OffsetCoord to an AxialCoord. Used when you
    have "pointy top" hexagons, and you want even rows
    shoved 1/2 column to the right.

    Parameters:
        hex: The OffsetCoord to convert.

    Returns:
        The converted AxialCoord.
    """
    parity = int(hex.col) & 1
    q = hex.col
    r = hex.row - (hex.col + parity) // 2
    return AxialCoord(q, r)


def neighbors(coord: AxialCoord) -> list[AxialCoord]:
    """
    Return a list of the six neighbors of the given hexagon.

    The neighbors are computed by adding each of the six
    NEIGHBORS to the given AxialCoord.

    Parameters:
        coord: The hexagon for which to compute the neighbors.

    Returns:
        The list of neighbors of the given hexagon.
    """
    return [coord + other for other in NEIGHBORS]


def distance(a: AxialCoord, b: AxialCoord) -> int | float:
    """
    Computes the Manhattan distance between two hexagons.

    Parameters:
        a: The first hexagon.
        b: The second hexagon.

    Returns:
        The distance between the two hexagons.
    """
    v = a - b
    return max(abs(v.q), abs(v.r), abs(v.s))


def euclidean_distance(a: AxialCoord, b: AxialCoord) -> float:
    """
    Computes the Euclidean distance between two hexagons.

    Parameters:
        a: The first hexagon.
        b: The second hexagon.

    Returns:
        The Euclidean distance between the two hexagons.
    """
    v = a - b
    return (v.q**2 + v.r**2 + (v.q * v.r)) ** 0.5


def offset_distance(
    a: OffsetCoord, b: OffsetCoord, conversion: Callable[[OffsetCoord], AxialCoord]
) -> int | float:
    """
    Computes the Manhattan distance between two hexagons given their offset coordinates.

    Parameters:
        a: The first hexagon.
        b: The second hexagon.
        conversion: A function to convert an OffsetCoord to an AxialCoord.

    Returns:
        The distance between the two hexagons.
    """
    return distance(conversion(a), conversion(b))


def axial_round(frac_q: float, frac_r: float, frac_s: float = None) -> AxialCoord:
    """
    Rounds the given fractional hex coordinates to the nearest axial coordinates.

    The fractional coordinates are rounded to the nearest axial coordinates.
    If the difference between the rounded coordinates and the fractional coordinates
    is greater than the difference between the other two coordinates, the rounded
    coordinates are adjusted to minimize the difference.

    Parameters:
        frac_q: The fractional q coordinate.
        frac_r: The fractional r coordinate.
        frac_s: The fractional s coordinate, defaults to None.

    Returns:
        The nearest axial coordinates to the given fractional coordinates.
    """
    if frac_s is None:
        frac_s = -frac_q - frac_r
    q = round(frac_q)
    r = round(frac_r)
    s = round(frac_s)

    q_diff = abs(q - frac_q)
    r_diff = abs(r - frac_r)
    s_diff = abs(s - frac_s)

    if q_diff > r_diff and q_diff > s_diff:
        q = -r - s
    elif r_diff > s_diff:
        r = -q - s

    return AxialCoord(q, r)


def lerp(a: int | float, b: int | float, t: float) -> float:
    """
    Linearly interpolates between two values.

    Parameters:
        a: The starting value.
        b: The ending value.
        t: The interpolation factor, where 0 <= t <= 1.

    Returns:
        The interpolated value.
    """
    return a + (b - a) * t


def axial_lerp(a: AxialCoord, b: AxialCoord, t: float) -> AxialCoord:
    """
    Linearly interpolates between two AxialCoords.

    Parameters:
        a: The starting AxialCoord.
        b: The ending AxialCoord.
        t: The interpolation factor, where 0 <= t <= 1.

    Returns:
        The interpolated AxialCoord.
    """
    return axial_round(lerp(a.q, b.q, t), lerp(a.r, b.r, t), lerp(a.s, b.s, t))


def axial_line_draw(a: AxialCoord, b: AxialCoord) -> list[AxialCoord]:
    """
    Draws a line of hexagons between two points.

    Parameters:
        a: The starting point of the line.
        b: The ending point of the line.

    Returns:
        A list of hexagons (AxialCoords) that form the line.
    """
    N = int(distance(a, b))
    results = []
    a_nudged = a + AxialCoord(0.000001, 0.000002)
    b_nudged = b + AxialCoord(0.000001, 0.000002)
    n = 1.0 / N
    for i in range(N + 1):
        results.append(axial_lerp(a_nudged, b_nudged, n * i))
    return results


def axial_scale(a: AxialCoord, factor: int) -> AxialCoord:
    """
    Scales an AxialCoord by a given factor.

    Parameters:
        a: The AxialCoord to scale.
        factor: The factor to scale by.

    Returns:
        The scaled AxialCoord.
    """
    return AxialCoord(a.q * factor, a.r * factor)


def axial_ring(center: AxialCoord, radius: int) -> list[AxialCoord]:
    """
    Computes a list of hexagons that form a ring around a given center at a given radius.

    Parameters:
        center: The center of the ring.
        radius: The radius of the ring.

    Returns:
        A list of hexagons that form the ring.
    """
    if radius <= 0:
        return [center]
    results = []

    hexagon = center + axial_scale(NEIGHBORS[4], radius)
    for i in range(6):
        for _ in range(radius):
            results.append(hexagon)
            hexagon = neighbors(hexagon)[i]

    return results


def flat_axial_to_pixel(hex: AxialCoord, size: int) -> Point:
    """
    Computes the position of a flat-top hexagon in pixels from its axial coordinates.

    Parameters:
        hex: The axial coordinates of the hexagon.
        size: The size of the hexagon.

    Returns:
        The position of the hexagon in pixels.
    """
    from math import sqrt

    x = (3.0 / 2 * hex.q) * size
    y = (sqrt(3) / 2 * hex.q + sqrt(3) * hex.r) * size

    return Point(x, y)


def pointy_axial_to_pixel(hex: AxialCoord, size: int) -> Point:
    """
    Computes the position of a pointy-top hexagon in pixels from its axial coordinates.

    Parameters:
        hex: The axial coordinates of the hexagon.
        size: The size of the hexagon.

    Returns:
        The position of the hexagon in pixels.
    """
    from math import sqrt

    x = (sqrt(3) * hex.q + sqrt(3) / 2 * hex.r) * size
    y = (3.0 / 2 * hex.r) * size

    return Point(x, y)


def pixel_to_pointy_hex(point: Point, size: int) -> AxialCoord:
    """
    Computes the axial coordinates of a pointy-top hexagon from its pixel coordinates.

    Parameters:
        point: The pixel coordinates of the hexagon.
        size: The size of the hexagon.

    Returns:
        The axial coordinates of the hexagon.
    """

    from math import sqrt

    c_x = point.x / size
    c_y = point.y / size

    q = sqrt(3) / 3 * c_x - 1.0 / 3 * c_y
    r = 2.0 / 3 * c_y
    return axial_round(q, r, -q - r)


def pixel_to_flat_hex(point: Point, size: int) -> AxialCoord:
    """
    Computes the axial coordinates of a flat-top hexagon from its pixel coordinates.

    Parameters:
        point: The pixel coordinates of the hexagon.
        size: The size of the hexagon.

    Returns:
        The axial coordinates of the hexagon.
    """
    from math import sqrt

    c_x = point.x / size
    c_y = point.y / size

    q = 2.0 / 3 * c_x
    r = -1.0 / 3 * c_x + sqrt(3) / 3 * c_y
    return axial_round(q, r, -q - r)
