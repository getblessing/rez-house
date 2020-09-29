
name = "house"

version = "1.0.0"

description = "Studio/Site-wide production environment"

requires = []

build_command = False


def commands():
    env = globals()["env"]

    # Ozark database with auth
    # ...

    # Pipeline database with auth
    env.HOUSE_PIPELINE_MONGO = "localhost:27017"

    # Licenses server
    # ...
