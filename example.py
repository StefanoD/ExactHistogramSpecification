#!/usr/bin/env python3

"""
@license: Apache License Version 2.0
@author: Stefano Di Martino
Exact histogram matching
"""

from scipy import misc
from histogram_matching import ExactHistogramMatcher


def histogram_matching_rgb():
    target_img = misc.imread('images/RGB/Luna_medium.jpg')
    reference_img = misc.imread('images/RGB/Luna_White_Balance_medium.jpg')

    reference_histogram = ExactHistogramMatcher.get_histogram(reference_img)
    new_target_img = ExactHistogramMatcher.match_image_to_histogram(target_img, reference_histogram)
    misc.imsave('rgb_out.png', new_target_img)


def histogram_matching_grey_values():
    target_img = misc.imread('images/GreyValue/Luna_medium.jpg')
    reference_img = misc.imread('images/GreyValue/Luna_White_Balance_medium.jpg')

    reference_histogram = ExactHistogramMatcher.get_histogram(reference_img)
    new_target_img = ExactHistogramMatcher.match_image_to_histogram(target_img, reference_histogram)
    misc.imsave('grey_out.png', new_target_img)


def main():
    histogram_matching_rgb()
    histogram_matching_grey_values()


if __name__ == "__main__":
    main()
