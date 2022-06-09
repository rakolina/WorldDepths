# AI Rev tech task

# we have a 2-D world (like Terraria!)
# How deep is the deepest water pool?
# Assumptions:
#   1. pools at world edges have depth 0
#
# Game plan:
#   set deepest world point at highest value in world points
#   find all local maxima
#   walk all maxima but start at second one
#     find lowest point between adjaacent local maxima
#       set deepest pool to the difference between the smaller of two adjacent local maxima and the deepest point
#

from scipy.signal import find_peaks


class WorldDepth:
    # world_points = [ 2, 1, 2, 3, 1, 3, 0, 1, 2, 6, 3, 5, 2, 1, 4, 9, 7, 8 ]


    def find_deepest_pool ( self, points ):
        if not points:
            return 0

        peak_points, _ = find_peaks ( points )

        # set initial lowest point to world global maximum
        dip = 0
        for p in peak_points:
            if points [ p ] > dip:
                dip = points [ p ]

        left_edge = 0
        deepest_pool = 0
        for peak_idx in peak_points:
            # start at second local maximum
            if 0 == peak_idx:
                break

            # walk left
            for i in range ( peak_idx, left_edge + 1, -1 ):
                if points [ i - 1 ] < points [ i ]:
                    dip = points [ i - 1 ]
                else:
                    break

            # pool depth is the difference between the lower local maximum and the local lowset point
            if points [ left_edge ] <= points [ peak_idx ]:
                if deepest_pool < points [ left_edge ] - dip:
                    deepest_pool = points [ left_edge ] - dip
            else:
                if deepest_pool < points [ peak_idx ] - dip:
                    deepest_pool = points [ peak_idx ] - dip

            left_edge = peak_idx

        return deepest_pool
