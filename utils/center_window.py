def center_window(master):
    master.update_idletasks()
    width = master.winfo_width()
    height = master.winfo_height()
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    # 실제 윈도우 위치를 지정
    master.geometry(f'{width}x{height}+{x}+{y}')
