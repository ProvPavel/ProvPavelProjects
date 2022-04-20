from yandex_testing_lesson import reverse
import pytest


def test_empty():
    assert reverse('') == ''


def test_one():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('rats live on no evil star') == 'rats live on no evil star'


def test_usual_string():
    assert reverse('not a palindrome') == 'emordnilap a ton'


def test_not_iterable():
    with pytest.raises(TypeError):
        reverse(123)


def test_iterable():
    with pytest.raises(TypeError):
        reverse((1, 2, 3))
