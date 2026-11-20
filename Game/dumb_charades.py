"""Run: python dumb_charades.py

Load a UTF-8 CSV with one term per row in its first column.
An optional first-row header (word, words, term, terms, or question) is skipped.
Set seconds before Next; use Apply / Restart Timer to change the current timer.
"""

import csv
import math
import random
import time
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox


def load_terms(path):
    """Read first-column terms, ignoring empty rows and duplicate terms."""
    with open(path, newline="", encoding="utf-8-sig") as handle:
        rows = [row[0].strip() for row in csv.reader(handle) if row and row[0].strip()]
    if rows and rows[0].casefold() in {"word", "words", "term", "terms", "question", "questions"}:
        rows.pop(0)
    terms = list(dict.fromkeys(rows))
    if not terms:
        raise ValueError("The CSV has no words in its first column.")
    return terms


class CharadesApp:
    BG = "#152238"

    def __init__(self, window):
        self.window = window
        self.terms = []
        self.deck = []
        self.index = 0
        self.timer_id = None
        self.deadline = None
        window.title("Dumb Charades — Technical Terms")
        window.geometry("900x580")
        window.minsize(700, 520)
        window.configure(bg=self.BG)
        window.protocol("WM_DELETE_WINDOW", self.close)

        self.label("TECHNICAL DUMB CHARADES", 18, "#8bd5ff").pack(pady=(22, 12))
        tk.Button(window, text="Load CSV…", command=self.choose_csv, font=("Arial", 13)).pack()
        self.file_label = self.label("Load a CSV: one word or phrase per row, first column.", 11)
        self.file_label.pack(pady=8)
        self.term_label = self.label("Load a CSV to begin", 32, "white")
        self.term_label.configure(wraplength=820)
        self.term_label.pack(expand=True, fill="both", padx=20)
        window.bind("<Configure>", self.resize)

        settings = tk.Frame(window, bg=self.BG)
        settings.pack(pady=8)
        tk.Label(settings, text="Duration (seconds):", bg=self.BG, fg="white", font=("Arial", 12)).pack(side=tk.LEFT)
        self.duration = tk.StringVar(value="60")
        tk.Spinbox(settings, from_=1, to=86400, textvariable=self.duration, width=7,
                   font=("Arial", 14)).pack(side=tk.LEFT, padx=8)
        self.apply_button = tk.Button(settings, text="Apply / Restart Timer", command=self.restart_timer, state=tk.DISABLED)
        self.apply_button.pack(side=tk.LEFT)
        self.timer_label = self.label("Time: --:--", 25, "#8bd5ff")
        self.timer_label.pack(pady=5)
        self.progress_label = self.label("0 / 0", 13)
        self.progress_label.pack(pady=5)
        buttons = tk.Frame(window, bg=self.BG)
        buttons.pack(pady=(10, 22))
        self.next_button = tk.Button(buttons, text="Next →", command=self.show_next,
                                     font=("Arial", 17, "bold"), width=12, bg="#8bd5ff", state=tk.DISABLED)
        self.next_button.pack(side=tk.LEFT, padx=10)
        self.restart_button = tk.Button(buttons, text="Restart Game", command=self.restart,
                                        font=("Arial", 17), width=13, state=tk.DISABLED)
        self.restart_button.pack(side=tk.LEFT, padx=10)

    def label(self, text, size, color="#b8c4d8"):
        return tk.Label(self.window, text=text, font=("Arial", size), bg=self.BG, fg=color)

    def resize(self, event):
        if event.widget is self.window:
            self.term_label.configure(wraplength=max(200, event.width - 50))

    def choose_csv(self):
        path = filedialog.askopenfilename(title="Choose words CSV", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if not path:
            return
        try:
            terms = load_terms(path)
        except (OSError, UnicodeError, csv.Error, ValueError) as error:
            messagebox.showerror("Could not load CSV", str(error))
            return
        self.terms = terms
        self.file_label.config(text=f"{Path(path).name} — {len(terms)} unique terms")
        self.restart_button.config(state=tk.NORMAL)
        self.restart()

    def seconds(self):
        try:
            value = int(self.duration.get())
            if not 1 <= value <= 86400:
                raise ValueError
            return value
        except ValueError:
            messagebox.showerror("Invalid duration", "Enter a whole number from 1 to 86400 seconds.")
            return None

    def cancel_timer(self):
        if self.timer_id is not None:
            self.window.after_cancel(self.timer_id)
            self.timer_id = None
        self.deadline = None

    def start_timer(self, seconds):
        self.cancel_timer()
        self.deadline = time.monotonic() + seconds
        self.tick()

    def tick(self):
        self.timer_id = None
        remaining = max(0, math.ceil(self.deadline - time.monotonic()))
        minutes, seconds = divmod(remaining, 60)
        self.timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}",
                                fg="#ff8585" if remaining <= 10 else "#8bd5ff")
        if remaining == 0:
            self.deadline = None
            self.timer_label.config(text="Time’s up!", fg="#ff8585")
            self.window.bell()
        else:
            self.timer_id = self.window.after(100, self.tick)

    def show_next(self):
        if self.index >= len(self.deck):
            return
        seconds = self.seconds()
        if seconds is None:
            return
        self.term_label.config(text=self.deck[self.index])
        self.index += 1
        suffix = " — Last term" if self.index == len(self.deck) else ""
        self.progress_label.config(text=f"{self.index} / {len(self.deck)}{suffix}")
        self.apply_button.config(state=tk.NORMAL)
        if self.index == len(self.deck):
            self.next_button.config(state=tk.DISABLED)
        self.start_timer(seconds)

    def restart_timer(self):
        if self.index:
            seconds = self.seconds()
            if seconds is not None:
                self.start_timer(seconds)

    def restart(self):
        self.cancel_timer()
        self.deck = self.terms.copy()
        random.shuffle(self.deck)
        self.index = 0
        self.term_label.config(text="Set duration, then click Next")
        self.timer_label.config(text="Time: --:--", fg="#8bd5ff")
        self.progress_label.config(text=f"0 / {len(self.deck)}")
        self.next_button.config(state=tk.NORMAL if self.deck else tk.DISABLED)
        self.apply_button.config(state=tk.DISABLED)

    def close(self):
        self.cancel_timer()
        self.window.destroy()


def main():
    window = tk.Tk()
    CharadesApp(window)
    window.mainloop()


if __name__ == "__main__":
    main()
