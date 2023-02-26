import tkinter as tk
from tkinter import filedialog
import pygame
import os
import random
from tkinter import *



class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Music App")
        self.master.geometry("500x350")
        Label(master,text="Sasta Spotify",fg="white",bg="black",borderwidth="3",font="Arial 10 bold italic").pack()
      

        # Create a frame for the playlist
        #self.playlist2_frame = tk.Frame(self.master)
#        self.playlist2_frame.pack(fill=tk.BOTH, expand=True)
        
        self.playlist_frame = tk.Frame(self.master)
        self.playlist_frame.pack(fill=tk.BOTH, expand=True)

        # Create a scrollbar for the playlist
        self.playlist_scrollbar = tk.Scrollbar(self.playlist_frame)
        self.playlist_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a listbox for the playlist
        self.playlist = tk.Listbox(self.playlist_frame, yscrollcommand=self.playlist_scrollbar.set, width=50)
        self.playlist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.playlist_scrollbar.config(command=self.playlist.yview)

        # Load the music directory
        self.music_directory = "/storage/emulated/0/songs_python"
        self.music_files = os.listdir(self.music_directory)
        for file in self.music_files:
            self.playlist.insert(tk.END, file)

        # Add buttons for controlling the music
        self.play_button = tk.Button(self.master, text="Play",bg="black", fg="white",command=self.play_music)
        self.stop_button = tk.Button(self.master, text="Stop",bg="black", fg="white",command=self.stop_music)
        self.pause_button = tk.Button(self.master, text="Pause",bg="black",fg="white", command=self.pause_music)
        self.resume_button = tk.Button(self.master, text="Resume",bg="black",fg="white", command=self.resume_music)
        self.shuffle_button = tk.Button(self.master, text="Shuffle", bg="black",fg="white",command=self.shuffle_music)
        self.volume_label = tk.Label(self.master, text="Volume:")
        self.volume_slider = tk.Scale(self.master, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)

        self.play_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.stop_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.pause_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.resume_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.shuffle_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.volume_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.volume_slider.pack(side=tk.LEFT, padx=10, pady=10)

        # Add buttons for manipulating the playlist
        self.add_button = tk.Button(self.master, text="Add", command=self.add_to_playlist)
        self.remove_button = tk.Button(self.master, text="Remove", command=self.remove_from_playlist)
        self.clear_button = tk.Button(self.master, text="Clear", command=self.clear_playlist)

        self.add_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.remove_button.pack(side=tk.LEFT, padx=10, pady=10)
        self.clear_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Add a menu for opening music files
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Files", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_music_file)

        # Initialize Pygame
        pygame.init()
        pygame.mixer.music.set_volume(0.5)

    def play_music(self):
        index = self.playlist.curselection()
        if index:
            file = self.playlist.get(index)
            path = os.path.join(self.music_directory, file)
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
        else:
            print("No music selected")

    def stop_music(self):
        pygame.mixer.music.stop()

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def shuffle_music(self):
        self.playlist.delete(0, tk.END)
        random.shuffle(self.music_files)
        for file in self.music_files:
            self.playlist.insert(tk.END, file)

    def set_volume(self, val):
        volume = int(val) / 100
        pygame.mixer.music.set_volume(volume)

    def add_to_playlist(self):
        file = filedialog.askopenfilename(initialdir="./", title="Select Music File", filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")))
        if file:
            filename = os.path.basename(file)
            self.playlist.insert(tk.END, filename)

    def remove_from_playlist(self):
        index = self.playlist.curselection()
        if index:
            self.playlist.delete(index)

    def clear_playlist(self):
        self.playlist.delete(0, tk.END)

    def open_music_file(self):
        file = filedialog.askopenfilename(initialdir="./", title="Select Music File", filetypes=(("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")))
        if file:
            filename = os.path.basename(file)
            self.playlist.insert(tk.END, filename)

root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()
