# AI Rev tech task

# we have a 2-D world (like Terraria!)
# How deep is the deepest water pool?
# Assumptions:
#   1. pools at world edges have depth 0
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


class WorldDepth:

    def find_deepest_pool ( self, points ):
        if not points:
            return 0

        peak_points, _ = find_peaks ( points )

        # set initial lowest point to world global maximum
        dip = self.find_global_max ( peak_points, points )

        deepest_pool = 0
        for peak_index in range ( 1, len ( peak_points ) ):

            # walk right
            for i in range ( peak_index - 1, peak_index ):
                if points [ i - 1 ] >= points [ i ]:
                    dip = points [ i ]
                else:
                    break

            # current pool depth is the difference between the lower of two adjacent peaks
            # and the lowest point between them
            # keep a running maximum
            if points [ peak_index - 1 ] <= points [ peak_index ]:
                if deepest_pool < points [ peak_index - 1 ] - dip:
                    deepest_pool = points [ peak_index - 1 ] - dip
            else:
                if deepest_pool < points [ peak_index ] - dip:
                    deepest_pool = points [ peak_index ] - dip

        return deepest_pool

    def find_global_max ( self, peak_points, points ):
        dip = 0
        for p in peak_points:
            if points [ p ] > dip:
                dip = points [ p ]
        return dip
