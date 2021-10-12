import pytest


def test_1():
    x = 10
    y = 10
    assert x == y


def test_2():
    name = "Jodi"
    title = "Jodi is a foodie"
    assert name in title


def test_3():
    name = "jenkins"
    title = "Jenkins is a CI server"
    assert name in title, "Title does not match"
