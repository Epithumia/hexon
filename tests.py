import unittest

import pytest


class CliTests:
    pass


class CoordinatesUnitTests(unittest.TestCase):
    def test_axial_to_oddr(self):
        from hexon.structs.coordinates import axial_to_oddr
        from hexon.structs.coordinates import AxialCoord
        from hexon.structs.coordinates import OffsetCoord

        assert axial_to_oddr(AxialCoord(0, 0)) == OffsetCoord(0, 0)
        assert axial_to_oddr(AxialCoord(-1, -2)) == OffsetCoord(-2, -2)
        assert axial_to_oddr(AxialCoord(3, -2)) == OffsetCoord(2, -2)
        assert axial_to_oddr(AxialCoord(-3, 2)) == OffsetCoord(-2, 2)
        assert axial_to_oddr(AxialCoord(1, 2)) == OffsetCoord(2, 2)
        assert axial_to_oddr(AxialCoord(-2, 1)) == OffsetCoord(-2, 1)

    def test_oddr_to_axial(self):
        from hexon.structs.coordinates import oddr_to_axial
        from hexon.structs.coordinates import OffsetCoord
        from hexon.structs.coordinates import AxialCoord

        assert oddr_to_axial(OffsetCoord(0, 0)) == AxialCoord(0, 0)
        assert oddr_to_axial(OffsetCoord(-2, -2)) == AxialCoord(-1, -2)
        assert oddr_to_axial(OffsetCoord(2, -2)) == AxialCoord(3, -2)
        assert oddr_to_axial(OffsetCoord(-2, 2)) == AxialCoord(-3, 2)
        assert oddr_to_axial(OffsetCoord(2, 2)) == AxialCoord(1, 2)
        assert oddr_to_axial(OffsetCoord(-2, 1)) == AxialCoord(-2, 1)

    def test_axial_to_evenr(self):
        from hexon.structs.coordinates import axial_to_evenr
        from hexon.structs.coordinates import AxialCoord
        from hexon.structs.coordinates import OffsetCoord

        assert axial_to_evenr(AxialCoord(0, 0)) == OffsetCoord(0, 0)
        assert axial_to_evenr(AxialCoord(-1, -2)) == OffsetCoord(-2, -2)
        assert axial_to_evenr(AxialCoord(3, -2)) == OffsetCoord(2, -2)
        assert axial_to_evenr(AxialCoord(-3, 2)) == OffsetCoord(-2, 2)
        assert axial_to_evenr(AxialCoord(1, 2)) == OffsetCoord(2, 2)
        assert axial_to_evenr(AxialCoord(-2, 1)) == OffsetCoord(-1, 1)

    def test_evenr_to_axial(self):
        from hexon.structs.coordinates import evenr_to_axial
        from hexon.structs.coordinates import OffsetCoord
        from hexon.structs.coordinates import AxialCoord

        assert evenr_to_axial(OffsetCoord(0, 0)) == AxialCoord(0, 0)
        assert evenr_to_axial(OffsetCoord(-2, -2)) == AxialCoord(-1, -2)
        assert evenr_to_axial(OffsetCoord(2, -2)) == AxialCoord(3, -2)
        assert evenr_to_axial(OffsetCoord(-2, 2)) == AxialCoord(-3, 2)
        assert evenr_to_axial(OffsetCoord(2, 2)) == AxialCoord(1, 2)
        assert evenr_to_axial(OffsetCoord(-1, 1)) == AxialCoord(-2, 1)

    def test_axial_to_oddq(self):
        from hexon.structs.coordinates import axial_to_oddq
        from hexon.structs.coordinates import AxialCoord
        from hexon.structs.coordinates import OffsetCoord

        assert axial_to_oddq(AxialCoord(0, 0)) == OffsetCoord(0, 0)
        assert axial_to_oddq(AxialCoord(-2, -1)) == OffsetCoord(-2, -2)
        assert axial_to_oddq(AxialCoord(2, -3)) == OffsetCoord(+2, -2)
        assert axial_to_oddq(AxialCoord(-2, 3)) == OffsetCoord(-2, 2)
        assert axial_to_oddq(AxialCoord(2, 1)) == OffsetCoord(2, 2)
        assert axial_to_oddq(AxialCoord(-1, -1)) == OffsetCoord(-1, -2)

    def test_oddq_to_axial(self):
        from hexon.structs.coordinates import oddq_to_axial
        from hexon.structs.coordinates import OffsetCoord
        from hexon.structs.coordinates import AxialCoord

        assert oddq_to_axial(OffsetCoord(0, 0)) == AxialCoord(0, 0)
        assert oddq_to_axial(OffsetCoord(-2, -2)) == AxialCoord(-2, -1)
        assert oddq_to_axial(OffsetCoord(2, -2)) == AxialCoord(2, -3)
        assert oddq_to_axial(OffsetCoord(-2, 2)) == AxialCoord(-2, 3)
        assert oddq_to_axial(OffsetCoord(2, 2)) == AxialCoord(2, 1)
        assert oddq_to_axial(OffsetCoord(-1, -2)) == AxialCoord(-1, -1)

    def test_axial_to_evenq(self):
        from hexon.structs.coordinates import axial_to_evenq
        from hexon.structs.coordinates import AxialCoord
        from hexon.structs.coordinates import OffsetCoord

        assert axial_to_evenq(AxialCoord(0, 0)) == OffsetCoord(0, 0)
        assert axial_to_evenq(AxialCoord(-2, -1)) == OffsetCoord(-2, -2)
        assert axial_to_evenq(AxialCoord(2, -3)) == OffsetCoord(+2, -2)
        assert axial_to_evenq(AxialCoord(-2, 3)) == OffsetCoord(-2, 2)
        assert axial_to_evenq(AxialCoord(2, 1)) == OffsetCoord(2, 2)
        assert axial_to_evenq(AxialCoord(-1, -1)) == OffsetCoord(-1, -1)

    def test_evenq_to_axial(self):
        from hexon.structs.coordinates import evenq_to_axial
        from hexon.structs.coordinates import OffsetCoord
        from hexon.structs.coordinates import AxialCoord

        assert evenq_to_axial(OffsetCoord(0, 0)) == AxialCoord(0, 0)
        assert evenq_to_axial(OffsetCoord(-2, -2)) == AxialCoord(-2, -1)
        assert evenq_to_axial(OffsetCoord(2, -2)) == AxialCoord(2, -3)
        assert evenq_to_axial(OffsetCoord(-2, 2)) == AxialCoord(-2, 3)
        assert evenq_to_axial(OffsetCoord(2, 2)) == AxialCoord(2, 1)
        assert evenq_to_axial(OffsetCoord(-1, -1)) == AxialCoord(-1, -1)

    def test_neighbors(self):
        from hexon.structs.coordinates import neighbors
        from hexon.structs.coordinates import AxialCoord

        assert neighbors(AxialCoord(0, 0)) == [
            AxialCoord(1, 0),
            AxialCoord(1, -1),
            AxialCoord(0, -1),
            AxialCoord(-1, 0),
            AxialCoord(-1, 1),
            AxialCoord(0, 1),
        ]

    def test_distance(self):
        from hexon.structs.coordinates import distance
        from hexon.structs.coordinates import AxialCoord

        assert distance(AxialCoord(0, 0), AxialCoord(0, 0)) == 0
        assert distance(AxialCoord(0, 0), AxialCoord(1, 0)) == 1
        assert distance(AxialCoord(0, 0), AxialCoord(1, 1)) == 2
        assert distance(AxialCoord(0, 0), AxialCoord(-1, 0)) == 1
        assert distance(AxialCoord(0, 0), AxialCoord(-1, -1)) == 2

    def test_euclidean_distance(self):
        from hexon.structs.coordinates import euclidean_distance
        from hexon.structs.coordinates import AxialCoord
        from math import sqrt

        assert euclidean_distance(AxialCoord(0, 0), AxialCoord(0, 0)) == 0
        assert euclidean_distance(AxialCoord(0, 0), AxialCoord(1, 0)) == 1
        assert euclidean_distance(AxialCoord(0, 0), AxialCoord(1, 1)) == sqrt(3)
        assert euclidean_distance(AxialCoord(0, 0), AxialCoord(-1, 0)) == 1
        assert euclidean_distance(AxialCoord(0, 0), AxialCoord(-1, -1)) == sqrt(3)
        assert euclidean_distance(AxialCoord(4, 2), AxialCoord(2, -1)) == sqrt(19)

    def test_offset_distance(self):
        from hexon.structs.coordinates import (
            offset_distance,
            oddq_to_axial,
            oddr_to_axial,
            evenq_to_axial,
            evenr_to_axial,
        )
        from hexon.structs.coordinates import OffsetCoord

        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(0, 0), oddq_to_axial) == 0
        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 0), oddq_to_axial) == 1
        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 1), oddq_to_axial) == 2
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, 0), oddq_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, -1), oddq_to_axial) == 1
        )

        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(0, 0), oddr_to_axial) == 0
        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 0), oddr_to_axial) == 1
        assert offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 1), oddr_to_axial) == 2
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, 0), oddr_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, -1), oddr_to_axial) == 1
        )

        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(0, 0), evenq_to_axial) == 0
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 0), evenq_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 1), evenq_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, 0), evenq_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, -1), evenq_to_axial) == 2
        )

        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(0, 0), evenr_to_axial) == 0
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 0), evenr_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(1, 1), evenr_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, 0), evenr_to_axial) == 1
        )
        assert (
            offset_distance(OffsetCoord(0, 0), OffsetCoord(-1, -1), evenr_to_axial) == 2
        )

    def test_axial_round(self):
        from hexon.structs.coordinates import axial_round, AxialCoord

        assert axial_round(0, 0, 0) == AxialCoord(0, 0)
        assert axial_round(1.1, 1.1, 1.1) == AxialCoord(1, 1)
        assert axial_round(-1.1, -1.1, -1.1) == AxialCoord(-1, -1)
        assert axial_round(0, 0) == AxialCoord(0, 0)
        assert axial_round(1.1, 1.1) == AxialCoord(1, 1)
        assert axial_round(-1.1, -1.1) == AxialCoord(-1, -1)

    def test_Point(self):
        from hexon.structs.coordinates import Point

        p1 = Point(1, 1)
        p2 = Point(1, 1)
        p3 = Point(2, 2)

        assert p1 == p2
        assert p1 != p3
        assert p1 + p2 == p3
        assert p3 - p2 == p1
        assert p1 != (1, 1)

    def test_lerp(self):
        from hexon.structs.coordinates import lerp

        assert lerp(1, 2, 0.5) == 1.5

    def test_axial_lerp(self):
        from hexon.structs.coordinates import axial_lerp
        from hexon.structs.coordinates import AxialCoord

        assert axial_lerp(AxialCoord(1, 1), AxialCoord(2, 2), 0.5) == AxialCoord(2, 1)

    def test_axial_line_draw(self):
        from hexon.structs.coordinates import axial_line_draw
        from hexon.structs.coordinates import AxialCoord

        assert axial_line_draw(AxialCoord(0, 0), AxialCoord(2, 3)) == [
            AxialCoord(0, 0),
            AxialCoord(0, 1),
            AxialCoord(1, 1),
            AxialCoord(1, 2),
            AxialCoord(2, 2),
            AxialCoord(2, 3)
        ]

        assert axial_line_draw(AxialCoord(0, 0), AxialCoord(1, 5)) == [
            AxialCoord(0, 0),
            AxialCoord(0, 1),
            AxialCoord(0, 2),
            AxialCoord(0, 3),
            AxialCoord(1, 3),
            AxialCoord(1, 4),
            AxialCoord(1, 5)
        ]
    
    def test_pixel_to_pointy_hex(self):
        from hexon.structs.coordinates import pixel_to_pointy_hex, Point, AxialCoord

        assert pixel_to_pointy_hex(Point(0, 0), 10) == AxialCoord(0, 0)
        assert pixel_to_pointy_hex(Point(12, 12), 10) == AxialCoord(0, 1)
        assert pixel_to_pointy_hex(Point(111, 111), 10) == AxialCoord(3, 7)

    def test_pixel_to_flat_hex(self):
        from hexon.structs.coordinates import pixel_to_flat_hex, Point, AxialCoord

        assert pixel_to_flat_hex(Point(0, 0), 10) == AxialCoord(0, 0)
        assert pixel_to_flat_hex(Point(12, 12), 10) == AxialCoord(1, 0)
        assert pixel_to_flat_hex(Point(111, 111), 10) == AxialCoord(7, 3)

