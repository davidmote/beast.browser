from setuptools import setup, find_packages
import os

version = '0.1.2'

setup(
    name='beast.browser',
    version=version,
    description='Browser tools for Beast Core Products',
    classifiers=[
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/beast.browser',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'':'src'},
    namespace_packages=['beast'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'five.grok',
        'plone.z3cform',
        'z3c.form',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
