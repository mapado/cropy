import math

from skimage.exposure import histogram


def image_entropy(img):
    """ Calculate the entropy of an image

    :param img: image vector
    :type img: numpy.ndarray

    :return: value of the image entropy
    :type return: float

    """
    histo, bins = histogram(img, nbins=255)
    histogram_length = sum(histo)

    samples_probability = [float(h) / histogram_length for h in histo]
    entropy = -sum([p * math.log(p, 2) for p in samples_probability if p != 0])
    return entropy


def entropy_crop(img, target_width, target_height, max_steps=10):
    """ Return best starting point for a crop based on target width and height

    Image is not resized. Thus, a small crop size with a big original
    image could lead to weird, unoptimal results.

    :param target_width, target_height: dimensions of the cropped image
    :type param target_width, target_height: int

    :param maxsteps: maximum number of iteration.
        More iteration means more precision but less speed (default=10)
    :type maxsteps: int

    """
    original_height, original_width = img.shape
    right_x = original_width
    bottom_y = original_height
    top_y = 0  # offset value from image top to estimate
    left_x = 0  # offset value from image top to estimate*

    # calculate slice size based on max steps
    slice_size = int(round((original_width - target_width) / max_steps))
    if slice_size == 0:
        slice_size = 1

    left_slice = None
    right_slice = None

    # cut left or right slice of image based on min entropy value until targetwidth is reached
    # while there still are uninvestigated slices of the image (left and right)
    while ((right_x - left_x - slice_size) > target_width):
        if (left_slice is None):
            left_slice = img[0: original_height + 1, left_x: left_x + slice_size + 1]

        if (right_slice is None):
            right_slice = img[0: original_height + 1, right_x - slice_size: right_x + 1]

        if (image_entropy(left_slice) < image_entropy(right_slice)):
            left_x = left_x + slice_size
            left_slice = None
        else:
            right_x = right_x - slice_size
            right_slice = None

    top_slice = None
    bottom_slice = None

    # calculate slice size based on max steps
    slice_size = int(round((original_height - target_height) / max_steps))
    if slice_size == 0:
        slice_size = 1

    # cut upper or bottom slice of image based on min entropy value until
    # target height is reached
    # while there still are uninvestigated slices of the image (top and bottom)
    while ((bottom_y - top_y - slice_size) > target_height):
        if (top_slice is None):
            top_slice = img[top_y: top_y + slice_size + 1, 0: original_width + 1]

        if (bottom_slice is None):
            bottom_slice = img[bottom_y - slice_size:bottom_y + 1, 0: original_width + 1]

        if (image_entropy(top_slice) < image_entropy(bottom_slice)):
            top_y = top_y + slice_size
            top_slice = None
        else:
            bottom_y = bottom_y - slice_size
            bottom_slice = None

    return(left_x, top_y)
