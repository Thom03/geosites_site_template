import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="site1",
    version="0.1",
    author="Thomas Muteti",
    author_email="",
    description="site1, a GeoNode Geosites project",
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 1 - Planning',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/site1/site1',
    include_package_data=True,
    zip_safe=False,
   
)
