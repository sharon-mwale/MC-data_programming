from cross_peer import digits, squares

def parse_grid(grid):
    """Convert grid to dict of possible values, {square: digits}, or 
    return false if contradicion is detected."""
    ## To start , every square can be any digit; then assign values from the grid
    values = dict((s, digits) for s in squares)
    for s,d in grid_values(grid).items():