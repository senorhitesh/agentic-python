import arrow

now = arrow.now()
print(now)

from collections import namedtuple
chaiProfile = namedtuple("ChaiProfile", ["name", "age", "favorite_tea"])
print(chaiProfile)