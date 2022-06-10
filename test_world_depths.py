from unittest import TestCase

from world_depths import find_deepest_pool


class Test ( TestCase ):

    # world_points = [ 2, 1, 2, 3, 1, 3, 0, 1, 2, 6, 3, 5, 2, 1, 4, 9, 7, 8 ]

    def test_find_deepest_pool01 ( self ):
        points = [ ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_find_deepest_pool02 ( self ):
        points = [ 2, 1, -1 ]
        expected = -1
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_find_deepest_pool03 ( self ):
        points = [ 0, 1, 2, 3, 4, 3, 2, 1, 0 ]
        expected = 0
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_find_deepest_pool04 ( self ):
        points = [ 6, 5, 4, 3, 4, 5, 6 ]
        expected = 3
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_find_deepest_pool05 ( self ):
        points = [ 0, 2, 1, 2, 4, 1, 3, 0, 1, 2 ]
        expected = 2
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )

    def test_find_deepest_pool06 ( self ):
        points = [ 6, 3, 5, 2, 1, 4, 9, 7, 8 ]
        expected = 4
        result = find_deepest_pool ( points )
        self.assertEqual ( expected, result, points )
