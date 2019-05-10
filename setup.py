from setuptools import setup

setup(
    name='neat-python-fast',
    version='0.1',
    author='cesar.gomes, mirrorballu2, Moraxno',
    author_email='nobody@nowhere.com',
    maintainer='Moraxno',
    maintainer_email='robertbock.98@googlemail.com',
    url='https://github.com/RobertNiklasBock/neat-python',
    license="BSD",
    description='A faster NEAT (NeuroEvolution of Augmenting Topologies) implementation',
    long_description='Python implementation of NEAT (NeuroEvolution of Augmenting Topologies), a method ' +
                     'developed by Kenneth O. Stanley for evolving arbitrary neural networks.',
    packages=['neatfast', 'neatfast/iznn', 'neatfast/nn', 'neatfast/ctrnn'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering'
    ],
    install_requires=[
        'numpy'
    ]
)
