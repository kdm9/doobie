from setuptools import setup
import versioneer
import os

versioneer.VCS = 'git'
versioneer.versionfile_source = '_version.py'
versioneer.versionfile_build = '_version.py'
versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'doobie-'

desc = """
doobie: Hash in a pipe!
"""

if os.path.exists('README.md'):
    with open('README.md') as rm_fh:
        desc = rm_fh.read()

test_requires = [
    "coverage==3.7.1",
    "nose==1.3.0",
    "pep8==1.4.6",
    "pylint==1.0.0",
]

setup(
    name="doobie",
    py_modules=['doobie', ],
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
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
