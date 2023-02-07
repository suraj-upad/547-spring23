def test_line():
    from plane import line
    inputs = [(0,0),(2,3),2]
    answer = line(inputs[0], inputs[1], inputs[2])
    expected = 3
    assert answer == expected
