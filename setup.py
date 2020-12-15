from setuptools import setup, find_packages
import pathlib


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

version = {}
ver_text = (here / 'plot_styles' / '__version.py').read_text(encoding='utf-8')
exec(ver_text, version)

setup(
    name='plot_styles',
    version=version['__version__'],
    description=(
        'Assorted matplotlib styles'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/asongtoruin/plot_styles',
    author='Adam Ruszkowski',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=find_packages(),
    package_data={
      'plot_styles': ['data/*.mplstyle'],
    },
    python_requires='>=3, <4',
    install_requires=[
        'matplotlib<4'
    ],
    project_urls={
        # 'Documentation': 'https://asongtoruin.github.io/palbums/',
        'Source': 'https://github.com/asongtoruin/plot_styles/',
    }, 
)