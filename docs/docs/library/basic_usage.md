<!-- markdownlint-disable MD007 MD031 -->
# Using hexon as a library

Hexon is a set of classes and utilities to manipulate hexagonal maps.

At the core, you would start by instancing one of the following classes:

- [RectHexMap](./library.md#hexon.structs.hexmap.RectHexMap)
- [CircularHexMap](./library.md#hexon.structs.hexmap.CircularHexMap)

This will also create a list of [Hexagon](./library.md#hexon.structs.hexagon.Hexagon) objects that you can manipulate. In particular, you can set properties for the hexagons that will affect how they are drawn on the map, such as color, label, etc.

To draw the map to an image, you would use the draw ([RectHexMap.draw](./library.md#hexon.structs.hexmap.RectHexMap.draw) or [CircularHexMap.draw](./library.md#hexon.structs.hexmap.CircularHexMap.draw)) method.

See the [code documentation](./library.md) for more details.
