def line(coords1, coords2, x):
    slope = (coords2[1]-coords1[1])/(coords2[0]-coords1[0])
    yint = coords1[1] - (slope*coords1[0])
    return (slope*x) + yint

    