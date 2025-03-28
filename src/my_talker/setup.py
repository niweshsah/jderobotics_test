from setuptools import find_packages, setup

package_name = 'my_talker'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='niweshsah',
    maintainer_email='sahniwesh@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
     entry_points={
        'console_scripts': [
            'publisher = my_talker.publisher:main',  # Ensure this points to `main()` in publisher.py
            'subscriber = my_talker.subscriber:main',  # If you also have a subscriber
        ],
    },
)
