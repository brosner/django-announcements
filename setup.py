
from distutils.core import setup

setup(
    name = "django-announcements",
    version = __import__("announcements").__version__,
    author = "Brian Rosner",
    author_email = "brosner@gmail.com",
    description = "Announcements for your Django powered website.",
    long_description = open("README").read(),
    license = "MIT",
    url = "http://code.google.com/p/django-announcements",
    packages = [
        "announcements",
    ],
)
