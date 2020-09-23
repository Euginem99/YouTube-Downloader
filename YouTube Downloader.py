import tkinter as tk
import os
import youtube_dl
import tkinter.font as tkfont


root = tk.Tk() 
root.title("YouTube Video Downloader Service")
root.geometry('400x400')

# Creating a canvas 
canvas1 = tk.Canvas(root,height = 400,width = 400,bg = "gray")
bold_font = tkfont.Font(family = "Helvetica", size = 12,weight = "bold")


label1 = tk.Label(root,text = "Enter the URL",width = 10,bg = None)
label1.config(font = bold_font)
canvas1.create_window(200,50,window = label1)
download_entry = tk.Entry(root)
canvas1.create_window(200,100,window = download_entry)

label2 = tk.Label(root,text = "Enter the Path",width = 10,bg = None)
label2.config(font = bold_font)
canvas1.create_window(200,150,window = label2)
path_entry = tk.Entry(root)
canvas1.create_window(200,200,window = path_entry)

canvas1.pack()

#Download
def get_video_url():
  search_item = download_entry.get()
  save_path = path_entry.get()
  ydl_opts = {'format': 'best','noplaylist':True,'extract-audio':True,}
  os.chdir(save_path)
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([search_item])
    
  bold_font2 = tkfont.Font(family="Helvetica",size=10,weight="bold")
  out_text = "Video Downloaded at "
  label3 =tk.Label(root,text= out_text.join(save_path),width=20,bg=None)
  label3.config(font=bold_font2)
  canvas1.create_window(200,350,window=label3)

download = tk.Button(text= "Download", padx=5,pady=5,fg = "white",bg = "red",command = get_video_url)
canvas1.create_window(200,250,window=download)

root.mainloop()
