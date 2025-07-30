from sample2 import get_intro, get_first_letter, get_name_slice, can_vote, list_cars, print_stars

def test_get_intro():
    assert get_intro("Arjunreddy", 24) == "My name is Arjunreddy and I am 24 years old"

def test_get_first_letter():
    assert get_first_letter("Arjunreddy") == "A"

def test_get_name_slice():
    assert get_name_slice("Arjunreddy") == "Arjun"

def test_can_vote():
    assert can_vote(24) == "You can vote"
    assert can_vote(17) == "Better Luck next time"

def test_list_cars():
    assert list_cars(["BMW", "AUDI"]) == ["BMW", "AUDI"]

def test_print_stars():
    assert print_stars(5) == ["*", "**", "***", "****"]
