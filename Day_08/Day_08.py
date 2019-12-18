from PIL import Image
ROWS = 6
COLUMNS = 25
LAYER_SIZE = ROWS * COLUMNS
RGB_COLOURS = {
        0: (0, 0, 0),
        1: (255, 255, 255)
        }


def read_layers(filename="input.txt"):
    with open(filename, "r") as input_file:
        raw_data = input_file.read()
        return split_into_layers(raw_data)


def split_into_layers(data):
    if len(data) % LAYER_SIZE != 0:
        raise Exception("Invalid data length; not a multiple of layer size!")

    number_of_layers = int(len(data)/LAYER_SIZE)
    layers = []
    for layer in range(number_of_layers):
        start_index = layer * LAYER_SIZE
        layers.append(data[start_index:start_index+LAYER_SIZE])
    return layers


def star_one(layers):
    fewest_zeros = float('inf')
    result = -1
    for layer in layers:
        zero_count = layer.count("0")
        if zero_count < fewest_zeros:
            fewest_zeros = zero_count
            result = layer.count("1")*layer.count("2")
    return result


def star_two(layers):
    result = []
    for i in range(LAYER_SIZE):
        for layer in layers:
            if int(layer[i]) < 2:
                result.append(int(layer[i]))
                break
    return result


def print_image(image_data):
    scale = 10
    img = Image.new("RGB", (COLUMNS, ROWS), "black")
    pixels = img.load()
    for row in range(ROWS):
        for col in range(COLUMNS):
            pixels[col, row] = RGB_COLOURS[image_data[row*COLUMNS + col]]
    img_scaled = img.resize((COLUMNS*scale, ROWS*scale), Image.NEAREST)
    img_scaled.show()


if __name__ == "__main__":
    layers = read_layers()
    print("Star_one: {}".format(star_one(layers)))
    print_image(star_two(layers))
