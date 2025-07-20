import argparse
import UltraQuery_core.internal as internal
import os

def main():

    parser=argparse.ArgumentParser(description="Welcome to UltraQuery CLI Tool")
    parser.add_argument("-f","--file",help="type -f to enter the file")
    parser.add_argument("-v","--view",action="store_true",help="type -v to view the dataframe")
    parser.add_argument("-col","--columns",help="type -col to view the columns list")
    parser.add_argument("-vc","--column_data")
    parser.add_argument("-plt","--plot",action="store_true",help="Plot the graphs")
    parser.add_argument("-typ","--type",help="Available type of graphs :\n['bar','pie','line','scatter','histogram']")
    parser.add_argument("-x","--xAxis",help="Give the X axis here")
    parser.add_argument("-y","--yAxis",help="give the y axis here" )
    parser.add_argument("-df","--DataFrame",help="Use -df for building dataframes")
    parser.add_argument("-l","--limit",type=int,help="type -l to limit the number of rows")
    args=parser.parse_args()
    
    
    if args.view:
        internal.UltraQuery().viewfile(args.file,args.limit)
    
    if args.columns:
        internal.UltraQuery().viewcolumn(args.file,100)
    
    if args.column_data:
        internal.UltraQuery().viewdata(args.file,args.limit)

    if args.DataFrame:
        internal.UltraQuery().dataframe(args.file,args.limit)
    
    if args.plot:
        internal.UltraQuery().plot(args.file,args.xAxis,args.yAxis,args.type)

