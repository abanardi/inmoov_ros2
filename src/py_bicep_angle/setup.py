from setuptools import setup

package_name = 'py_bicep_angle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Andrew Banardi',
    maintainer_email='abanardi0@gmail.com',
    description='Calculates and sends bicep angles using OpenCv in Python',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_bicep_angle.angle_publisher:main',
            'listener = py_bicep_angle.angle_subscriber:main',
        ],
    },
)
