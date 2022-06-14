from unittest import TestCase

from world_depths import find_deepest_pool


class Test ( TestCase ):

    def test_empty ( self ):
        points = [ ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_out_of_bounds ( self ):
        points = [ -9, 2, 1 ]
        expected = -1
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_single_peak ( self ):
        points = [ 1, 20, 1 ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_single_dip ( self ):
        points = [ 91, 2, 8 ]
        expected = 6
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_double_peak ( self ):
        points = [ 4, 1, 100, 2, 10 ]
        expected = 8
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_plateau ( self ):
        points = [ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4 ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_double_plateau ( self ):
        points = [ 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_multi_plateau ( self ):
        points = [ 40, 60, 10, 10, 10, 5, 5, 5, 1, 1, 1, 20 ]
        expected = 19
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_multi_plateau2 ( self ):
        points = [ 40, 20, 20, 20, 6, 6, 6, 5, 5, 5, 2, 2, 2, 1, 1, 1, 7, 7, 7, 0, 0, 0, 2, 2, 2, 8, 8, 8, 10, 10, 10, 20 ]
        expected = 7
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_three_peaks ( self ):
        points = [ 1, 12, 3, 50, 1, 29, 9 ]
        expected = 28
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_contained_plateau ( self ):
        points = [ 10, 10, 10, 6, 6, 6, 2, 10, 10, 10, 11 ]
        expected = 8
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_contained_plateau2 ( self ):
        points = [ 1, 19, 2, 6, 6, 6, 20 ]
        expected = 17
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )
