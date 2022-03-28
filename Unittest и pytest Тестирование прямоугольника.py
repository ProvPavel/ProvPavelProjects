from yandex_testing_lesson import Rectangle
import pytest


def test_empty():
    with pytest.raises(TypeError):
        Rectangle()


def test_empty_second():
    with pytest.raises(TypeError):
        Rectangle(1)


def test_list_first():
    with pytest.raises(TypeError):
        Rectangle([1], 1)


def test_dictionary_first():
    with pytest.raises(TypeError):
        Rectangle({1}, 1)


def test_dictionary_second():
    with pytest.raises(TypeError):
        Rectangle(1, {1})


def test_not_int1():
    with pytest.raises(TypeError):
        Rectangle('42', 42)


def test_err_int1():
    with pytest.raises(ValueError):
        Rectangle(-42, 42)


def test_not_int2():
    with pytest.raises(TypeError):
        Rectangle(42, '42')


def test_err_int2():
    with pytest.raises(ValueError):
        Rectangle(42, -42)


def test_list_second():
    with pytest.raises(TypeError):
        Rectangle(1, [1])


def test_correct():
    assert Rectangle(2, 3).__class__ == Rectangle


def test_s():
    assert Rectangle(2, 3).get_area() == 6


def test_sym():
    assert Rectangle(2, 3).get_perimeter() == 10
