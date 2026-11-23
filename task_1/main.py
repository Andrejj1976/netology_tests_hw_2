def circle_calculations(r: float) -> tuple[float, float]:
    pi = 3.14
    circle_length = round(2 * pi * r, 2)
    area = round(pi * (r ** 2), 2)
    return circle_length, area


def check_auth(login: str, password: str) -> str:
    if login == 'admin' and password == 'password':
        result = 'Добро пожаловать'
    else:
        result = 'Доступ ограничен'
    return result


def unique_names(mentors: list[str]) -> str:
    names = set()
    for mentor in mentors:
        name_parts = mentor.split()
        name = name_parts[0]
        names.add(name)

    sorted_names = sorted(list(names))
    result = ", ".join(sorted_names)
    return result