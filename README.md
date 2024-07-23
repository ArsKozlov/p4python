## Latest p4python module for Maya 2018-2025

Some Python releases are deprecated, this is the list of the latest available modules for Maya 2018-2022:

![Maya Version](https://img.shields.io/badge/Maya-2018%20%7C%202019%20%7C%202020-white) ![P4 Version](https://img.shields.io/badge/p4python-2021.1.2265002-yellow) ![Python Version](https://img.shields.io/badge/py-2.7-blue)

![Maya Version](https://img.shields.io/badge/Maya-2022-white) ![P4 Version](https://img.shields.io/badge/p4python-2023.1.2545777-yellow) ![Python Version](https://img.shields.io/badge/py-3.7-blue)

![Maya Version](https://img.shields.io/badge/Maya-2023%20%7C%202024%20%7C%202025-white) ![P4 Version](https://img.shields.io/badge/p4python-2024.1.2625398-green) ![Python Version](https://img.shields.io/badge/py-3.9%20%7C%203.10%20%7C%203.11-blue)

### Installation:

#### First method:
Add folder path to MAYA_MODULE_PATH variable. It will work for all Maya versions. Check p4python.mod file for the details

#### Second method:
If you don't want to download all the versions, you can just copy P4.py and P4API.pyd directly to any folder in your PYTHONPATH environment. The *.pyd file should match Maya's Python version.

### Usage:
```
from P4 import P4
p4 = P4()
p4.connect()
```

Check [P4 Documentation](https://www.perforce.com/manuals/p4python/Content/P4Python/python.programming.html) for more info
