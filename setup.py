from setuptools import setup, find_packages

setup(
    name='focalors_extension',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'focalors=focalors.main:main',
        ],
    },
    install_requires=[
        # todo- 필요 패키지 추가
    ],
)
