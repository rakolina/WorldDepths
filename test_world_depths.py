from unittest import TestCase

from world_depths import WorldDepth


class Test ( TestCase ):

    def test_find_deepest_pool01 ( self ):
        points = [ ]
        expected = 0
        d = WorldDepth ( )
        result = d.find_deepest_pool ( points )
        self.assertEqual ( self, expected, result )


    def test_find_deepest_pool02 ( self ):
        points = [ 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0 ]
        expected = 5
        d = WorldDepth ( )
        result = d.find_deepest_pool ( points )
        self.assertEqual ( self, expected, result )


    def test_find_deepest_pool03 ( self ):
        points = [ 6, 5, 4, 3, 4, 5, 6 ]
        expected = 3
        d = WorldDepth ( )
        result = d.find_deepest_pool ( points )
        self.assertEqual ( self, expected, result )


    def test_find_deepest_pool04 ( self ):
        points = [ 0, 2, 1, 2, 4, 1, 3, 0, 1, 2 ]
        expected = 3
        d = WorldDepth ( )
        result = d.find_deepest_pool ( points )
        self.assertEqual ( self, expected, result )
