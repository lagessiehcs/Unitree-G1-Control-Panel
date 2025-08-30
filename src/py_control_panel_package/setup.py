import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'py_control_panel_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='quan',
    maintainer_email='lagessiehcs.git@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'control_panel = py_control_panel_package.main:main',
        ],
    },
    package_data={
        'human_position_publisher': [
            "*", 
        ],
    }


)
