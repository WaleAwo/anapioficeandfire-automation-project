### Python 🐍
- Ensure you have a recent version of Python (preferably 3.7 or newer) installed and configured as your interpreter.
- Download Python [here](https://www.python.org/downloads/).
- Windows installation [here](https://www.youtube.com/watch?v=JJQW3GPnzQ8). MacOS installation [here](https://www.youtube.com/watch?v=nVeg5nnQF90).

### IDE (Integrated Development Environment) 🖥️
- Pycharm is a widely used IDE for Python development.
- Download PyCharm [here](https://www.jetbrains.com/pycharm/).
- Windows installation [here](https://www.youtube.com/watch?v=EWTLWH-dH90). MacOS installation [here](https://www.youtube.com/watch?v=SzP7XJd66qM).

### Packages 📦
- The following python packages are required to run the tests:
  * [pytest](https://pypi.org/project/pytest/) - Testing framework
  * [requests](https://pypi.org/project/requests/) - HTTP request library
- After cloning this repository, run `pip install -r requirements.txt` from the project root to install the necessary packages.

### Tasks 🗒️
API documentation [here](https://anapioficeandfire.com/Documentation).
- **Task 1**: Write a code solution that finds the sum of the total number of pages of all the books that are available in the API.
- **Task 2**: Design a test automation framework for the API with a language of your choice, covering only regression test scenarios.

### Running the tests ✅
- **CMD**
  * Running the tests is as easy as running `python -m pytest <test_file_name.py>` from the project root, e.g. `python -m pytest test_task_one.py`
  * To run the regression suite, enter the following command from the project root `python -m pytest -vm regression`
- **IDE**
  * Open the test file `test_task_one.py`, click the file menu option then click `Run`
