import os
for (root,dirs,files) in os.walk('D:',topdown=True):
  print("Directory path: %s"%root)
  print("Directory Names: %s"%dirs)
  print("Files Names: %s"%files)
