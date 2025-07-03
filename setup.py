from setuptools import find_packages, setup

package_name = 'tcs34725'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/tcs34725.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yamato',
    maintainer_email='yamato@todo.todo',
    description='A ROS2 package for the TCS34725 color sensor.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'color_publisher = tcs34725.example.color_publisher:main',
        ],
    },
)