from setuptools import setup, find_packages

setup(
    name="math_quiz",  # Name of your project
    version="0.1",  # Version number
    packages=find_packages(),  # Automatically find packages in math_quiz/
    install_requires=[  # List your dependencies here (leave empty if none)
        # Example: 'requests',
    ],
    entry_points={  # Allow `pip` to register your project as a command line tool
        'console_scripts': [
            'math_quiz = math_quiz.math_quiz:math_quiz',  # Entry point to your math quiz game
        ],
    },
    include_package_data=True,  # Include additional files like `README.md`
    classifiers=[  # Add some metadata for your project
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
    ],
)
