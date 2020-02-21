import tkinter      as tk
import tkinter.ttk  as ttk

class LRUExample(ttk.Frame):
    def __init__(self, parent, cache):
        super().__init__(parent)
        self._cache = cache
        self.master.title(f"LRU Cache Example - Size = {self._cache.maxsize}")
        self.pack(fill=tk.BOTH, expand=True)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self._key_var = tk.StringVar()
        ttk.Entry(self, textvariable=self._key_var) \
            .grid(row=0, column=0, sticky=tk.W+tk.E)
        ttk.Button(self, text='ADD', command=self._on_add) \
            .grid(row=0, column=2, sticky=tk.W+tk.E)

        self._value_var = tk.StringVar()
        ttk.Entry(self, textvariable=self._value_var) \
            .grid(row=0, column=1, sticky=tk.W+tk.E)

        self._get_var = tk.StringVar()
        ttk.Entry(self, textvariable=self._get_var) \
            .grid(row=1, column=1, sticky=tk.W+tk.E)
        ttk.Button(self, text='GET', command=self._on_get) \
            .grid(row=1, column=2)

        self._get_label = ttk.Label(self)
        self._get_label.grid(row=1, column=3)

        self._items = tk.Listbox(self)
        self._items.grid(row=3, column=0, columnspan=4,
                         sticky=tk.N+tk.S+tk.W+tk.E)

        scrollbar = tk.Scrollbar(self._items, orient="vertical")
        scrollbar.config(command=self._items.yview)
        scrollbar.pack(side="right", fill="y")
        self._items.config(yscrollcommand=scrollbar.set)

        for child in self.winfo_children():
            child.grid_configure(padx=10, pady=10)

        self._on_get()

    def _on_get(self):
        value = 'No Value :)'
        if self._get_var.get():
            try:
                value = self._cache[self._get_var.get()]
            except KeyError:
                value = 'Not Found :('
        self._get_label.config(text=value)
        self._draw_cache()

    def _on_add(self):
        if self._key_var.get() and self._value_var.get():
            self._cache[self._key_var.get()] = self._value_var.get()
        self._draw_cache()

    def _draw_cache(self):
        self._items.delete(0, tk.END)
        self._items.insert(
            tk.END, *[f'{k} -> {v}' for k, v in self._cache.items()][::-1]
        )

def run(cache) -> int:
    root = tk.Tk()
    root.geometry("500x300")
    LRUExample(root, cache)
    root.mainloop()
    return 0
