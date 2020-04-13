import os
import sys

curr_dir = os.path.dirname(__file__)
if curr_dir not in sys.path:
    sys.path.append(curr_dir)