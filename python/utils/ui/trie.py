import tkinter      as tk
import tkinter.ttk  as ttk

class TrieExample(ttk.Frame):
    def __init__(self, parent, trie):
        super().__init__(parent)
        self._trie = trie
        self.master.title("Trie Example")
        self.pack(fill=tk.BOTH, expand=True)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        ttk.Label(self, text="Input:").grid(row=0, column=0)

        self._entry_var = tk.StringVar()
        self._entry_var.trace('w', self._on_change)
        ttk.Entry(self, textvariable=self._entry_var) \
            .grid(row=0, column=1, sticky=tk.W+tk.E)

        self._suggestions = tk.Listbox(self)
        self._suggestions.grid(row=1, column=0, columnspan=2,
                         sticky=tk.N+tk.S+tk.W+tk.E)

        scrollbar = tk.Scrollbar(self._suggestions, orient="vertical")
        scrollbar.config(command=self._suggestions.yview)
        scrollbar.pack(side="right", fill="y")
        self._suggestions.config(yscrollcommand=scrollbar.set)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

        self._on_change()

    def _on_change(self, name='', index=0, mode=''):
        self._suggestions.delete(0, tk.END)
        self._suggestions.insert(
            tk.END, *self._trie.find_all(self._entry_var.get())
        )

def run(trie) -> int:
    root = tk.Tk()
    root.geometry("300x300")
    TrieExample(root, trie)
    root.mainloop()
    return 0