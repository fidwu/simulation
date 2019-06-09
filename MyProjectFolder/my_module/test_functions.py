import my_module.functions as func

def test_point():
    """Tests the Point class."""
    
    # validating instance creation without parameters
    point = func.Point()
    assert point.get_x() == 0
    assert point.get_y() == 0

    # validating instance creation with parameters
    point = func.Point(5, 6)
    assert point.get_x() == 5
    assert point.get_y() == 6

    # validate setting x/y
    point.set_coordinate(2, 4)
    assert point.get_x() == 2
    assert point.get_y() == 4

def test_screen():
    """Tests the Point class."""
    
    # validating instance creation without parameters
    screen = func.Screen()
    assert screen.get_width() == 80
    assert screen.get_height() == 40
    assert screen.density == 0.01
    assert screen.frames == 50
    assert screen.delay == .1

    # validating instance creation with parameters
    screen = func.Screen(grid_width=33, grid_height=77)
    assert screen.get_width() == 33
    assert screen.get_height() == 77
    assert screen.density == 0.01
    assert screen.frames == 50
    assert screen.delay == .1
