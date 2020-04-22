
#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    print ("foo self main run")
else:
    print ("foo package imported")

from . import mod1
from . import mod2
__all__ = ["print_mod1", "print_mod2"]
