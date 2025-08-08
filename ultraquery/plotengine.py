import sys
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
from ultraquery import UltraQuery
import os

def try_float_conversion(values):
    converted = []
    for val in values:
        try:
            converted.append(float(val))
        except ValueError:
            converted.append(val)
    return converted


plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333F4B'
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.color'] = '#A0A0A0'
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.7
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlepad'] = 15
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['xtick.color'] = '#333F4B'
plt.rcParams['ytick.color'] = "#303C48"
plt.rcParams['xtick.labelsize'] = 11
plt.rcParams['ytick.labelsize'] = 11

class UltraQuery_plot:
    def __init__(self, file, x, y):
        self.x = x
        self.y = y

        file_path = os.path.abspath(file)
        if not os.path.exists(file_path):
            print(f"[❌] File not found: {file_path}")
            exit(1)

        self.file = file

        # validate columns
        columns = UltraQuery.columns(self.file)
        if self.x not in columns:
            print(f"[✗] Column '{self.x}' not found.")
            sys.exit()
        if self.y not in columns:
            print(f"[✗] Column '{self.y}' not found.")
            sys.exit()

        # load both columns
        x_col = UltraQuery.listcolumn(self.file, self.x)
        y_col = UltraQuery.listcolumn(self.file, self.y)

        # align both columns by row index and filter bad rows
        self.x_val = []
        self.y_val = []
        for xi, yi in zip(x_col, y_col):
            if xi.strip() and yi.strip():  # skip empty
                self.x_val.append(xi.strip())
                self.y_val.append(yi.strip())

        # build counts for bar/pie/hist
        self.counts = dict(Counter(self.x_val))
        self.ycounts = dict(Counter(self.y_val))

    def _bar(self):
        x_final=try_float_conversion(self.x_val)
        y_final=try_float_conversion(self.y_val)
        bars = plt.bar(
            x_final,
            y_final,
            color=plt.cm.viridis_r(np.array(list(self.counts.values())) / max(np.array(list(self.counts.values())))),
            alpha=0.85,
            edgecolor='#222222',
            linewidth=0.8
        )
        plt.xlabel(self.x, fontsize=14)
        plt.ylabel(self.y, fontsize=14)
        plt.title(f'{self.x} vs {self.y}', fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, axis='y', alpha=0.6)
        plt.tight_layout()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()

    def _pie(self):
        x_final=try_float_conversion(self.x_val)
        y_final=try_float_conversion(self.y_val)
        plt.pie(
            y_final,
            labels=x_final,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.plasma(np.array(list(self.counts.values())) / max(np.array(list(self.counts.values())))),
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.7},
            textprops={'fontsize': 12, 'color': 'black'}
        )
        plt.title(f'Market Share by {self.x}', fontsize=16)
        plt.tight_layout()
        plt.show()

    def _line(self):
        x_final=try_float_conversion(self.x_val)
        y_final=try_float_conversion(self.y_val)

        plt.plot(x_final, y_final, marker='o', linestyle='-', color="#1575ba", alpha=0.85, linewidth=2)
        plt.xticks(rotation=45, ha='right')
        plt.xlabel(self.x, fontsize=14)
        plt.ylabel(self.y, fontsize=14)
        plt.title(f'{self.x} vs {self.y}', fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.tight_layout()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()


    def _scatter(self):
        x_final=try_float_conversion(self.x_val)
        y_final=try_float_conversion(self.y_val)
        plt.scatter(
            x_final,
            y_final,
            s=100,
            c=plt.cm.cividis(np.array(list(self.counts.values())) / max(np.array(list(self.counts.values())))),
            alpha=0.85,
            edgecolors='black',
            linewidth=0.7
        )
        plt.xlabel(self.x, fontsize=14)
        plt.ylabel(self.y, fontsize=14)
        plt.title(f'{self.x} vs {self.y}', fontsize=16)
        plt.xticks(rotation=45, ha='right')
        plt.grid(True, alpha=0.5)
        plt.tight_layout()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()

    def _histogram(self):
        y_final=try_float_conversion(self.y_val)
        plt.hist(
            y_final,
            bins=10,
            edgecolor='black',
            color=plt.cm.magma(0.7),
            alpha=0.85
        )
        plt.xlabel(self.x, fontsize=14)
        plt.ylabel(self.y, fontsize=14)
        plt.title(f'Distribution of {self.x}', fontsize=16)
        plt.grid(True, axis='y', alpha=0.6)
        plt.tight_layout()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()

