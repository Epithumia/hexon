import unittest


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
