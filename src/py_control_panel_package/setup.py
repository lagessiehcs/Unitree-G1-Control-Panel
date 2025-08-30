import os
import subprocess
from glob import glob
from setuptools import find_packages, setup
from setuptools.command.build_py import build_py as build_py_orig

package_name = 'py_control_panel_package'


ui_file = os.path.join(package_name, "G1ControlPanel.ui")
py_file = os.path.join(package_name, "g1_control_panel.py")
subprocess.run(["pyside6-uic", ui_file, "-o", py_file], check=True)

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
            'control_panel = py_control_panel_package.main_window:main',
        ],
    },
    package_data={
        'py_control_panel_package': [
            "utils/lib/*",
            "utils/*" 
        ],
    },
)
