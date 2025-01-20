import sys
from unittest.mock import patch

with patch("sys.argv", ["file.py", "-h"]):
    print(sys.argv)