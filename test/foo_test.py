#!/usr/bin/env python

import sys
sys.stderr.write("\n".join(sys.path))

import unittest
import rospy

from bug_python_test_deps.foo import *

class FooTest(unittest.TestCase):
    def foo_test(self):
      return True

if __name__ == '__main__':
    import rostest
    rospy.init_node('test_foo')
    rostest.rosrun('bug_python_test_deps', 'test_foo', FooTest)