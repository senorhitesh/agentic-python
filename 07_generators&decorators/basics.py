def courses():
    yield "Course 1: Python Development"
    yield "Course 2: Frotend Intenship"
    yield "Course 3: Maga-Dent"

course = courses()


print(next(course))