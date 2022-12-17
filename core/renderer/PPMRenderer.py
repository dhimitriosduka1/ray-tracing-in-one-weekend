class PPMRenderer:
    def __init__(self, path, image):
        self.path = path
        self.image = image

    def render(self):
        image_width = self.image.width
        image_height = self.image.height

        data = [f'P3\n{image_width} {image_height}\n255\n']

        for j in range(image_height - 1, -1, -1):
            for i in range(image_width):
                pixel = self.image.pixels[j][i]
                data.append(f'{pixel.x} {pixel.y} {pixel.z}\n')

        output_file = open(self.path, "w")
        output_file.writelines(data)
        output_file.close()
