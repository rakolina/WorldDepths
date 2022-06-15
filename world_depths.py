# AI Rev tech task

# Class expects non-negative integers list1
#
# In a 2-D world (like Terraria!) water pools can form between adjacent peaks
# How deep is the deepest water pool?
#
# Assumptions:
#   0. world points list fits in memory - otherwise we need paging/parallelization across multiple computers
#   1. pools at world edges have depth 0
#   2. world points are non-negative integers
#
# Game plan:
#   find all local peaks
#   safely probe each section between adjacent peak pair
#     walk from lower peak down to the lowest point
#       current pool depth is the difference between lower peak and lowest point
#       update running deepest pool
#   return deepest pool

from scipy.signal import find_peaks
import matplotlib.pyplot as plt

DEBUG = 0


# pad 0 height edges to the data set because signal.find_peaks skips edges
def locate_peaks ( points ):
    world_points = [ 0 ]
    world_points.extend ( points )
    world_points.append ( 0 )
    # scipy.signal.find_peaks
    peak_points, _ = find_peaks ( world_points )
    return [ p - 1 for p in peak_points ]  # need list indexes


def find_tallest_peak ( peaks, points ):
    top = 0
    for p in peaks:
        if top < points [ p ]:
            top = points [ p ]
    return top


def find_deepest_pool ( points ):
    if not points:
        return 0
    for p in points:
        if p < 0:
            return -1

    peaks = locate_peaks ( points )
    if 2 > len ( peaks ):
        return 0

    if 0 != DEBUG:
        print ( points )
        print ( peaks )

    deepest_pool = 0
    for p in range ( 1, len ( peaks ) ) :
        left_peak = points [ peaks [ p - 1 ] ]
        right_peak = points [ peaks [ p ] ]
        if left_peak <= right_peak:
            for x in range ( peaks [ p - 1 ], peaks [ p ] ):
                if points [ x ] >= points [ x + 1 ]:
                    depth = left_peak - points [ x + 1 ]
                    if depth > deepest_pool:
                        deepest_pool = depth
        else:
            for x in range ( peaks [ p ], peaks [ p - 1 ], -1 ):
                if points [ x - 1 ] <= points [ x ]:
                    depth = right_peak - points [ x - 1 ]
                    if depth > deepest_pool:
                        deepest_pool = depth

    if 0 != DEBUG:
        print ( "Deepest pool:", deepest_pool )

    return deepest_pool
