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
        "announcements.templatetags",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
