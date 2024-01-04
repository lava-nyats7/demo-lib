from setuptools import setup, find_packages
setup(
    name='sniper_common_lib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'kazoo==2.9.0',
        'redis==5.0.1',
        'requests==2.28.1',
        'confluent-kafka==1.7.0',
        'fastapi==0.103.0',
        'elasticsearch==7.12.0',
    ],
)
