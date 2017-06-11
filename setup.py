from setuptools import setup, find_packages

setup(
    name='u2b2bili',
    version=1.0,
    description='Download video from Youtube and rip it.',
    long_description='Download video and subtitles from Youtube and burn subtitles into the video.',
    author='Chigusa',
    maintainer='Chigusa',
    maintainer_email='c02110210610204@gmail.com',
    license='LGPL',
    packages=find_packages(),
    scripts=['u2b2bili.py'],
    install_requires=['youtube-dl']
)
