import random   # to randomly place stars on the grid
from time import sleep   # used for a slight delay between frames

from IPython.display import clear_output   # clears previous output, allowing each "frame" to
                                           # overlay one another, and make movements appear

class Point:
    """Specifies the coordinates of the point. It maintains info about the coordinate system
    to be able to track a star, and to get/set the coordinates.

    """


    def __init__(self, location_x=0, location_y=0):
        """Initializes the point.

        Parameters
        ----------
        location_x : int
            x position of the star
        location_y : int
            y position of the star

        Returns
        -------
        The star point is initialized and can be manipulated.
        """

        self.x_pos = location_x
        self.y_pos = location_y

    def get_x(self):
        """Get x position of the point.

        Paramters
        ---------
        None

        Returns
        -------
        Point's x-coordinate
        """

        return self.x_pos

    def get_y(self):
        """Get y position of the point.

        Paramters
        ---------
        None

        Returns
        -------
        Point's y-coordinate

        """
        return self.y_pos

    def set_coordinate(self, x_coord, y_coord):
        """Set x and y coordinate of the point.

        Paramters
        ---------
        x : int
            Point's x position
        y : int
            Point's y position

        Returns
        -------
        Sets the point's coordinates based on the x and y inputs
        """

        self.x_pos = x_coord
        self.y_pos = y_coord


class Screen:
    """Used to display the screen with the stars simulation, and controls any other settings,
    ex. frame, density, etc. It models outer space from a porthole view, where you can see the
    stars passing by. For this simulation, I used a '*' for a star, and ' ' for empty space.

    """

    def __init__(self, grid_width=80, grid_height=40, density=0.01, frames=50, delay=.1):
        """Initializes screen and star settings.

        Paramters
        ---------
        grid_width : int
            Sets width of the grid, used to display the star simulation
        grid_height : int
            Sets height of the grid, used to display the star simulation
        density : float
            Float used to determine how many stars should be display
        frames : int
            Integer to determine how many times the star's positions are changed
        delay : float
            Float used to determine if there is a delay between each frame

        Returns
        -------
        Screen and star settings are initialized and can be used.
        """

        self.width = grid_width
        self.height = grid_height

        # creates 2d array for the screen
        self.screen = [[" " for x in range(self.width)] for y in range(self.height)]

        self.density = density
        self.frames = frames
        self.delay = delay

        ## list of Points (each point models a star)
        self.stars = []
        self.direction = Point(1, 1)  # default direction is x = 1, y = 1
        self.add_stars()

    def set_screen_size(self, width, height):
        """Sets screen size, based on width and height inputs

        Paramters
        ---------
        width : int
            width of the screen display
        height : int
            height of the screen display

        Returns
        -------
        Sets the screen size, and adds stars to the grid
        """

        self.width = width
        self.height = height
        self.screen = [[" " for x in range(self.width)] for y in range(self.height)]
        self.stars = []
        self.add_stars()

    def set_frames(self, frames):
        """Sets number of frames the simulation will be run

        Paramters
        ---------
        frames : int
            number of times run

        Returns
        -------
        Sets the number of frames
        """

        self.frames = frames

    def get_frames(self):
        """Gets number of frames the simulation will be run

        Paramters
        ---------
        None

        Returns
        -------
        Number of frames
        """

        return self.frames


    def set_density(self, density):
        """Sets the percent of the screen will be covered with stars

        Paramters
        ---------
        density : float
            Float to set density

        Returns
        -------
        Sets density of screen with stars, and adds the stars into the board
        """

        self.screen = [[" " for x in range(self.width)] for y in range(self.height)]
        self.density = density
        self.stars = []
        self.add_stars()

    def get_density(self):
        """Gets the percent of the screen will be covered with stars

        Paramters
        ---------
        density : float
            Float to set density

        Returns
        -------
        Gets percent of stars, in decimal form
        """

        return self.density

    def get_width(self):
        """Gets width of grid display

        Paramters
        ---------
        None

        Returns
        -------
        Gets width of screen
        """

        return self.width

    def get_height(self):
        """Gets height of grid display

        Paramters
        ---------
        None

        Returns
        -------
        Gets height of screen
        """

        return self.height


    def set_direction(self, vector):
        """Sets direction the stars will be traveling in

        Paramters
        ---------
        vector : Point
            Inputted as a point object to set direction

        Returns
        -------
        Direction, as a Point object, is set.
        """

        if isinstance(vector, Point):  # checks that it is inputted as a point object

            self.direction = vector

    def get_direction(self):
        """Gets direction the stars will be traveling in

        Paramters
        ---------
        None

        Returns
        -------
        Returns direction.
        """

        return self.direction

    def add_stars(self):
        """Add stars to the display

        Paramters
        ---------
        None

        Returns
        -------
        Randomly placed stars are visible in the frame
        """

        # calculates number of stars, based on width, height, and density,
        # since the number of stars can vary based on the grid size
        num_stars = int(self.width * self.height * self.density)

        for it in range(num_stars):

            # create a single point star
            rand_star_x = random.randint(0, self.width-1)
            rand_star_y = random.randint(0, self.height-1)

            # star is added into the points list and into the screen
            a_point = Point(rand_star_x, rand_star_y)
            self.stars.append(a_point)
            self.screen[rand_star_y][rand_star_x] = "*"

    def display_screen(self):
        """Function to display the screen

        Paramters
        ---------
        None

        Returns
        -------
        New grid called output, as a string, is created
        """

        output = ""

        # Used to print the grid out, and in the correct format
        for row in range(0, self.height):

            for col in range(0, self.width):

                output += self.screen[row][col]

            output += "\n"

        # clear previous iteration, print the new grid (as a string)
        clear_output(True)
        print(output)

    def update_board_linearly(self):
        """Updates the location of the stars and moves them to create a simulation

        Paramters
        ---------
        None

        Returns
        -------
        New location for star
        """

        # stars are incremented based on the direction values
        x_increment = self.direction.get_x()
        y_increment = self.direction.get_y()

        for star in self.stars:

            # get coordinates of star
            star_x = star.get_x()
            star_y = star.get_y()

            # erase star from old location by using empty string
            self.screen[star_y][star_x] = " "

            # do math for new star location, and prevents new star to move off the grid
            star_x += x_increment
            star_y -= y_increment
            new_x = star_x % self.width
            new_y = star_y % self.height

            # place star in new location and update new location for the Point
            self.screen[new_y][new_x] = "*"
            star.set_coordinate(new_x, new_y)

    def run(self):
        """Updates the location of the stars and moves them to create a simulation

        Paramters
        ---------
        None

        Returns
        -------
        The program can be run, with the default settings or the settings the user had inputted
        """

        # runs the simulation depending on the number of frames set
        for second in range(1, self.frames):

            self.display_screen()
            self.update_board_linearly()
            sleep(self.delay)
