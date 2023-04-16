import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-gui-tutorials',
    version='0.0.1',
    description='Python GUI tutorials',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rusu24edward/python-gui-tutorials',
    author='Ephraim Rusu',
    author_email='serephraim24@gmail.gov',
    license='BSD 3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Education',
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib',
        'numpy',
        'opencv-python',
        'pysimplegui'
    ],
    python_requires='>=3.7, <3.11',
    # entry_points={
    #     'console_scripts': [
    #         'abmarl=abmarl.scripts.scripts:cli'
    #     ]
    # },
)
