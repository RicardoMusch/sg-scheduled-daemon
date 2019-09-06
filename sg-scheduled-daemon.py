import os
import sys
import sg_connection




plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")
"Insert plugins folder as path"
sys.path.insert(0, plugin_dir)


import glob
plugin_files = glob.glob(os.path.join(plugin_dir, "*.py"))
print plugin_files
for plugin in plugin_files:
    try:
        plugin = os.path.basename(plugin).split(".")[0]
        __import__(plugin)
    except Exception as e:
        print "Error: Could not import", plugin
        print e
        print " "


