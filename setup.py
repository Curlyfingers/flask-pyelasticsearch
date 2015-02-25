from setuptools import setup


with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='Flask-PyElasticSearch',
    version='0.1',
    download_url='https://github.com/jace/flask-pyelasticsearch',
    license='BSD',
    author='Peter Flood - Kazoup, Kiran Jonnalagadda',
    author_email='jace@pobox.com',
    description='ElasticSearch for Flask',
    long_description=long_description,
    py_modules=['flask_pyelasticsearch'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'pyelasticsearch',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
