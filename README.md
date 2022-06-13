# PythonUnitTest
unit test in python example

to run test use below command
```
python3 -m unittest discover
```
### you should have setup.py file in project folder 

```
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"src"
)
sys.path.append(SOURCE_PATH)
```
### you should have empty __init__.py file inside src and test folder
