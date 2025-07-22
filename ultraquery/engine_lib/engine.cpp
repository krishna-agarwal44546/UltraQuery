#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <unordered_map>
#include <iomanip>
using namespace std;

class CSVReader {

private:
    string filename;
    int rowlimit;
    unordered_map<string, int> columnIndexMap;
    vector<string> columnNames;
    vector<vector<string>> dataRows;

    string trim(const string& str) {
        size_t start = str.find_first_not_of(" \t\r\n");
        size_t end = str.find_last_not_of(" \t\r\n");
        return (start == string::npos) ? "" : str.substr(start, end - start + 1);
    }

public:
    CSVReader(const char* file, int limit) : filename(file), rowlimit(limit) {}

    bool load() {
        ifstream file(filename);
        if (!file) {
            cerr << "Error in file opening.\n";
            return false;
        }

        string line;
        if (!getline(file, line)) {
            cerr << "File is either empty or header can't be read.\n";
            return false;
        }

        istringstream headerStream(line);
        string col;
        int index = 0;

        while (getline(headerStream, col, ',')) {
            col = trim(col);
            columnNames.push_back(col);
            columnIndexMap[col] = index++;
        }

        int count = 0;
        while (getline(file, line)) {  
            istringstream rowStream(line);
            vector<string> row;
            string cell;

            while (getline(rowStream, cell, ',')) {
                row.push_back(trim(cell));
            }

            dataRows.push_back(row);
            if (++count == rowlimit) break;  
        }

        file.close();
        return true;
    }

    void printColumn(const string& column) const {  
        if (columnIndexMap.find(column) == columnIndexMap.end()) {
            cout << "Error: Column \"" << column << "\" not found.\n";
            return;
        }

        int colindex = columnIndexMap.at(column);
        cout << "\nColumn: " << columnNames[colindex] << "\n\n";

        for (const auto& row : dataRows) {
            if (colindex < row.size()) {
                cout << row[colindex] << "\n";
            } else {
                cout << "[Missing]\n";
            }
        }
    }

    void listColumns() const {  
        cout << "Available Columns:\n";
        for (const auto& col : columnNames) {
            cout << col << endl;
        }
    }

    void getdata() const{
        cout<<"Here is your full Data.\n";
        for (const auto& col : columnNames){
            cout<<col<<"| ";
        }
        cout<<"\n\n\n";
        for(const auto& row:dataRows){
            for(const auto& cell:row){
                cout<<cell<<"| ";
            }
        }
    }
    void Dataframe() {
        vector<size_t> colwidths(columnNames.size(), 0);

    
        for (size_t i = 0; i < columnNames.size(); i++) {
            colwidths[i] = columnNames[i].length();
            for (const auto& row : dataRows) {
                if (i < row.size()) {
                    colwidths[i] = max(colwidths[i], row[i].length());
            }
        }
    }

    
        for (size_t i = 0; i < columnNames.size(); i++) {
            cout << "| " << left << setw(colwidths[i]) << columnNames[i] << " ";
    }
        cout << "|\n";

    
        for (size_t i = 0; i < columnNames.size(); i++) {
            cout << "|" << string(colwidths[i] + 2, '-') ;
    }
        cout << "|\n";

    
        for (const auto& row : dataRows) {
            for (size_t i = 0; i < columnNames.size(); i++) {
                cout << "| ";
                if (i < row.size()) {
                    cout << left << setw(colwidths[i]) << row[i] << " ";
            }   else {
                    cout << left << setw(colwidths[i]) << "[Missing]" << " ";
            }
        }
            cout << "|\n";
    }
            for (size_t i = 0; i < columnNames.size(); i++) {
            cout << "|" << string(colwidths[i] + 2, '-') ;
    }
}

};
extern "C"{
    void readcsv(const char* csv,int limit){
    CSVReader reader(csv,limit);
    if (!reader.load()) return exit(EXIT_FAILURE);

    reader.listColumns();  

    string column;
    cout << "Enter column name: ";
    cin >> ws;
    getline(cin, column);
    column.erase(0, column.find_first_not_of(" \t\r\n"));
    column.erase(column.find_last_not_of(" \t\r\n") + 1);


    reader.printColumn(column);
}
    void columnsget(const char* csv){
    CSVReader reader(csv,10000000);
    if (!reader.load()) return exit(EXIT_FAILURE);

    reader.listColumns();


    }
    void getdata(const char* csv,int limit){
    CSVReader reader(csv,limit);
    if (!reader.load()) return exit(EXIT_FAILURE);
    string column;
    cout << "Enter column name: ";
    cin >> ws;
    getline(cin, column);
    column.erase(0, column.find_first_not_of(" \t\r\n"));
    column.erase(column.find_last_not_of(" \t\r\n") + 1);


    reader.printColumn(column);
    }

    void dataframe(const char* csv,int limit){
    CSVReader reader(csv,limit);
    if (!reader.load()) return exit(EXIT_FAILURE);

    reader.Dataframe();

    }


   // reader.getdata();


}


int main() {
    return 0;

}