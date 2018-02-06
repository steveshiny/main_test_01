import logging
from sub_test_02 import test_something

logging.info("test from main_01: %s" % test_something.sub_id)
print("test from main_01: %s" % test_something.sub_id)
