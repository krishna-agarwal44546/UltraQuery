import argparse
import ultraquery.UltraQuery as uq

def main():

    parser=argparse.ArgumentParser(description="Welcome to UltraQuery CLI Tool")
    parser.add_argument("-f","--file",help="type -f to enter the file")
    parser.add_argument("-col","--columns",help="type -col to view the columns list")
    parser.add_argument("-vc","--column_data")
    parser.add_argument("-plt","--plot",action="store_true",help="Plot the graphs")
    parser.add_argument("-typ","--type",help="Available type of graphs :\n['bar','pie','line','scatter','histogram']")
    parser.add_argument("-x","--xAxis",help="Give the X axis here")
    parser.add_argument("-y","--yAxis",help="give the y axis here" )
    parser.add_argument("-df","--DataFrame",action="store_true",help="Use -df for building dataframes")
    parser.add_argument("-l","--limit",type=int,help="type -l to limit the number of rows")
    parser.add_argument("-sql","--SQL",action="store_true",help="for SQL databases")
    parser.add_argument("-table","--table",help="Type -table for entering the table name")
    args=parser.parse_args()
    
    if args.columns:
        uq.UltraQuery().viewcolumn(args.file,100)
    
    if args.column_data:
        uq.UltraQuery().viewdata(args.file,args.limit)

    if args.DataFrame:
        uq.UltraQuery().df(args.file,args.limit)

    if args.SQL:
        uq.UltraQuery().viewsql(args.file,args.table,args.limit)
    
    if args.plot:
        uq.UltraQuery().plot(args.file,args.xAxis,args.yAxis,args.type)

