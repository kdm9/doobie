from setuptools import setup

desc = """
doobie: Hash in a pipe!
"""

test_requires = [
    "coverage==3.7.1",
    "nose==1.3.0",
    "pep8==1.4.6",
    "pylint==1.0.0",
]

setup(
    name="doobie",
    py_modules=['doobie', ],
    version="0.0.1",
    install_requires=[],
    tests_require=test_requires,
    description=desc,
    author="Kevin Murray",
    author_email="spam@kdmurray.id.au",
    url="https://github.com/kdmurray91/doobie",
    keywords=["hash", "pipeline", "md5", "sha512", "sha256"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later " +
            "(GPLv3+)",
    ],
)
