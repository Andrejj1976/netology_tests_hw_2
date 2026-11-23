import pytest
from main import circle_calculations, check_auth, unique_names


@pytest.mark.parametrize(
    "radius, expected",
    [
        (5, (31.4, 78.5)),
        (1, (6.28, 3.14)),
        (10, (62.8, 314.0)),
        (0, (0.0, 0.0)),
    ],
)
def test_circle_calculations(radius, expected):
    assert circle_calculations(radius) == expected


@pytest.mark.parametrize(
    "login, password, expected",
    [
        ("admin", "password", "Добро пожаловать"),
        ("user", "password", "Доступ ограничен"),
        ("admin", "123", "Доступ ограничен"),
        ("", "", "Доступ ограничен"),
        ("Admin", "password", "Доступ ограничен"),
    ],
)
def test_check_auth(login, password, expected):
    assert check_auth(login, password) == expected


@pytest.mark.parametrize(
    "mentors_list, expected",
    [
        (["Евгений Шмаргунов", "Олег Булыгин", "Евгений Грязнов"], "Евгений, Олег"),
        (["Азамат Искаков", "Адилет Асканжоев", "Александр Иванов"], "Адилет, Азамат, Александр"),
        (["Иван Бочаров", "Иван Маркитан"], "Иван"),
        ([], ""),
    ],
)
def test_unique_names(mentors_list, expected):
    assert unique_names(mentors_list) == expected