from setuptools import setup, find_packages

setup(
    name='pynotification',
    version='1.0.0',
    description='A Python library to send notifications',
    url='https://github.com/jonghwanhyeon/python-notification',
    author='Jonghwan Hyeon',
    author_email='hyeon0145@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Topic :: System :: Monitoring',
    ],
    # Note that this is a string of words separated by whitespace, not a list.
    keywords='notification',
    packages=find_packages(),
    install_requires=['requests'],
)