import time
import matplotlib.pyplot as plt
import pandas as pd
import os

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

x = time.perf_counter()


class UltraQuery_plot:
    def __init__(self, file, x, y):
        self.x = x.strip()
        self.y = y.strip()

        file_path = os.path.abspath(file)
        if not os.path.exists(file_path):
            print(f"[❌] File not found: {file_path}")
            exit(1)

        # use encoding that won't crash on Windows CSVs
        self.file = pd.read_csv(file_path, encoding='ISO-8859-1', engine='python', on_bad_lines='skip')
        self.file.columns = self.file.columns.str.strip()

        print(f"[✓] Columns: {self.file.columns.tolist()}")

        if self.x not in self.file.columns:
            print(f"[✗] Column '{self.x}' not found.")
            exit(1)
        if self.y not in self.file.columns:
            print(f"[✗] Column '{self.y}' not found.")
            exit(1)

        self.counts = self.file[self.x].value_counts()

    def _bar(self):
        bars = plt.bar(
            self.counts.index,
            self.counts.values,
            color=plt.cm.viridis_r(self.counts.values / max(self.counts.values)),
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
        plt.pie(
            self.counts.values,
            labels=self.counts.index,
            autopct='%1.1f%%',
            startangle=140,
            colors=plt.cm.plasma(self.counts.values / max(self.counts.values)),
            wedgeprops={'edgecolor': 'black', 'linewidth': 0.7},
            textprops={'fontsize': 12, 'color': 'black'}
        )
        plt.title(f'Market Share by {self.x}', fontsize=16)
        plt.tight_layout()
        plt.show()

    def _line(self):
        x_vals = range(len(self.counts.index))
        y_vals = self.counts.values
        plt.plot(x_vals, y_vals, marker='o', linestyle='-', color="#1575ba", alpha=0.85, linewidth=2)
        plt.xticks(x_vals, self.counts.index, rotation=45, ha='right', fontsize=12)
        plt.xlabel(self.x, fontsize=14)
        plt.ylabel(self.y, fontsize=14)
        plt.title(f'{self.x} vs {self.y}', fontsize=16)
        plt.grid(True, alpha=0.5)
        plt.tight_layout()
        plt.gca().spines['top'].set_visible(False)
        plt.gca().spines['right'].set_visible(False)
        plt.show()

    def _scatter(self):
        plt.scatter(
            self.counts.index,
            self.counts.values,
            s=100,
            c=plt.cm.cividis(self.counts.values / max(self.counts.values)),
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
        plt.hist(
            self.counts.values,
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


if __name__ == "__main__":
    y = time.perf_counter()
    available_types = ['bar']
    print("Available plot types:", ", ".join(available_types))
    user_choice = input("Choose plot type: ").strip().lower()
    uq = UltraQuery_plot("cars.csv", "Engines", "CC/Battery Capacity")
    try:
        uq.plot(user_choice)
    except ValueError as e:
        print(e)

    print(f"Execution time: {y - x:.4f} seconds")
