# AI Rev tech task

# Class expects non-negative integers list1
#
# we have a 2-D world (like Terraria!)
# How deep is the deepest water pool?
# Assumptions:
#   1. pools at world edges have depth 0
#   2. world points are positive integers including 0
#
# Game plan:
#   find all local peaks
#   safely walk all peaks
#     find lowest point between two adjacent local maxima
#       current pool depth is the difference
#       between the lower of the two adjacent peaks
#       and the deepest point between them
#     remember the deepest pool seen so far
#

from scipy.signal import find_peaks
import matplotlib.pyplot as plt

DEBUG = 1


# pad 0 height edges to the data set because signal.find_peaks skips edges
def find_peak_locations ( points ):
    world_points = [ 0 ]
    world_points.extend ( points )
    world_points.append ( 0 )
    peak_points, _ = find_peaks ( world_points )
    return [ p - 1 for p in peak_points ]  # need list indexes


def find_tallest_peak ( peak_points, points ):
    top = 0
    for p in peak_points:
        if top < points [ p ]:
            top = points [ p ]
    return top


def find_deepest_pool ( points ):
    if not points:
        return 0
    for p in points:
        if p < 0:
            return -1

    peak_indexes = find_peak_locations ( points )
    if 2 > len ( peak_indexes ):
        return 0

    dip = find_tallest_peak ( peak_indexes, points )  # initialize lowest point to largest datapoint
    deepest_pool = 0
    for peak_index in range ( 1, len ( peak_indexes ) ):

        # walk right
        for points_index in range ( peak_indexes [ peak_index - 1 ], peak_indexes [ peak_index ] ):
            if points [ points_index ] >= points [ points_index + 1 ]:
                dip = points [ points_index ]
            else:
                break

        if points [ peak_index - 1 ] <= points [ peak_index ]:
            if deepest_pool < points [ peak_index - 1 ] - dip:
                deepest_pool = points [ peak_index - 1 ] - dip
        else:
            if deepest_pool < points [ peak_index ] - dip:
                deepest_pool = points [ peak_index ] - dip

    if 0 != DEBUG:
        print ( "Deepest pool:", deepest_pool )

    return deepest_pool
