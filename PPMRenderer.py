class PPMRenderer:
    def __init__(self, path: str):
        self.path = path

    def render(self):
        image_width = 256
        image_height = 256

        data = [f'P3\n{image_width} {image_height}\n255\n']

        for j in range(image_height - 1, -1, -1):
            for i in range(image_width):
                r = float(i) / (image_width - 1)
                r = int(255.999 * r)

                g = float(j) / (image_height - 1)
                g = int(255.999 * g)

                b = 0.25
                b = int(255.999 * b)

                data.append(f'{r} {g} {b}\n')

        output_file = open(self.path, "w")
        output_file.writelines(data)
        output_file.close()
