from common.src.classes import Node


def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb):
    return f"#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def interpolate_color(
    start_color: tuple[int, int, int],
    end_color: tuple[int, int, int],
    elem_sequence_number: float,
) -> tuple[int, int, int]:
    interpolated_color: list[int] = []
    rgb_borders = zip(start_color, end_color)

    for color_channel in rgb_borders:
        start_channel, end_channel = color_channel
        interpolated_channel = (
            start_channel + (end_channel - start_channel) * elem_sequence_number
        )
        interpolated_color.append(int(interpolated_channel))

    return interpolated_color[0], interpolated_color[1], interpolated_color[2]


def color_nodes(nodes_sequence: list[Node]) -> None:
    start_color = hex_to_rgb("#0000FF")  # Blue
    end_color = hex_to_rgb("#FFFF00")  # Yellow
    total_nodes = len(nodes_sequence)

    for index, node in enumerate(nodes_sequence):
        elem_sequence_number = index / (total_nodes - 1) if total_nodes > 1 else 0
        interpolated_color = interpolate_color(
            start_color, end_color, elem_sequence_number
        )
        node.color = rgb_to_hex(interpolated_color)
