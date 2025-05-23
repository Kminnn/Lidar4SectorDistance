from setuptools import find_packages, setup

package_name = 'lidar_processing'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
         ['launch/scan_and_processing.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khemin',
    maintainer_email='khemin@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sector_distance_node = lidar_processing.sector_distance_node:main',
        ],
    },
)
