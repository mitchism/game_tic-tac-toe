from setuptools import setup, find_packages
import pathlib

#with open("README.md", "r") as readme_file:
#    readme = readme_file.read()
here = pathlib.Path(__file__).parent.resolve()
readme = (here / "README.md").read_text(encoding="utf-8")

requirements = ["ipython"]

setup(
    name="tictactoe-by-msm",
    version="1.4.0a1", 
    #ver 1.3.1.2 first stable alpha iteration
    #ver 1.4 upon merge of single player feature branch
    author="Mitch Miller",
    author_email="mitchell.shaw.miller@gmail.com",
    description="Tic-tac-toe console game in Python with single-player and multiplayer",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/mitchism/tictactoe_by_msm",
    packages=find_packages(),
    install_requires=requirements,

    project_urls={  # Optional
        "project GitHub": "https://github.com/mitchism/tictactoe_by_msm",
        "author url": "http://mitchellsmiller.weebly.com/",
    },
    classifiers=[
        "Classifier: Environment :: Console (Text Based)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 3 - Alpha", #(3-alpha,4-beta,5-production/stable)
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9.7",
    ],
    keywords="Tic-Tac-Toe, Tic Tac Toe, Single player, Game, Console Game, Text based game",  # Optional
    packages=setuptools.find_packages(),
    #package_dir={"": "tictactoe_game"},  
    #packages=find_packages(where="tictactoe_game"),
    python_requires=">=3.7, <4",
)
