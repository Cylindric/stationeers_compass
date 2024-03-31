from compass.compass import Compass

class TestCompass(object):

    def test_distance(self):
        result = Compass.distance([1, 0], [0, 0])
        assert result == 1

        result = Compass.distance([0, 0], [1, 0])
        assert result == 1

    def test_distance_when_zero(self):
        result = Compass.distance([0, 0], [0, 0])
        assert result == 0

    def test_bearing_0(self):
        c = Compass("Moon")
        result = c.bearing([0, 100], [0, 0])
        assert result == 0

    def test_bearing_90(self):
        c = Compass("Moon")
        result = c.bearing([100, 0], [0, 0])
        assert result == 90

    def test_bearing_180(self):
        c = Compass("Moon")
        result = c.bearing([0, -100], [0, 0])
        assert result == 180

    def test_bearing_270(self):
        c = Compass("Moon")
        result = c.bearing([-100, 0], [0, 0])
        assert result == 270

    def test_bearing_when_zero(self):
        c = Compass("Moon")
        result = c.bearing([0, 0], [0, 0])
        assert result == 0

