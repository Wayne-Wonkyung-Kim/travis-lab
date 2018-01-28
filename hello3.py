
def getCharNum( filename ):
    input = io.open( filename, "r" )
    count = 0

    x = input.readline()
    while x:
        x = x.strip()
        count += len( x )
        x = input.readline()

    return count


def test_getCharNum():
    assert getCharNum( "input.txt" ) == 6



