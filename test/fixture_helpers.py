import os


def fixture_path(name):
    basepath = os.path.dirname(os.path.abspath(__file__))
    filename = "%s.json" % name
    return os.path.join(basepath, "fixtures", filename)
