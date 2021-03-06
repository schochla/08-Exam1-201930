"""
Exam 1, problem 4.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Leo Schoch-Spana.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem4()


def run_test_problem4():
    """ Tests the   problem4  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem4  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ONE test on this window:
    title = 'Test 1 of problem4'
    window = rg.RoseWindow(320, 200, title)

    p1 = rg.Point(30, 20)
    p1.fill_color = 'red'
    p2 = rg.Point(300, 150)
    p2.fill_color = 'black'
    problem4(p1, p2, 5, window)
    window.close_on_mouse_click()

    # TWO tests on ANOTHER window.
    title = 'Tests 2 and 3 of problem4'
    window = rg.RoseWindow(400, 250, title)

    p1 = rg.Point(20, 20)
    p1.fill_color = 'yellow'
    p2 = rg.Point(60, 120)
    p2.fill_color = 'gray'
    problem4(p1, p2, 2, window)
    window.continue_on_mouse_click()

    p1 = rg.Point(80, 150)
    p1.fill_color = 'magenta'
    p2 = rg.Point(380, 200)
    p2.fill_color = 'cyan'
    problem4(p1, p2, 15, window)
    window.close_on_mouse_click()


def problem4(point1, point2, n, window):
    point1.attach_to(window)
    point2.attach_to(window)
    line = rg.Line(point1, point2)
    #Placeholder to have a dot path
    line.color = 'Green'
    line.attach_to(window)
    for k in range((2*n) + 1):
        rg.Point.attach_to(line)
    window.render()
    """
    See   problem4_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- Two rg.Point objects, where the second rg.Point is below
            and to the right of the first rg.Point
      -- A positive integer n
      -- A rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:  Draws, on the given RoseWindow:
      -- The two given rg.Point objects.
      -- 2n additional rg.Point objects such that:  (SEE THE PICTURES.)
           - They are evenly spaced between the two given rg.Point objects.
           - The leftmost n of the additional 2n rg.Point objects has fill
             color the same as the rightmost of the two given rg.Point objects.
           - The rightmost n of the additional 2n rg.Point objects has fill
             color the same as the leftmost of the two given rg.Point objects.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type point1:  rg.Point
      :type point2:  rg.Point
      :type n:       int
      :type window:  rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 2. Implement and test this function.
    #          Tests have been written for you (above).
    # IMPORTANT: For PARTIAL CREDIT, ignore the colors.
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
