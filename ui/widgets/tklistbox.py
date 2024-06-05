from tkinter import Frame, Listbox, SINGLE, END, SUNKEN

from ui.global_font import GlobalFont


class TKListbox:
    def __init__(self, master, items, **kwargs):
        self.master = master
        self.items = items
        self.kwargs = kwargs

    def create_listbox(self):
        listbox_frame = Frame(self.master, relief=SUNKEN, bd=2, bg="#AAAAAA")
        listbox_frame.pack(padx=50, pady=10, fill="both", expand=True, **self.kwargs)

        font = GlobalFont.get_global_font(font_size=22)
        listbox = Listbox(listbox_frame, selectmode=SINGLE, font=font, bg="#AAAAAA",
                          fg="black", borderwidth=0, selectbackground="#0000BA", selectforeground="white",
                          justify="center", activestyle='none')

        listbox_height = len(self.items)
        listbox.config(height=listbox_height)

        listbox.pack(fill="both", expand=True)  # 부모 프레임의 100% 채우기

        for item in self.items:
            # 각 항목을 가운데 정렬
            listbox.insert(END, f"{item['label']:^20}")

        listbox.bind("<Double-1>", self.on_double_click)
        self.listbox = listbox

        return listbox_frame

    def on_double_click(self, event):
        selected_index = self.listbox.curselection()

        if selected_index:
            selected_item = self.items[selected_index[0]]
            selected_item['on_item_selected'](selected_item['label'])


