from collection.mix import requestPost
import common.common
import time


print("################## START #######################")
print(common.common.current_time())
print("------------------")

execSet = (170, 0, "twice")
execSet2 = (10, 0, "kang")

requestPost(execSet2)

print("------------------")
print("################## END #######################")
print(common.common.current_time())