import ctypes
import sqlite3
import os
import platform
import sys
import csv
import io
import ultraquery.plotengine as ple

# Determine platform and correct DLL/SO path
engine_dir = os.path.join(os.path.dirname(__file__), "engine_lib")
engine_path = os.path.join(engine_dir, "engine.dll") if platform.system() == "Windows" else os.path.join(engine_dir, "engine.so")
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

if not os.path.exists(engine_path):
    print(f"❌ Critical: Engine file not found at {engine_path}")
    sys.exit(1)

clib = ctypes.CDLL(engine_path)
clib.readcsv.argtypes = [ctypes.c_char_p, ctypes.c_int]
clib.columnsget.argtypes = [ctypes.c_char_p]
clib.getdata.argtypes = [ctypes.c_char_p, ctypes.c_int]
clib.dataframe.argtypes = [ctypes.c_char_p, ctypes.c_int]

def listcolumn(csvfile,x: str):
    a=[]
    ans=[]
    with open(csvfile,"r",newline="") as f:
        sample = f.read(1024)  # Read a small chunk of the file
        dialect = csv.Sniffer().sniff(sample)
    with open(csvfile,"r") as f:
        if dialect.delimiter==',':
            reader=csv.DictReader(f,delimiter=',')
            for column in reader:
                a.append(list(column.values()))
            z=list(column.keys())
    
        elif dialect.delimiter=='\t':
            reader=csv.DictReader(f,delimiter='\t')
            for column in reader:
                m=list(column.values())
                a.append(m)
            z=list(column.keys())
        i=0
        while(i<len(z)):
            if z[i]==x:
                i=i
                break
                
            else:
                i=i+1
    
        p=0
        while(p<len(a)):
            ans.append(a[p][i])
            p=p+1
    return ans


def columns(csvfile):
    with open(csvfile,"r",newline="") as f:
        sample = f.read(1024)  # Read a small chunk of the file
        dialect = csv.Sniffer().sniff(sample)
    with open(csvfile,"r") as f:
        if dialect.delimiter==',':
            reader=csv.DictReader(f,delimiter=',')
            for column in reader:
                z=list(column.keys())
    
        elif dialect.delimiter=='\t':
            reader=csv.DictReader(f,delimiter='\t')
            for column in reader:
                m=list(column.values())
            z=list(column.keys())
    return z
    
class UltraQuery:
    def __init__(self):
        pass

    def read_dict(self,dict: dict):
        keys=list(dict.keys())
        values=list(dict.values())
        with open("read.csv","a") as f:
            i=0
            while(i<len(keys)):
                if i==len(keys)-1:
                    f.write(f"{keys[i]}\n")
                else:
                    f.write(f"{keys[i]},")
                i=i+1

            k=0
            while(k<len(values[0])):
                j=0
                while(j<len(values)):
                    if j==len(values)-1:
                        f.write(f"{values[j][k]}\n")
                    else:
                        f.write(f"{values[j][k]},")
                    j=j+1
                k=k+1

        UltraQuery.df(self,"read.csv",len(values[0]))
        os.remove("read.csv")

    def viewcolumn(self, csv):
        return clib.columnsget(csv.encode())
    
    def viewdata(self,csv,col):
        for i in listcolumn(csv,col):
            print(f"{i}")

    def df(self,csv,limit):
        if not os.path.exists(csv):
            print(f"❌ File '{csv}' not found.")
            sys.exit(1)
        return clib.dataframe(csv.encode(),limit)

    def viewsql(self,file,table,limit):
        conn = sqlite3.connect(file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        column_names = [description[0] for description in cursor.description]
        rows = cursor.fetchall()
        i=0
        while(i<len(column_names)):
            with open("sample.txt","a") as f:
                if(i==len(column_names)-1):
                    f.write(f"{column_names[i]}\n")
                else:
                    f.write(f"{column_names[i]},")
            i=i+1
        for row in rows:
             
            with open("sample.txt","a") as f:
                i=0
                while(i<len(column_names)):
                    if(i==len(column_names)-1):
                        f.write(f"{row[i]}\n")
                    else:
                        f.write(f"{row[i]},")
                    i=i+1
        UltraQuery.df(self,"sample.txt",limit)
        os.remove("sample.txt")
    

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