class MapUnitTests(unittest.TestCase):
    @pytest.fixture(scope="class", autouse=True)
    def new_path(self, tmp_path_factory):
        MapUnitTests.__new_path = tmp_path_factory.mktemp("hexon")

    def test_find_offset(self):
        from hexon.structs.hexmap import find_offset
        from hexon.structs.hexagon import Hexagon
        from hexon.structs.coordinates import Point, AxialCoord

        hex = Hexagon(AxialCoord(0, 0), 10)

        assert find_offset(hex, 10) == Point(-9, -10)

        hex = Hexagon(AxialCoord(0, 0), 10, "flat")

        assert find_offset(hex, 10) == Point(-10, -9)

    def test_RectHexMap(self):
        from hexon.structs.hexmap import RectHexMap

        map = RectHexMap(10, 10, 10)

        p = self.__new_path / "test.png"
        map.draw(p)

        assert (
            str(map)[0:81]
            == "RectHexMap(width=10, height=10, hex_size=10, orientation=orientation_types.pointy"
        )

        flat_map = RectHexMap(10, 10, 10, "flat")

        for hex in flat_map.hexagons:
            assert flat_map.hexagons[hex].orientation == "flat"
            flat_map.hexagons[hex].properties = {
                "border": (255, 0, 0),
                "fill": (0, 255, 0),
                "label": "test",
                "label_color": (0, 0, 255),
            }

        p = self.__new_path / "test.png"
        flat_map.draw(p)

        assert (
            str(flat_map)[0:61]
            == "RectHexMap(width=10, height=10, hex_size=10, orientation=flat"
        )

    def test_CircularHexMap(self):
        from hexon.structs.hexmap import CircularHexMap

        map = CircularHexMap(10, 10)

        p = self.__new_path / "test.png"
        map.draw(p)

        assert (
            str(map)[0:75]
            == "CircularHexMap(radius=10, hex_size=10, orientation=orientation_types.pointy"
        )

        flat_map = CircularHexMap(10, 10, "flat")

        p = self.__new_path / "test.png"
        flat_map.draw(p)

        assert (
            str(flat_map)[0:55]
            == "CircularHexMap(radius=10, hex_size=10, orientation=flat"
        )

    def test_Hexagon(self):
        from hexon.structs.hexagon import Hexagon
        from hexon.structs.coordinates import AxialCoord

        hex = Hexagon(AxialCoord(0, 0), 10)
        hex2 = Hexagon(AxialCoord(0, 0), 10)
        ax = AxialCoord(0, 0)

        assert hex.coords == AxialCoord(0, 0)
        assert hex.orientation == "pointy"
        assert hex.size == 10
        assert hex == hex2
        assert hex != ax
        assert hash(hex) == hash(hex2)
