import os, sys

try:
    from setuptools import setup
    from setuptools.command.install import install as _install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install as _install


def _post_install(install_lib):
    import shutil
    shutil.copy('pytwister.pth', install_lib)

class install(_install):
    def run(self):
        self.path_file = 'pytwister'
        _install.run(self)
        self.execute(_post_install, (self.install_lib,),
                     msg="Running post install task")

version = "0.1"

setup(
    cmdclass={'install': install},
    name="pytwister",
    version=version,
    download_url='',
    packages = ["pytwister", "pytwister.codec"],
    author='Otto Fajardo',
    author_email='pleasecontact@ongithub.com',
    url="http://github.com/ofajardo/pytwister",
    license='MIT',
    description="Python with a twist of R syntax.",
    long_description="Python with a twist of R syntax. Visit our webpage for more information: https://github.com/ofajardo/pytwister",
    keywords='python string interpolation interpolate ruby codec',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
