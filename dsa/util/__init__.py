if __name__ == "__main__":
    print("this module is for import only")
    exit()

import sys
from .math import dumb_add

# print(__name__)
# print(__package__)
# print(__file__) # only for package, not module
# print(sys.path[0])
