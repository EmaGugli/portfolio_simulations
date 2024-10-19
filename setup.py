from setuptools import setup, find_packages

setup(
    name='portfolio_simulations',
    version='0.0.0',
    description='Simulation of portfolio returns',
    long_description=open('README.md').read(),
    url='https://github.com/EmaGugli/portfolio_simulations',
    author='Emanuele Gugliandolo',
    author_email='emanuelegugliandolo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.12',
    ],
    keywords='portfolio simulations',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        'numpy',
        'matplotlib',
        'yfinance',
    ],
    extras_require={
        'dev': [
            'check-manifest',
        ],
        'test': [
            'coverage',
        ],
    },
    package_data={
        '': ['README.md', 'LICENSE'],
    },
    entry_points={
        'console_scripts': [
            'portfolio_simulation=portfolio_simulations.cli:main',
        ],
    },
)