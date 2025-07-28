import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from analyses.linear_regression import run as run_lr
from analyses.descriptive_stats import run as run_stats
from analyses.clustering import run as run_clust

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Data Analysis App")
        self.df = None

        tk.Button(self, text="Load CSV", command=self.load_csv).pack(pady=5)
        tk.Button(self, text="Descriptive Stats", command=self.do_stats).pack(pady=5)
        tk.Button(self, text="Linear Regression", command=self.do_lr).pack(pady=5)
        tk.Button(self, text="K-Means Clustering", command=self.do_clust).pack(pady=5)

    def load_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if not path:
            return
        try:
            self.df = pd.read_csv(path)
            messagebox.showinfo("Loaded", f"{len(self.df)} rows loaded.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def ensure_df(self):
        if self.df is None:
            messagebox.showwarning("No Data", "Please load a CSV first.")
            return False
        return True

    def do_stats(self):
        if self.ensure_df():
            run_stats(self.df)

    def do_lr(self):
        if self.ensure_df():
            run_lr(self.df)

    def do_clust(self):
        if self.ensure_df():
            run_clust(self.df)

if __name__ == "__main__":
    App().mainloop()
