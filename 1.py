import tkinter as tk
from tkinter import ttk
import threading
import speedtest

def check_speed():
    global download_speed, upload_speed
    speed_test = speedtest.Speedtest()
    download = speed_test.download()
    upload = speed_test.upload()

    download_speed = round(download / (10 ** 6), 2)
    upload_speed = round(upload / (10 ** 6), 2)

def update_text():
    thread = threading.Thread(target=check_speed)
    thread.start()
    progress = ttk.Progressbar(root, orient=tk.HORIZONTAL, length=210, mode='indeterminate')
    progress.place(x=85, y=140)
    progress.start()

    while thread.is_alive():
        root.update()

    down_label.config(text=f"⏬ Download Speed - {download_speed} Mbps")
    up_label.config(text=f"⏫ Upload Speed - {upload_speed} Mbps")

    st = speedtest.Speedtest()
    st.get_best_server()
    ping = st.results.ping
    ping_label.config(text=f"Your Ping is - {ping} ms")

    progress.stop()
    progress.destroy()

root = tk.Tk()
root.title("Internet Speed Test")
root.geometry('380x260')
root.resizable(False, False)
root.configure(bg="#ffffff")

title_label = tk.Label(root, text='Internet Speed Test', bg='#ffffff', fg='#404042', font='Arial 23 bold')
title_label.pack()

down_label = tk.Label(root, text="⏬ Download Speed - ", bg='#fff', font='Arial 10 bold')
down_label.place(x=90, y=50)

up_label = tk.Label(root, text="⏫ Upload Speed - ", bg='#fff', font='Arial 10 bold')
up_label.place(x=90, y=80)

ping_label = tk.Label(root, text="Your Ping - ", bg='#fff', font='Arial 10 bold')
ping_label.place(x=90, y=110)

button = tk.Button(root, text="Check Speed ▶", width=30, bd=0, bg='#404042', fg='#fff', pady=5, command=update_text)
button.place(x=85, y=170)

root.mainloop()
