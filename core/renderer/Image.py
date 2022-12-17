from core.vector.Color import Color


class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[Color() for __ in range(self.width)] for _ in range(self.height)]

    def set_pixel(self, x, y, color):
        self.pixels[y][x] = color
