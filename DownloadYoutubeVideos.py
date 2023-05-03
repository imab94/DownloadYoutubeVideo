import ttkbootstrap as ttk
import ttkbootstrap.dialogs
from ttkbootstrap.constants import *
from pytube import YouTube



def download_video():
    try:
        ytLink = entry.get().strip()
        ytObject = YouTube(ytLink,on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only("mp4")
        video.download()
    except Exception as e:
        ttkbootstrap.dialogs.Messagebox.show_error("failed to download", "video download failed!", alert=True)


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = bytes_downloaded / total_size * 100
    per  = str(int(percentage_of_compeletion))
    progress_bar.set(float(percentage_of_compeletion)/100)
    percentLabel.configure(textvariable=per + "%")
    percentLabel.update()

def confirm_quit():
    response  = ttkbootstrap.dialogs.Messagebox.yesnocancel("Are you sure want to exit?", "exit", alert=True)
    if response == "Yes":
        root.destroy()


root = ttk.Window(themename="morph")
root.title("YouTube Video Downloader")

per = ttk.StringVar()
url_var = ttk.StringVar()

# Download label
download_label = ttk.Label(root, text='Download any video from here', font=('Arial', 16))
download_label.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

# Video URL label
url_label = ttk.Label(root, text='Enter YouTube video URL:')
url_label.grid(row=1, column=0, padx=20, pady=10, sticky='w')

# Video URL entry
entry = ttk.Entry(root, width=50, font=('Arial 10'),textvariable=url_var)
entry.grid(row=2, column=0, padx=20, pady=10)

percentLabel = ttk.Label(root,text="0%")
percentLabel.grid(row=3,column=0,columnspan=3,padx=1,pady=1,rowspan=10)

# Progress bar
progress_bar = ttk.Progressbar(root,bootstyle="success",length=400,mode='determinate')
progress_bar.grid(row=4, column=0, columnspan=4,padx=10,pady=50)

# Download and cancel buttons
download_button = ttk.Button(root, text='Download', command=download_video)
download_button.grid(row=5, column=0, padx=20, pady=10, sticky='w')

cancel_button = ttk.Button(root, text='Cancel', command=confirm_quit)
cancel_button.grid(row=5, column=1, padx=5, pady=10, sticky='e')

root.mainloop()
