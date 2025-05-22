from setuptools import setup, find_packages

setup(
    name="Deskweblib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "robotframework",
        "selenium",
        "pyautogui",
        "pillow",
        "opencv-python",
        "numpy",
    ],
    entry_points={
        'robotframework_library': [
            'Deskweblib = Deskweblib.__init__:DeskWebLib'
        ]
    },
    author="Reshma Banu",
    description="Robot Framework library combining Selenium and image-based desktop keywords",
    license="MIT",
)
