import pytest

def capitalize_case(x):
    if not isinstance(x, str):
        raise TypeError("Please pass \'x\' value as a string.")

    return x.capitalize()

def test_capitalize_case():
    assert capitalize_case("semaphore") == 'Semaphore'

# Testing type of input passed to capitalize_case()
def test_raise_type_error_capitalize():
    # import pdb; pdb.set_trace()
    with pytest.raises(TypeError):
        capitalize_case(3)

def main():
    print "Inside main function, yet to come"
    x = "ram"
    result = capitalize_case(x)
    print "Capitalized x: ", result

if __name__ == "__main__":
    main()
