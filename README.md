## p4python-2021.1.2265002-py2.7-win-amd64
Tested on Maya 2018, 2020

Built with 2023.2 Perforce C++ API

#### Usage:
Extract to any PYTHONPATH folder, name the directory as p4python
```
import p4python.P4 as P4
p4 = P4.P4()
p4.connect()
```
Alternatively, you can just copy P4.py and P4API.pyd directy to any folder in your PYTHONPATH environment without __init__.py
In this case usage will be a bit different
```
from P4 import P4
p4 = P4()
p4.connect()
```
Check [P4 Documentation](https://www.perforce.com/manuals/p4python/Content/P4Python/python.programming.html) for more info
