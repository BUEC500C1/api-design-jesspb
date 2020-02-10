from extra_func import getCityFromCode
from extra_func import getCityFromAirport

def test_code1():
    assert getCityFromCode("GB-0058") == "Boston"

def test_code2():
    assert getCityFromCode("FA91") == "Orlando"

def test_code_fail():
    assert getCityFromCode("YAH-Y33T") == ""

def test_airport1():
    assert getCityFromAirport("Sarasota Memorial Hospital North Port ER Heliport") == "North Port"

def test_airport2():
    assert getCityFromAirport("Aberdeen Airport") == "Aberdeen"

def test_airport_fail():
    assert getCityFromAirport("Take The Gluten Out The Bread") == ""
