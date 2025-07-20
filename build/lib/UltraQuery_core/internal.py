import ctypes
import time
import os
import platform
import sys
import UltraQuery_core.plotengine as ple

# Determine platform and correct DLL/SO path
engine_dir = os.path.join(os.path.dirname(__file__), "engine_lib")
engine_path = os.path.join(engine_dir, "engine.dll") if platform.system() == "Windows" else os.path.join(engine_dir, "engine.so")

if not os.path.exists(engine_path):
    print(f"❌ Critical: Engine file not found at {engine_path}")
    sys.exit(1)

clib = ctypes.CDLL(engine_path)

clib.readcsv.argtypes = [ctypes.c_char_p, ctypes.c_int]
clib.columnsget.argtypes = [ctypes.c_char_p]
clib.getdata.argtypes = [ctypes.c_char_p, ctypes.c_int]
clib.dataframe.argtypes = [ctypes.c_char_p, ctypes.c_int]

class UltraQuery:
    def __init__(self):
        pass

    def viewcolumn(self, csv):
        return clib.columnsget(csv.encode())

    def viewdata(self, csv, limit):
        return clib.getdata(csv.encode(), limit if limit else 100)
    
    def df(self,csv,limit):
        if not os.path.exists(csv):
            print(f"❌ File '{csv}' not found.")
            sys.exit(1)
        return clib.dataframe(csv.encode(),limit)
    

    def plot(self, file, xcol, ycol, graph_type):
        fun = ple.UltraQuery_plot(file, xcol, ycol)
        match graph_type:
            case "bar":
                fun._bar()
            case "pie":
                fun._pie()
            case "line":
                fun._line()
            case "histogram":
                fun._histogram()
            case "scatter":
                fun._scatter()
            case _:
                print("❌ Invalid plot type. Supported types: bar, pie, line, histogram, scatter.")
